import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class Driver:
    @staticmethod
    def setup_driver():
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        prefs = {
            "excludeSwitches": ["disable-popup-blocking"],
            "profile.default_content_setting_values.cookies": 2,
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_values.popups": 2,
        }
        chrome_options.add_experimental_option("prefs", prefs)
        s = Service(os.getenv("DRIVER_PATH"))
        driver = webdriver.Chrome(service=s, options=chrome_options)
        return driver
