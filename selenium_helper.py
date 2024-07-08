import random
import time

from selenium.webdriver import ActionChains, Keys
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

    def perform_random_human_like_actions(self):
        actions = [
            self.scroll_page,
            self.move_mouse_randomly,
            self.click_random_pixel,
            self.hover_over_element,
            self.input_text,
            self.press_random_keys,
            self.highlight_text
        ]
        random.choice(actions)()

    def scroll_page(self):
        action = ActionChains(self.driver)
        scroll_amount = random.randint(100, 1000)
        direction = random.choice([-1, 1])
        self.random_delay(1, 3)
        action.scroll_by_amount(0, direction * scroll_amount).perform()
        self.random_delay(1, 3)
        print(f"Page scrolled by {direction * scroll_amount} pixels")

    def move_mouse_randomly(self):
        self.perform_random_mouse_action(action_type="move")

    def click_random_pixel(self):
        self.perform_random_mouse_action(action_type="click")

    def hover_over_element(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, "a, button, div, img")
        if elements:
            element = random.choice(elements)
            action = ActionChains(self.driver)
            self.random_delay(1, 3)
            action.move_to_element(element).perform()
            self.random_delay(1, 3)
            print(f"Element hovered: {element.get_attribute('outerHTML')}")

    def input_text(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, "input[type='text'], textarea")
        if elements:
            element = random.choice(elements)
            action = ActionChains(self.driver)
            text = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(5, 15)))
            self.random_delay(1, 3)
            action.move_to_element(element).click().send_keys(text).perform()
            self.random_delay(1, 3)
            print(f"Text entered: {text} in element: {element.get_attribute('outerHTML')}")

    def press_random_keys(self):
        keys = [Keys.ARROW_UP, Keys.ARROW_DOWN, Keys.PAGE_UP, Keys.PAGE_DOWN]
        key_names = {
            Keys.ARROW_UP: "ARROW_UP",
            Keys.ARROW_DOWN: "ARROW_DOWN",
            Keys.PAGE_UP: "PAGE_UP",
            Keys.PAGE_DOWN: "PAGE_DOWN"
        }
        key = random.choice(keys)
        self.random_delay(1, 3)
        action = ActionChains(self.driver)
        action.send_keys(key).perform()
        self.random_delay(1, 3)
        print(f"Pressed key: {key_names[key]}")

    def highlight_text(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, "p, span, h1, h2, h3, h4, h5, h6")
        if elements:
            element = random.choice(elements)
            action = ActionChains(self.driver)
            self.random_delay(1, 3)
            action.move_to_element(element).click_and_hold().move_by_offset(10, 0).release().perform()
            self.random_delay(1, 3)
            print(f"Highlighted text in element: {element.get_attribute('outerHTML')}")

    def perform_random_mouse_action(self, action_type="move"):
        width = self.driver.execute_script("return window.innerWidth")
        height = self.driver.execute_script("return window.innerHeight")
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        self.random_delay(1, 3)
        action = ActionChains(self.driver)
        action.move_by_offset(x, y)

        if action_type == "click":
            action.click()

        action.perform()
        self.random_delay(1, 3)
        print(f"Mouse {action_type.capitalize()}d at coordinates: ({x}, {y})")
