import json
import os
import threading
import time

from src.constants import IMAGES_BASE_DIR, WEBSITES_FILE, PROFILES_FILE, SLEEP_TIME
from src.driver import Driver


def save_screenshot(driver, url, file_name):
    try:
        driver.get(url)
        time.sleep(SLEEP_TIME)
        driver.save_screenshot(IMAGES_BASE_DIR + file_name)
        print(f"Screenshot saved as {file_name} for url {url}")
    except Exception as ex:
        print(f"Exception occurred for url {url} : {ex}")


def screenshot_thread(profile, websites, user_data_dir):
    driver = Driver.setup_driver(profile, user_data_dir)
    for url, file_path in websites.items():
        save_screenshot(driver, url, file_path)
    driver.quit()


def load_websites_and_profiles():
    os.makedirs(IMAGES_BASE_DIR, exist_ok=True)
    with open(WEBSITES_FILE, "r") as file:
        websites = json.load(file)

    with open(PROFILES_FILE, "r") as profiles_file:
        profiles = json.load(profiles_file)
    return websites, profiles


def main():
    websites, profiles = load_websites_and_profiles()

    num_profiles = len(profiles)
    num_websites = len(websites)

    websites_per_profile = num_websites // num_profiles
    remaining_websites = num_websites % num_profiles

    threads = []

    start_idx = 0
    for i, (profile, user_data_dir) in enumerate(profiles.items()):
        end_idx = (
            start_idx + websites_per_profile + (1 if i < remaining_websites else 0)
        )
        websites_for_profile = dict(list(websites.items())[start_idx:end_idx])
        print(websites_for_profile)
        thread = threading.Thread(
            target=screenshot_thread,
            args=(profile, websites_for_profile, user_data_dir),
        )
        threads.append(thread)
        start_idx = end_idx

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
