import time

from selenium.common import WebDriverException, TimeoutException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options

from filesystem_utils import FileUtils
from user_data import UserData
from browser_utils import BrowserUtils
from selenium_helper import SeleniumHelper
from xpath import xpath


class InstaHelper:
    def __init__(self):
        self.driver = None
        self.helper = None

    def run(self):
        file_utils = FileUtils()
        username = "aromaze.fr"
        message = "Hello, this is a test message!"

        try:
            self.initialize_driver_and_helper()

            self.driver.get('https://www.instagram.com/')
            self.helper.random_delay()
            self.handle_cookies()

            self.helper.perform_random_human_like_actions()

            self.helper.random_delay()
            self.handle_login(UserData.username, UserData.password)
            self.helper.random_delay()
            self.check_login_result()

            self.handle_browser_notifications()

            self.visit_user_page(username)
            self.helper.random_delay()

            self.handle_browser_notifications()
            self.helper.perform_random_human_like_actions()

            # self.send_message(username, message)

            while self.driver.window_handles:
                time.sleep(1)

        except TimeoutException as e:
            print(f"TimeoutException: ")
        except NoSuchElementException as e:
            print(f"NoSuchElementException: ")
        except WebDriverException as e:
            self.driver.quit()
            print(f"WebDriverException: Perhaps the browser was closed")

    def initialize_driver_and_helper(self):
        options = Options()
        options.add_argument("lang=en")
        options.add_argument("user-agent=Your User-Agent String Here")
        # options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--profile-directory=Default")
        options.add_argument("--incognito")
        options.add_argument("--disable-plugins-discovery")
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

    def handle_browser_notifications(self):
        try:
            notification_turn_on_button = self.helper.wait_for_element("notification", "turn_on_button")
            notification_not_now_button = self.helper.wait_for_element("notification", "not_now_button")

            # Click on the buttons (if needed to turn on or not now for notifications)
            # notification_turn_on_button.click()
            notification_not_now_button.click()
            print("Notifications handled")
        except TimeoutException:
            print("No browser notification switcher found")
            return

    def handle_login(self, username, password):
        username_input = self.helper.wait_for_element("login", "username")
        password_input = self.helper.wait_for_element("login", "password")
        username_input.send_keys(username)
        password_input.send_keys(password)
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

    def visit_user_page(self, username):
        self.driver.get(f'https://www.instagram.com/{username}/')
        print(f"Go to user page {username}")

    def send_message(self, username, message):
        try:
            message_button = self.helper.wait_for_element("user_page", "message_button")
            if not message_button:
                print(f"Message button not found for {username}")
                return
            message_button.click()
            self.helper.random_delay()
            message_area = self.helper.wait_for_element("user_page", "message_area")
            message_area.send_keys(message)
            print(f"Message: {message} entered for {username}")
            self.helper.random_delay()
            message_area.send_keys(Keys.RETURN)
            print(f"Message sent to {username}")
            if not message_area:
                print(f"Message area not found for {username}")
                return
        except TimeoutException:
            print(f"Message button not found for {username}")
            return
