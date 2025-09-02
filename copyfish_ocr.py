import requests
from tkinter import Tk, filedialog
from PIL import Image, ImageEnhance
from io import BytesIO
import os

# -------------------------------
API_KEY = "K87899389288957"
URL = "https://api.ocr.space/parse/image"

MAX_SIZE = (1200, 1200)   # max image dimensions
TIMEOUT = 180              # seconds
OUTPUT_FILE = "all_images_ocr.txt"  # single output file
LANGUAGE = "jpn"          # change to "eng", "ben", etc.
CONTRAST = 2              # contrast enhancement factor
THRESHOLD = None           # optional threshold for binarization (e.g., 180)
# -------------------------------

# --- Step 1: Preprocessing function ---
def preprocess_image(file_path, max_size=MAX_SIZE, contrast=CONTRAST, threshold=THRESHOLD):
    img = Image.open(file_path)
    img = img.convert("L")  # grayscale
    img = ImageEnhance.Contrast(img).enhance(contrast)
    img.thumbnail(max_size)
    
    # Optional binarization
    if threshold:
        img = img.point(lambda p: 255 if p > threshold else 0)
    
    # Crop whitespace
    img = img.crop(img.getbbox())
    
    # Save to in-memory bytes
    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)
    return img_bytes

# --- Step 2: Pick multiple images ---
root = Tk()
root.withdraw()
file_paths = filedialog.askopenfilenames(
    title="Select one or more images",
    filetypes=[
        ("Image files", "*.png *.jpg *.jpeg *.bmp *.tif *.tiff *.pdf"),
        ("All files", "*.*"),
    ]
)

if not file_paths:
    print("❌ No files selected")
    exit()

# Open the output file in the script directory
script_dir = os.getcwd()
output_path = os.path.join(script_dir, OUTPUT_FILE)

with open(output_path, "w", encoding="utf-8") as final_out:

    # --- Step 3: Process each image ---
    for file_path in file_paths:
        image_name = os.path.basename(file_path)
        print(f"\n📂 Processing file: {file_path}")

        try:
            img_bytes = preprocess_image(file_path)
            files = {"file": ("image.png", img_bytes, "image/png")}
        except Exception as e:
            print("⚠️ Preprocessing failed, using original image:", e)
            files = {"file": (image_name, open(file_path, "rb"), "image/png")}

        # --- Step 4: Upload to OCR.space ---
        payload = {
            "apikey": API_KEY,
            "language": LANGUAGE,
            "OCREngine": 2,  # high accuracy
        }

        try:
            response = requests.post(URL, data=payload, files=files, timeout=TIMEOUT)
            result = response.json()
        except requests.exceptions.RequestException as e:
            print("❌ Request failed:", e)
            continue

        if isinstance(files["file"][1], BytesIO):
            files["file"][1].close()

        # --- Step 5: Handle Engine 2 timeout by falling back to Engine 1 ---
        if result.get("IsErroredOnProcessing") and any("E101" in str(err) for err in result.get("ErrorMessage", [])):
            print("⚠️ Engine 2 timed out, retrying with Engine 1...")
            payload["OCREngine"] = 1
            try:
                response = requests.post(URL, data=payload, files=files, timeout=TIMEOUT)
                result = response.json()
            except requests.exceptions.RequestException as e:
                print("❌ Retry with Engine 1 failed:", e)
                continue

        # --- Step 6: Extract text safely ---
        if result.get("IsErroredOnProcessing"):
            print("❌ OCR failed:", result.get("ErrorMessage"))
            continue

        parsed_results = result.get("ParsedResults")
        if parsed_results and len(parsed_results) > 0:
            text = parsed_results[0].get("ParsedText", "")
            final_out.write(f"\n--- {image_name} ---\n")
            final_out.write(text + "\n")
            print(f"✅ Text from '{image_name}' added to {OUTPUT_FILE}")
        else:
            print("❌ No parsed results. Full response:")
            print(result)

print(f"\n✅ All OCR results saved in: {output_path}")
