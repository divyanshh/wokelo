import os
import time

from src.driver import Driver
import concurrent.futures


def take_screenshot(driver, url, file_path):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)
    time.sleep(3)
    driver.save_screenshot("../images/" + file_path)
    print(f"Screenshot saved as {file_path}")
    print(f"Taken screenshot of {url}")
    driver.close()


def main():
    os.makedirs("../images", exist_ok=True)
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
        "https://www.cookieyes.com/blog/how-to-block-cookies/": "cookieyes.png",
        "https://www.cookieserve.com/": "cookieserve.png",
        "https://www.makemytrip.com/": "makemytrip.png",
        "https://www.kaggle.com/datasets/lava18/google-play-store-apps": "kaggle.png",
        "https://www.westminster-abbey.org/about-the-abbey/privacy-policy/cookies": "westminster.png",
        "https://www.templafy.com/privacy/cookies-list/": "templafy.png",
        "https://www.sdcard.org/list-of-cookies-on-this-site/": "sdcard.png",
        "https://www.deif.com/cookies/cookielist/": "deif.png",
        "https://www.allstemconnections.com/cookie-list.aspx": "allstemconnections.png",
        "https://termly.io/resources/articles/does-my-website-use-cookies/": "termly.png",
        "https://www.bucherer.com": "bucherer.png",
        "https://www.gsmatraining.com/cookie-list/": "gsmatraining.png",
        "https://pimeyes.com/en": "pimeyes.png",
        "https://www.qr-code-generator.com/": "qr-code-generator.png",
        "https://clym.io/": "clym.png"
    }
    driver = Driver.setup_driver()

    max_threads = 10
    urls_to_process = list(websites.items())

    with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
        futures = {executor.submit(take_screenshot, driver, url, file_path): (url, file_path) for url, file_path in
                   urls_to_process}
        for future in concurrent.futures.as_completed(futures):
            url, file_path = futures[future]
            try:
                future.result()
            except Exception as e:
                print(f"An error occurred while processing {url}: {e}")

    # Quit the WebDriver instance after all threads finish
    driver.quit()


if __name__ == '__main__':
    main()
