import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class Driver:
    @staticmethod
    def setup_driver(user_profile, user_data_dir):
        driver_path = os.getenv("DRIVER_PATH")
        brave_path = os.getenv("BRAVE_PATH")

        chrome_options = Options()
        chrome_options.binary_location = brave_path
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--user-data-dir={}".format(user_data_dir))
        chrome_options.add_argument("--profile-directory={}".format(user_profile))

        s = Service(driver_path)
        driver = webdriver.Chrome(service=s, options=chrome_options)
        return driver
