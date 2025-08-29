import pytesseract
from PIL import Image
from tkinter import Tk, filedialog
import json
import os
import re

# Hide Tkinter root
Tk().withdraw()

# Open file dialog (multiple selection allowed)
file_paths = filedialog.askopenfilenames(
    title="Select images",
    filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff")]
)

results = {}

if file_paths:
    for file_path in file_paths:
        # Open image
        image = Image.open(file_path)

        # Extract Japanese text with OCR
        text = pytesseract.image_to_string(image, lang='jpn', config="--psm 6")

        # Split into raw lines
        raw_lines = text.strip().splitlines()

        # Clean lines: remove OCR artifacts like "Q" from search icons
        lines = []
        for line in raw_lines:
            # Remove "Q", punctuation, or stray symbols if at the **start** of the line
            clean_line = re.sub(r'^[Q。、|]+', '', line).strip()
            if clean_line:  # keep only non-empty lines
                lines.append(clean_line)

        # Store results with filename as key
        filename = os.path.basename(file_path)
        results[filename] = lines if lines else ["No text detected"]

    # Save all results into sug.json
    with open("sug.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print("\n✅ Text from all images saved to sug.json")
else:
    print("No files selected.")
