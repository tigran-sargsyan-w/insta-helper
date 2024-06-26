import time
from selenium.common import WebDriverException
from browser_utils import BrowserUtils
from selenium.webdriver.chrome.options import Options

# Check versions of Chrome and Selenium
# print(BrowserUtils.get_chrome_version_registry())
# print(BrowserUtils.get_chrome_version_selenium())
# print(BrowserUtils.get_selenium_version())

# Check functionality of BrowserUtils
try:
    options = Options()
    options.add_argument("lang=en")
    driver = BrowserUtils.get_chrome_driver(options)
    driver.get("https://www.google.com")
    while driver.window_handles:
        time.sleep(5)

except WebDriverException as e:
    driver.quit()
    print(f"WebDriverException: Something went wrong:")


