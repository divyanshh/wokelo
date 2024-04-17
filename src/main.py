import os

from src.driver import Driver
from src.website_handlers.website_handler_factory import WebsiteHandlerFactory


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
    }
    driver = Driver.setup_driver()
    for url, file_path in websites.items():
        handler = WebsiteHandlerFactory.get_website_handler(driver, url)
        handler.load_website(url)
        handler.block_modals()
        handler.take_screenshot(file_path)
        print(f"Taken screenshot of {url}")


if __name__ == '__main__':
    main()
