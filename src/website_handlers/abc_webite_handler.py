from abc import ABC, abstractmethod


class WebsiteHandler(ABC):
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def load_website(self, url):
        pass

    @abstractmethod
    def block_modals(self):
        pass

    def take_screenshot(self, output_file):
        self.driver.save_screenshot("images/" + output_file)
        print(f"Screenshot saved as {output_file}")
