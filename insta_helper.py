import time
from selenium.common import WebDriverException, TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from browser_utils import BrowserUtils
from selenium_helper import SeleniumHelper
from xpath import xpath


def check_login_result(selenium_helper):
    if is_login_successful(selenium_helper):
        print("Login successful")
    else:
        print("Login failed, check your login and password...")


def is_login_successful(selenium_helper):
    try:
        incorrect_password_message = selenium_helper.wait_for_element("login", "incorrect_password")
        if incorrect_password_message is not None:
            return False
    except TimeoutException:
        return True


# Check functionality of BrowserUtils
try:
    options = Options()
    options.add_argument("lang=en")
    # Get the driver
    driver = BrowserUtils.get_chrome_driver(options)
    # Get the helper
    helper = SeleniumHelper(driver, xpath)

    driver.get('https://www.instagram.com/')

    cookie_allow_button = helper.wait_for_element("cookies", "allow_button")
    cookie_decline_button = helper.wait_for_element("cookies", "decline_button")

    # Click on the buttons (if needed to accept or decline cookies)
    cookie_allow_button.click()
    # cookie_decline_button.click()

    username_input = helper.wait_for_element("login", "username")
    password_input = helper.wait_for_element("login", "password")

    username_input.send_keys("username")
    password_input.send_keys("password")
    print("Login data entered")

    time.sleep(3)
    password_input.submit()
    print("Login data submitted")

    check_login_result(helper)

    while driver.window_handles:
        time.sleep(5)

except TimeoutException as e:
    print(f"TimeoutException: {e}")
except NoSuchElementException as e:
    print(f"NoSuchElementException: {e}")
except WebDriverException as e:
    driver.quit()
    print(f"WebDriverException: Perhaps the browser was closed")
