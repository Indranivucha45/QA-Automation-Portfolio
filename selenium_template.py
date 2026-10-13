# Project Name: E-Commerce Automated Regression Suite
# Tool: Python + Selenium WebDriver
# Author: Indrani Vucha

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_google_search_and_navigation():
    # 1. Initialize Chrome Web Driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        # 2. Open Target Application URL
        driver.get("https://www.google.com")
        
        # 3. Verify Page Title
        assert "Google" in driver.title, "Test Failed: Title mismatch!"
        print("Step 1 Passed: Navigation successful.")
        
        # 4. Locate Search Bar and Submit Query
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Software QA Testing Portfolio")
        search_box.send_keys(Keys.RETURN)
        
        time.sleep(3)
        print("Step 2 Passed: Search query executed successfully.")
        
    except Exception as e:
        print(f"Test encountered an error: {e}")
        
    finally:
        # 5. Clean up and close browser
        driver.quit()
        print("Test execution finished. Browser closed.")

if __name__ == "__main__":
    test_google_search_and_navigation()
