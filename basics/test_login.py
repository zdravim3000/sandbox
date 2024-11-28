from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Set up Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode if GUI is not needed
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Path to your ChromeDriver
chromedriver_path = "/usr/bin/chromedriver"  # Update with the correct path

def test_prd():
    try:
        # Set up the WebDriver
        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Open Google
        driver.get("https://www.google.com")

        # Assert the title
        assert "Google" in driver.title, "Title does not match expected value!"

        print("Test passed: Google is successfully opened, and the title is correct.")

    except WebDriverException as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        if 'driver' in locals():
            driver.quit()
