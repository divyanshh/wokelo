import json
import os
import time

from src.driver import Driver


def take_screenshot(driver, url, file_path):
    driver.get(url)
    time.sleep(3)
    driver.save_screenshot("../images/" + file_path)
    print(f"Screenshot saved as {file_path}")
    print(f"Taken screenshot of {url}")


def main():
    os.makedirs("../images", exist_ok=True)
    with open("websites.json", "r") as file:
        websites = json.load(file)

    driver = Driver.setup_driver()

    for url, file_path in websites.items():
        driver.get(url)
        time.sleep(3)
        driver.save_screenshot("../images/" + file_path)
        print(f"Screenshot saved as {file_path}")
        print(f"Taken screenshot of {url}")


if __name__ == '__main__':
    main()
