from BaseApp import BasePage


class ProductPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = self.base_url + "/desktops/mac/imac"

    def go_to_product_page(self):
        return self.driver.get(self.url)
