# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# # Setup Chrome
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# # Add the experimental option to keep the browser open
# options.add_experimental_option("detach", True) 

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Open Google
# driver.get("https://www.google.com")

# # Wait for the search box
# wait = WebDriverWait(driver, 10)
# search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))

# # Type the search text (without pressing Enter)
# search_box.send_keys("sunflower")

# # Wait for suggestions to appear
# time.sleep(3)

# # Get suggestions
# suggestions = driver.find_elements(By.XPATH, '//ul[@role="listbox"]//li//div[@role="option"]//span')
# for idx, s in enumerate(suggestions, 1):
#     print(f"{idx}. {s.text}")

# # The script will end here, but the browser will stay open

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# # Get user input for the search query
# search_query = input("What would you like to search for on Google? ")

# # Setup Chrome options
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# options.add_experimental_option("detach", True)

# # Initialize the WebDriver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Open Google
# driver.get("https://www.google.com")

# try:
#     # Wait for the search box to be present
#     wait = WebDriverWait(driver, 10)
#     search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))

#     # Type the user's search text into the search box
#     search_box.send_keys(search_query)

#     # Wait for the suggestions to appear (usually takes a moment)
#     # A short sleep is often necessary here to let the suggestions load
#     time.sleep(2)

#     # Locate and retrieve the suggestion elements
#     # The XPath targets the suggestion text within the listbox
#     suggestions = driver.find_elements(By.XPATH, '//ul[@role="listbox"]//li//div[@role="option"]//span')

#     # Check if any suggestions were found
#     if suggestions:
#         print(f"\nHere are the top suggestions for '{search_query}':")
#         for idx, s in enumerate(suggestions, 1):
#             suggestion_text = s.text
#             if suggestion_text:
#                 print(f"{idx}. {suggestion_text}")
#     else:
#         print("No suggestions found.")

# except Exception as e:
#     print(f"An error occurred: {e}")

# # The browser will remain open due to the detach option


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# # Get user input for the search query
# search_query = input("What would you like to search for on Google? ")

# # Setup Chrome options to keep the browser open
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# options.add_experimental_option("detach", True)

# # Initialize the WebDriver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Open Google
# driver.get("https://www.google.com")

# try:
#     # Wait for the search box to be present
#     wait = WebDriverWait(driver, 10)
#     search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))

#     # Type the user's search text into the search box
#     search_box.send_keys(search_query)

#     # Wait for the suggestions to appear
#     time.sleep(2)

#     # Locate the entire suggestions box
#     suggestions_box = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@role="listbox"]')))

#     # Take a screenshot of the suggestions box and save it as a file
#     suggestions_box.screenshot("suggestions.png")
#     print("\nSuggestions screenshot saved as 'suggestions.png'")

#     # --- Optional: Print the suggestion text to the console as well ---
#     suggestions = suggestions_box.find_elements(By.TAG_NAME, 'span')
#     if suggestions:
#         print(f"\nHere are the top suggestions for '{search_query}':")
#         for idx, s in enumerate(suggestions, 1):
#             if s.text:
#                 print(f"{idx}. {s.text}")
#     else:
#         print("No suggestions found.")

# except Exception as e:
#     print(f"An error occurred: {e}")

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from PIL import Image
# import pytesseract
# import time

# # --- Get user input for the search query ---
# search_query = input("What would you like to search for on Google? ")

# # --- Setup Chrome options ---
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# options.add_experimental_option("detach", True)

# # --- Initialize the WebDriver ---
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # --- Open Google ---
# driver.get("https://www.google.com")

# try:
#     # --- Wait for and interact with the search box ---
#     wait = WebDriverWait(driver, 10)
#     search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
#     search_box.send_keys(search_query)
#     time.sleep(2)

#     # --- Locate the entire suggestions box ---
#     suggestions_box = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@role="listbox"]')))
    
#     # --- Take a screenshot of the suggestions box and save it ---
#     screenshot_filename = "suggestions.png"
#     suggestions_box.screenshot(screenshot_filename)
#     print(f"\nSuggestions screenshot saved as '{screenshot_filename}'")

#     # --- Use pytesseract to convert the image to text ---
#     print("\n--- Converted Text from Image ---")
#     text = pytesseract.image_to_string(Image.open(screenshot_filename))
#     print(text)

# except Exception as e:
#     print(f"An error occurred: {e}")

# # The browser will remain open due to the detach option


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from PIL import Image
# import pytesseract
# import time

# # --- Get user input for the search query ---
# search_query = input("What would you like to search for on Google? ")

# # --- Setup Tesseract path (if needed) ---
# # pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract' # for Mac

# # --- Setup Chrome options ---
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# options.add_experimental_option("detach", True)

# # --- Initialize the WebDriver ---
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # --- Open Google ---
# driver.get("https://www.google.com")

# try:
#     # --- Wait for and interact with the search box ---
#     wait = WebDriverWait(driver, 10)
#     search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
#     search_box.send_keys(search_query)
#     time.sleep(2)

#     # --- Locate the entire suggestions box ---
#     suggestions_box = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@role="listbox"]')))
    
#     # --- Take a screenshot of the suggestions box and save it ---
#     screenshot_filename = "suggestions.png"
#     suggestions_box.screenshot(screenshot_filename)
#     print(f"\nSuggestions screenshot saved as '{screenshot_filename}'")

#     # --- Use pytesseract to convert the image to text ---
#     print("\n--- Converted Text from Image ---")
#     extracted_text = pytesseract.image_to_string(Image.open(screenshot_filename))
#     print(extracted_text)

#     # --- Save the extracted text to a text file ---
#     text_filename = "suggestions.txt"
#     with open(text_filename, 'w', encoding='utf-8') as file:
#         file.write(extracted_text)
#     print(f"Extracted text saved to '{text_filename}'")

# except Exception as e:
#     print(f"An error occurred: {e}")

# # The browser will remain open due to the detach option



# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from PIL import Image
# import pytesseract
# import time

# # --- Get user input for the search query ---
# search_query = input("What would you like to search for on Google? ")

# # --- Setup Tesseract path (if needed) ---
# # pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract' # for Mac

# # --- Setup Chrome options ---
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# options.add_experimental_option("detach", True)

# # --- Initialize the WebDriver ---
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # --- Open Google ---
# driver.get("https://www.google.com")

# try:
#     # --- Wait for and interact with the search box ---
#     wait = WebDriverWait(driver, 10)
#     search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
#     search_box.send_keys(search_query)
#     time.sleep(2)

#     # --- Locate the entire suggestions box ---
#     suggestions_box = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@role="listbox"]')))
    
#     # --- Take a screenshot of the suggestions box and save it ---
#     screenshot_filename = "suggestions.png"
#     suggestions_box.screenshot(screenshot_filename)
#     print(f"\nSuggestions screenshot saved as '{screenshot_filename}'")

#     # --- Use pytesseract to convert the image to text ---
#     print("\n--- Converted Text from Image ---")
#     extracted_text = pytesseract.image_to_string(Image.open(screenshot_filename))

#     # --- Add this filtering logic to remove the unwanted text ---
#     clean_lines = []
#     for line in extracted_text.split('\n'):
#         # We check for a recognizable brand name to ensure the line is valid
#         if "brand cloud" in line.lower():
#             clean_lines.append(line.strip())
    
#     # Join the cleaned lines back into a single string
#     cleaned_text = '\n'.join(clean_lines)

#     print(cleaned_text)

#     # --- Save the cleaned text to a text file ---
#     text_filename = "suggestions.txt"
#     with open(text_filename, 'w', encoding='utf-8') as file:
#         file.write(cleaned_text)
#     print(f"\nExtracted text saved to '{text_filename}'")

# except Exception as e:
#     print(f"An error occurred: {e}")

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from PIL import Image
# import pytesseract
# import time

# # --- Get user input for the search query ---
# search_query = input("What would you like to search for on Google? ")

# # --- Setup Tesseract path (if needed) ---
# # pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract' # for Mac

# # --- Setup Chrome options ---
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# options.add_experimental_option("detach", True)

# # --- Initialize the WebDriver ---
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # --- Open Google ---
# driver.get("https://www.google.com")

# try:
#     # Wait for and interact with the search box
#     wait = WebDriverWait(driver, 10)
#     search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
#     search_box.send_keys(search_query)

#     # Use a longer wait to ensure suggestions have fully loaded
#     time.sleep(4)
#     print("Waiting for suggestions to load...")

#     # --- Locate the entire suggestions box ---
#     suggestions_box = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@role="listbox"]')))
    
#     # Take a screenshot of the suggestions box and save it
#     screenshot_filename = "suggestions.png"
#     suggestions_box.screenshot(screenshot_filename)
#     print(f"\nSuggestions screenshot saved as '{screenshot_filename}'")

#     # --- Use pytesseract to convert the image to text ---
#     print("\n--- Converted Text from Image ---")
#     try:
#         # Open the saved screenshot and extract text
#         # extracted_text = pytesseract.image_to_string(Image.open(screenshot_filename))
#         extracted_text = pytesseract.image_to_string(Image.open(screenshot_filename), lang='jpn')

#         if extracted_text.strip():
#             print(extracted_text)

#             # --- Save the extracted text to a text file ---
#             text_filename = "suggestions.txt"
#             with open(text_filename, 'w', encoding='utf-8') as file:
#                 file.write(extracted_text)
#             print(f"Extracted text saved to '{text_filename}'")
#         else:
#             print("Didn't get any readable text from the image.")

#     except Exception as e:
#         print(f"An error occurred during OCR: {e}")

# except Exception as e:
#     print(f"An error occurred with Selenium: {e}")

# # The browser will remain open due to the detach option

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from PIL import Image
# import pytesseract
# import time

# # --- User input ---
# search_query = input("What would you like to search for on Google? ")

# # --- Setup Tesseract path if needed ---
# # pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'  # Mac
# # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows

# # --- Chrome options ---
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# options.add_experimental_option("detach", True)

# # --- Initialize WebDriver ---
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://www.google.com")

# try:
#     wait = WebDriverWait(driver, 10)

#     # --- Find search box and type query ---
#     search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
#     search_box.send_keys(search_query)

#     # --- Wait for suggestions to appear ---
#     time.sleep(4)  # Wait for suggestions to fully load

#     # --- Locate suggestions box ---
#     suggestions_box = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@role="listbox"]')))

#     # --- Screenshot suggestions ---
#     screenshot_filename = "suggestions.png"
#     suggestions_box.screenshot(screenshot_filename)
#     print(f"Suggestions screenshot saved as '{screenshot_filename}'")

#     # --- OCR: Extract text from image ---
#     print("\n--- Extracted Text from Image ---")
#     try:
#         extracted_text = pytesseract.image_to_string(Image.open(screenshot_filename), lang='jpn+eng')  # Use multiple languages if needed

#         if extracted_text.strip():
#             print(extracted_text)

#             # --- Save text ---
#             text_filename = "suggestions.txt"
#             with open(text_filename, 'w', encoding='utf-8') as f:
#                 f.write(extracted_text)
#             print(f"Extracted text saved to '{text_filename}'")
#         else:
#             print("No readable text found in the image.")

#     except Exception as e:
#         print(f"OCR error: {e}")

# except Exception as e:
#     print(f"Selenium error: {e}")
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from PIL import Image, ImageEnhance
# import pytesseract
# import time
# import os

# # --- Optional: Set up tesseract path manually if needed ---
# # For Windows:
# # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# # For Mac:
# # pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# # --- User input ---
# search_query = input("What would you like to search for on Google? ")

# # --- Chrome options ---
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# options.add_experimental_option("detach", True)

# # --- Initialize WebDriver ---
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://www.google.com")

# try:
#     wait = WebDriverWait(driver, 10)

#     # --- Find search box and type query ---
#     search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
#     search_box.send_keys(search_query)

#     # --- Wait for suggestions to appear ---
#     time.sleep(3)  # wait to ensure suggestions load

#     # --- Locate suggestions box ---
#     suggestions_box = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@role="listbox"]')))

#     # --- Screenshot suggestions ---
#     screenshot_filename = "suggestions.png"
#     suggestions_box.screenshot(screenshot_filename)
#     print(f"Suggestions screenshot saved as '{screenshot_filename}'")

#     # --- Image preprocessing for better OCR ---
#     img = Image.open(screenshot_filename)
#     img = img.convert('L')  # Convert to grayscale

#     # Enhance contrast
#     enhancer = ImageEnhance.Contrast(img)
#     img = enhancer.enhance(2.0)

#     # Apply threshold to binarize image
#     img = img.point(lambda x: 0 if x < 140 else 255, '1')

#     # Optional: Save processed image to debug
#     processed_image_filename = "processed_suggestions.png"
#     img.save(processed_image_filename)
#     print(f"Processed image saved as '{processed_image_filename}'")

#     # --- OCR: Extract text from processed image ---
#     print("\n--- Extracted Text from Image ---")
#     extracted_text = pytesseract.image_to_string(img, lang='eng')

#     if extracted_text.strip():
#         print(extracted_text)

#         # --- Save text to file ---
#         text_filename = "suggestions.txt"
#         with open(text_filename, 'w', encoding='utf-8') as f:
#             f.write(extracted_text)
#         print(f"Extracted text saved to '{text_filename}'")
#     else:
#         print("No readable text found in the image.")

# except Exception as e:
#     print(f"Error occurred: {e}")

# finally:
#     # Optional: Close the browser automatically after some delay
#     time.sleep(5)
#     driver.quit()
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from PIL import Image
# import pytesseract
# import time

# # --- User input ---
# search_query = input("What would you like to search for on Google? ")

# # --- Setup Tesseract path if needed ---
# # pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'  # Mac
# # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows

# # --- Chrome options ---
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# options.add_experimental_option("detach", True)

# # --- Initialize WebDriver ---
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://www.google.com")

# try:
#     wait = WebDriverWait(driver, 10)

#     # --- Find search box and type query ---
#     search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
#     search_box.send_keys(search_query)

#     # --- Wait for suggestions to appear ---
#     time.sleep(4)  # Wait for suggestions to fully load

#     # --- Locate suggestions box ---
#     suggestions_box = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@role="listbox"]')))

#     # --- Screenshot suggestions ---
#     screenshot_filename = "suggestions.png"
#     suggestions_box.screenshot(screenshot_filename)
#     print(f"Suggestions screenshot saved as '{screenshot_filename}'")

#     # --- OCR: Extract text from image ---
#     print("\n--- Extracted Text from Image (Raw) ---")
#     extracted_text = pytesseract.image_to_string(
#         Image.open(screenshot_filename),
#         lang='jpn+eng'  # Use multiple languages if needed
#     )
#     print(extracted_text)

#     # --- Save raw OCR text ---
#     raw_text_filename = "suggestions_raw.txt"
#     with open(raw_text_filename, 'w', encoding='utf-8') as f:
#         f.write(extracted_text)
#     print(f"Raw OCR text saved to '{raw_text_filename}'")

#     # --- Clean the OCR text ---
#     cleaned_lines = []
#     for line in extracted_text.splitlines():
#         line = line.strip()
#         # Ignore empty lines or lines that only contain garbage
#         if line and not all(c in "Qq|e1234567890-+@#$%^&*() " for c in line):
#             cleaned_lines.append(line)

#     cleaned_text = "\n".join(cleaned_lines)

#     # --- Save cleaned text ---
#     cleaned_text_filename = "suggestions_cleaned.txt"
#     with open(cleaned_text_filename, 'w', encoding='utf-8') as f:
#         f.write(cleaned_text)
#     print(f"Cleaned OCR text saved to '{cleaned_text_filename}'")

#     print("\n--- Cleaned OCR Text ---")
#     print(cleaned_text)

# except Exception as e:
#     print(f"Error: {e}")


# from selenium import webdriver
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from PIL import Image, ImageFilter
# import pytesseract
# import time


# # --- User input ---
# search_query = input("What would you like to search for on Google? ")

# # --- Setup Tesseract path if needed ---
# # pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'  # Mac
# # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows

# # --- Chrome options ---
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# options.add_experimental_option("detach", True)  # Keep Chrome open after script ends

# # --- Initialize WebDriver ---
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://www.google.com")

# try:
#     wait = WebDriverWait(driver, 10)

#     # --- Find search box and type query ---
#     search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
#     search_box.send_keys(search_query)

#     # --- Wait for suggestions to appear ---
#     time.sleep(4)  # Wait for suggestions to fully load

#     # --- Locate suggestions box ---
#     suggestions_box = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@role="listbox"]')))

#     # --- Screenshot suggestions ---
#     screenshot_filename = "suggestions.png"
#     suggestions_box.screenshot(screenshot_filename)
#     print(f"Suggestions screenshot saved as '{screenshot_filename}'")

#     # --- Open image, resize and sharpen for better OCR ---
#     img = Image.open(screenshot_filename)
#     img = img.resize((img.width*2, img.height*2), Image.Resampling.LANCZOS)
#     img = img.filter(ImageFilter.SHARPEN)

#     # --- OCR: Extract text exactly as in image ---
#     # Include all languages you expect in the image
#     extracted_text = pytesseract.image_to_string(img, lang='ben+eng+jpn')

#     # --- Save verbatim OCR text ---
#     text_filename = "suggestions_exact.txt"
#     with open(text_filename, 'w', encoding='utf-8') as f:
#         f.write(extracted_text)

#     print(f"\nExtracted text saved exactly as in image to '{text_filename}'")
#     print("\n--- Extracted Text ---")
#     print(extracted_text)

# except Exception as e:
#     print(f"Error: {e}")

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
