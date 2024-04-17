import time

from src.website_handlers.abc_webite_handler import WebsiteHandler


class DefaultWebsiteHandler(WebsiteHandler):
    def load_website(self, url):
        self.driver.get(url)
        time.sleep(3)

    def take_screenshot(self, output_file):
        self.driver.save_screenshot("images/" + output_file)
        print(f"Screenshot saved as {output_file}")

    def block_modals(self):
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
        self.driver.execute_script(script)
