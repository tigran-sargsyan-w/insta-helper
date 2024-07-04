import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumHelper:
    def __init__(self, driver, xpath_dictionary):
        self.driver = driver
        self.xpath_dictionary = xpath_dictionary

    def read_xpath(self, category, xpath_name):
        return self.xpath_dictionary[category][xpath_name]

    def wait_for_element(self, category, xpath_name, timeout=5):
        element_xpath = self.read_xpath(category, xpath_name)
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, element_xpath))
        )

    @staticmethod
    def random_delay(min_delay=1, max_delay=5):
        time.sleep(random.uniform(min_delay, max_delay))
