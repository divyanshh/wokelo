import time

from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By

from src.website_handlers.abc_webite_handler import WebsiteHandler


class MomiBabyWebsiteHandler(WebsiteHandler):
    def load_website(self, url):
        self.driver.get(url)
        time.sleep(5)

    def block_modals(self):
        label_buttons = [
            "button[aria-label='Close dialog 1']",
            "button[aria-label='Dismiss campaign']",
            "button[aria-label='Close messenger prompt']"
        ]
        for button in label_buttons:
            try:
                close_button = self.driver.find_element(By.CSS_SELECTOR, button)
                close_button.click()
                print("Modal window closed.")
            except NoSuchElementException:
                print("Close button not found.")
            except ElementClickInterceptedException:
                print("Close button is not clickable.")
        time.sleep(3)
