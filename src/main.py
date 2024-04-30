import json
import os
import time

from src.driver import Driver

IMAGES_BASE_DIR = "../images/"
WEBSITES_FILE = "../websites.json"


def save_screenshot(driver, url, file_name):
    try:
        driver.get(url)
        time.sleep(5)
        driver.save_screenshot(IMAGES_BASE_DIR + file_name)
        print(f"Screenshot saved as {file_name} for url {url}")
    except Exception as ex:
        print(f"Exception occurred for url {url} : {ex}")


def main():
    os.makedirs(IMAGES_BASE_DIR, exist_ok=True)
    with open(WEBSITES_FILE, "r") as file:
        websites = json.load(file)

    driver = Driver.setup_driver()

    for url, file_path in websites.items():
        save_screenshot(driver, url, file_path)

    driver.quit()


if __name__ == '__main__':
    main()
