import os
import time
import random
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# version 2 - with bottom suggestions
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)
SUGGESTIONS_FILE = "suggestions.json"
# Load existing suggestions
if os.path.exists(SUGGESTIONS_FILE):
    try:
        with open(SUGGESTIONS_FILE, "r", encoding="utf-8") as f:
            suggestions_data = json.load(f)
    except json.JSONDecodeError:
        suggestions_data = {}
else:
    suggestions_data = {}
keyword = input("Enter keyword to search: ").strip()
if not keyword:
    print("No keyword entered. Exiting.")
    exit()
# Setup Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 " \
             "(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")
driver = webdriver.Chrome(options=chrome_options)
driver.execute_cdp_cmd(
    'Page.addScriptToEvaluateOnNewDocument',
    {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined});'}
)
try:
    driver.get("https://www.google.com/")
    time.sleep(random.uniform(1, 2))
    # Enter keyword
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(keyword)
    time.sleep(random.uniform(1, 2))
    # Wait for autocomplete box
    suggestion_box = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ul[role='listbox']"))
    )
    # Screenshot autocomplete
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = os.path.join(SCREENSHOT_DIR, f"{keyword}_suggestions_{timestamp}.png")
    suggestion_box.screenshot(screenshot_path)
    print(f":camera_with_flash: Suggestions screenshot saved: {screenshot_path}")
    # Extract autocomplete suggestions
    suggestion_elements = suggestion_box.find_elements(By.CSS_SELECTOR, "li span")
    clean_lines = [elem.text.strip() for elem in suggestion_elements if elem.text.strip()]
    # Save to JSON
    if keyword not in suggestions_data:
        suggestions_data[keyword] = {"autocomplete": [], "related_searches": []}
    for line in clean_lines:
        if line not in suggestions_data[keyword]["autocomplete"]:
            suggestions_data[keyword]["autocomplete"].append(line)
    # Perform the search
    search_box.send_keys(Keys.ENTER)
    # Wait for results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )
    # Scroll to bottom to load related searches
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    # Grab the bottom section with id=botstuff
    try:
        bottom_section = driver.find_element(By.ID, "bres")
        # Screenshot bottom suggestions
        bottom_screenshot_path = os.path.join(SCREENSHOT_DIR, f"{keyword}_bottom_{timestamp}.png")
        bottom_section.screenshot(bottom_screenshot_path)
        print(f":camera_with_flash: Bottom-of-page screenshot saved: {bottom_screenshot_path}")
        # Extract related searches
        bottom_links = bottom_section.find_elements(By.CSS_SELECTOR, "a[href^='/search']")
        bottom_suggestions = [link.text.strip() for link in bottom_links if link.text.strip()]
        for line in bottom_suggestions:
            if line not in suggestions_data[keyword]["related_searches"]:
                suggestions_data[keyword]["related_searches"].append(line)
    except Exception:
        print(":warning: No bottom related searches found.")
    # Save updated JSON
    with open(SUGGESTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(suggestions_data, f, ensure_ascii=False, indent=2)
    print(f":white_tick: Suggestions for '{keyword}' saved to {SUGGESTIONS_FILE}")
finally:
    driver.quit()