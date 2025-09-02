import requests
from tkinter import Tk, filedialog
from PIL import Image, ImageEnhance
from io import BytesIO
import os

# -------------------------------
# Your OCR.space / Copyfish API key
API_KEY = "K87899389288957"
URL = "https://api.ocr.space/parse/image"

# Maximum image size (width, height) to prevent timeout
MAX_SIZE = (2000, 2000)  # pixels
TIMEOUT = 60  # seconds for API request
# -------------------------------

# --- Step 1: Pick multiple images from Mac ---
root = Tk()
root.withdraw()  # hide Tkinter window
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

# --- Step 2: Process each image ---
for file_path in file_paths:
    print(f"\n📂 Processing file: {file_path}")

    try:
        # Open image
        img = Image.open(file_path)

        # Preprocess: grayscale + contrast
        img = img.convert("L")
        img = ImageEnhance.Contrast(img).enhance(2)

        # Resize if too large
        img.thumbnail(MAX_SIZE)

        # Save to in-memory bytes
        img_bytes = BytesIO()
        img.save(img_bytes, format="PNG")
        img_bytes.seek(0)

        # Use a proper filename and content-type for OCR.space
        files = {"file": ("image.png", img_bytes, "image/png")}

    except Exception as e:
        print("⚠️ Could not preprocess image, using original:", e)
        # fallback to original file
        files = {"file": (os.path.basename(file_path), open(file_path, "rb"), "image/png")}

    # --- Step 3: Upload to OCR.space ---
    payload = {
        "apikey": API_KEY,
        "language": "jpn",   # change to "ben", "jpn", etc. if needed
        "OCREngine": 1,      # 1 = faster, 2 = more accurate
    }

    try:
        response = requests.post(URL, data=payload, files=files, timeout=TIMEOUT)
        result = response.json()
    except requests.exceptions.RequestException as e:
        print("❌ Request failed:", e)
        continue

    # Close BytesIO if used
    if isinstance(files["file"][1], BytesIO):
        files["file"][1].close()

    # --- Step 4: Safe parsing of OCR result ---
    if result.get("IsErroredOnProcessing"):
        print("❌ OCR failed:", result.get("ErrorMessage"))
        continue

    parsed_results = result.get("ParsedResults")
    if parsed_results and len(parsed_results) > 0:
        text = parsed_results[0].get("ParsedText", "")

        # Save text to .txt file in same folder
        image_dir = os.path.dirname(file_path)
        image_name = os.path.splitext(os.path.basename(file_path))[0]
        output_file = os.path.join(image_dir, image_name + "_ocr.txt")

        with open(output_file, "w", encoding="utf-8") as out:
            out.write(text)

        print(f"✅ Extracted text saved to: {output_file}")

    else:
        print("❌ No parsed results. Full response:")
        print(result)
