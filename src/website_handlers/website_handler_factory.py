from src.website_handlers.default_website_handler import DefaultWebsiteHandler
from src.website_handlers.momi_baby_website_handler import MomiBabyWebsiteHandler


class WebsiteHandlerFactory:
    @staticmethod
    def get_website_handler(driver, url):
        if "momi.baby" in url:
            return MomiBabyWebsiteHandler(driver)
        else:
            return DefaultWebsiteHandler(driver)
