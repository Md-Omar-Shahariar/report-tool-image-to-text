import requests
from tkinter import Tk, filedialog
from PIL import Image, ImageEnhance
from io import BytesIO
import os

# -------------------------------
API_KEY = "K87899389288957"
URL = "https://api.ocr.space/parse/image"

MAX_SIZE = (2000, 2000)  # max image dimensions
TIMEOUT = 60              # API timeout in seconds
# -------------------------------

# --- Step 1: Pick multiple images ---
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

# --- Step 2: Process each image ---
for file_path in file_paths:
    print(f"\n📂 Processing file: {file_path}")

    try:
        # Open and preprocess image
        img = Image.open(file_path)
        img = img.convert("L")  # grayscale
        img = ImageEnhance.Contrast(img).enhance(2)
        img.thumbnail(MAX_SIZE)  # resize if too large

        # Save to in-memory bytes
        img_bytes = BytesIO()
        img.save(img_bytes, format="PNG")
        img_bytes.seek(0)

        # Proper filename for OCR.space
        files = {"file": ("image.png", img_bytes, "image/png")}

    except Exception as e:
        print("⚠️ Could not preprocess image, using original:", e)
        files = {"file": (os.path.basename(file_path), open(file_path, "rb"), "image/png")}

    # --- Step 3: Upload to OCR.space ---
    payload = {
        "apikey": API_KEY,
        "language": "eng",  # change to "ben", "jpn", etc.
        "OCREngine": 1,     # 1 = faster, 2 = more accurate
    }

    try:
        response = requests.post(URL, data=payload, files=files, timeout=TIMEOUT)
        result = response.json()
    except requests.exceptions.RequestException as e:
        print("❌ Request failed:", e)
        continue

    if isinstance(files["file"][1], BytesIO):
        files["file"][1].close()

    # --- Step 4: Extract & save text in script directory ---
    if result.get("IsErroredOnProcessing"):
        print("❌ OCR failed:", result.get("ErrorMessage"))
        continue

    parsed_results = result.get("ParsedResults")
    if parsed_results and len(parsed_results) > 0:
        text = parsed_results[0].get("ParsedText", "")

        # Save in the directory where this Python script is running
        script_dir = os.getcwd()  # current working directory
        image_name = os.path.splitext(os.path.basename(file_path))[0]
        output_file = os.path.join(script_dir, image_name + "_ocr.txt")

        with open(output_file, "w", encoding="utf-8") as out:
            out.write(text)

        print(f"✅ Extracted text saved to: {output_file}")

    else:
        print("❌ No parsed results. Full response:")
        print(result)
