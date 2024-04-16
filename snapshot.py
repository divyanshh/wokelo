from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time


def close_modal_by_aria_label(driver):
    label_buttons = [
        "button[aria-label='Close dialog 1']",
        "button[aria-label='Dismiss campaign']",
        "button[aria-label='Close messenger prompt']"
    ]
    for button in label_buttons:
        try:
            close_button = driver.find_element(By.CSS_SELECTOR, button)
            close_button.click()
            print("Modal window closed.")
        except NoSuchElementException:
            print("Close button not found.")
        except ElementClickInterceptedException:
            print("Close button is not clickable.")


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
        'div[id*=consent]'
    ];
    modalSelectors.forEach(function(selector) {
        var modals = document.querySelectorAll(selector);
        modals.forEach(function(modal) {
            modal.style.display = 'none';
        });
    });
    """
    driver.execute_script(script)


def close_popups(driver):
    popup_selectors = [
        'div[class*="cookie"] button',
        'div[class*="popup"] button',
        'div[id*="advertisement"] button',
        'button[class*="close"]'
    ]
    for selector in popup_selectors:
        try:
            popup_element = driver.find_element(By.CSS_SELECTOR, selector)
            popup_element.click()
            print(f"Closed popup: {selector}")
            time.sleep(5)
        except (NoSuchElementException, ElementClickInterceptedException):
            continue


def take_screenshot(url, output_file='screenshot.png'):
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("disable-popup-blocking")
    chrome_options.add_argument("disable-notifications")
    prefs = {
        "excludeSwitches": ["disable-popup-blocking"],
        "profile.default_content_setting_values.cookies": 2,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.popups": 2,
    }
    chrome_options.add_experimental_option("prefs", prefs)
    s = Service('/Users/divyansh'
                'jain/Downloads/chromedriver-mac-arm64/chromedriver')
    driver = webdriver.Chrome(service=s, options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)
        # close_popups(driver)
        close_modal_by_aria_label(driver)
        block_modals(driver)
        time.sleep(3)
        driver.save_screenshot(output_file)
        time.sleep(5)
        print(f"Screenshot saved as {output_file}")
    finally:
        driver.quit()


if __name__ == '__main__':
    #take_screenshot('https://birdeye.com/', "birdeye.png")
    #take_screenshot("https://www.alpha-sense.com/", "alphasense.png")
    take_screenshot("https://momi.baby/", "momibaby.png")
    # take_screenshot("https://stackoverflow.com/", "so.png")
