from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image, ImageFilter
import pytesseract
import time

# --- User input ---
search_query = input("What would you like to search for on Google? ")

# --- Chrome options ---
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

# --- Initialize WebDriver ---
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com")

try:
    wait = WebDriverWait(driver, 10)

    # --- Find search box and type query ---
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    search_box.send_keys(search_query)

    # --- Wait for suggestions to appear ---
    time.sleep(4)

    # --- Screenshot the entire visible browser window ---
    full_screenshot_filename = "google_search_with_suggestions.png"
    driver.save_screenshot(full_screenshot_filename)
    print(f"Full page screenshot saved as '{full_screenshot_filename}'")

    # --- Load image for OCR ---
    img = Image.open(full_screenshot_filename)
    img = img.resize((img.width*2, img.height*2), Image.Resampling.LANCZOS)
    img = img.filter(ImageFilter.SHARPEN)

    # --- OCR: Extract text exactly as in image ---
    extracted_text = pytesseract.image_to_string(img, lang='ben+eng+jpn')

    # --- Save verbatim OCR text ---
    text_filename = "suggestions_with_input_text.txt"
    with open(text_filename, 'w', encoding='utf-8') as f:
        f.write(extracted_text)

    print(f"\nExtracted text saved exactly as in image to '{text_filename}'")
    print("\n--- Extracted Text ---")
    print(extracted_text)

except Exception as e:
    print(f"Error: {e}")
