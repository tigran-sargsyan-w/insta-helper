import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import winreg as reg


class BrowserUtils:
    @staticmethod
    def get_chrome_driver(options=None, service=None):
        if options is None:
            options = Options()

        if service is None:
            service = ChromeService(ChromeDriverManager().install())

        driver = webdriver.Chrome(service=service, options=options)
        return driver

    @staticmethod
    def get_selenium_version():
        return selenium.__version__

    @staticmethod
    def get_chrome_version_selenium():
        options = Options()
        options.add_argument("--headless")
        driver = BrowserUtils.get_chrome_driver(options=options)
        chrome_version = driver.capabilities['browserVersion']
        driver.quit()
        return chrome_version

    @staticmethod
    def get_chrome_version_registry():
        try:
            key_path = r"SOFTWARE\Google\Chrome\BLBeacon"
            key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_path)
            version, _ = reg.QueryValueEx(key, "version")
            return version
        except WindowsError:
            return None
