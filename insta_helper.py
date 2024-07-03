import time
from selenium.common import WebDriverException, TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from browser_utils import BrowserUtils
from selenium_helper import SeleniumHelper
from xpath import xpath


class InstaHelper:
    def __init__(self):
        self.driver = None
        self.helper = None

    def initialize_driver_and_helper(self):
        options = Options()
        options.add_argument("lang=en")
        # Get the driver
        self.driver = BrowserUtils.get_chrome_driver(options)
        # Get the helper
        self.helper = SeleniumHelper(self.driver, xpath)
        print("Driver and helper initialized")

    def handle_cookies(self):
        cookie_allow_button = self.helper.wait_for_element("cookies", "allow_button")
        cookie_decline_button = self.helper.wait_for_element("cookies", "decline_button")
        # Click on the buttons (if needed to accept or decline cookies)
        cookie_allow_button.click()
        # cookie_decline_button.click()
        print("Cookies handled")

    def handle_login(self):
        username_input = self.helper.wait_for_element("login", "username")
        password_input = self.helper.wait_for_element("login", "password")
        username_input.send_keys("username")
        password_input.send_keys("password")
        print("Login data entered")
        time.sleep(2)
        password_input.submit()
        print("Login data submitted")

    def check_login_result(self):
        if self.is_login_successful():
            print("Login successful")
        else:
            print("Login failed, check your login and password...")

    def is_login_successful(self):
        try:
            incorrect_password_message = self.helper.wait_for_element("login", "incorrect_password")
            if incorrect_password_message is not None:
                return False
        except TimeoutException:
            return True

    def run(self):
        try:
            self.initialize_driver_and_helper()

            self.driver.get('https://www.instagram.com/')
            self.handle_cookies()
            self.handle_login()
            self.check_login_result()

            while self.driver.window_handles:
                time.sleep(5)

        except TimeoutException as e:
            print(f"TimeoutException: {e}")
        except NoSuchElementException as e:
            print(f"NoSuchElementException: {e}")
        except WebDriverException as e:
            self.driver.quit()
            print(f"WebDriverException: Perhaps the browser was closed")
