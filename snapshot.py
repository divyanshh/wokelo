import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def block_modals(driver):
    script = """
    var modalSelectors = [
        'div[role=dialog]',
        'div[class*=modal]',
        'div[id*=modal]',
        'div[class*=popup]',
        'div[id*=popup]',
        'div[class*=overlay]',
        'div[id*=overlay]',
        'div[class*=consent]',
        'div[id*=consent]',
        'div[class*="cc-banner"]',
        'div[id*=cc-banner]',
        'div[class*=ccc-content]',
        'div[id*=ccc-content]',
        'div[class*=cookies]',
        'div[id*=cookies]',
    ];
    modalSelectors.forEach(function(selector) {
        var modals = document.querySelectorAll(selector);
        modals.forEach(function(modal) {
            modal.style.display = 'none';
        });
    });
    """
    driver.execute_script(script)


def load_and_take_screenshot(url, output_file='screenshot.png'):
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

    try:
        driver.get(url)
        time.sleep(5)
        block_modals(driver)
        driver.save_screenshot("images/" + output_file)
        print(f"Screenshot saved as {output_file}")
    finally:
        driver.quit()


def main():
    os.makedirs("images", exist_ok=True)
    websites = {
        "https://momi.baby/": "momibaby.png",
        "https://birdeye.com/": "birdeye.png",
        "https://www.alpha-sense.com/": "alphasense.png",
        "https://stackoverflow.com/": "stackoverflow.png",
        "https://www.instagram.com/": "instagram.png",
        "https://masterchow.in/": "masterchow.png",
        "https://www.springeropen.com/": "springeropen.png",
        "https://ico.org.uk/": "ico.png",
        "https://www.iwm.org.uk/": "iwm.png",
        "https://www.geeksforgeeks.org/": "geeksforgeeks.png",
        "https://bmigroupinternational.com/": "bmigroupinternational.png",
        "https://european-union.europa.eu/": "european-union.png",
    }

    for url, file_path in websites.items():
        load_and_take_screenshot(url, file_path)
        print(f"Taken screenshot of {url}")


if __name__ == '__main__':
    main()
