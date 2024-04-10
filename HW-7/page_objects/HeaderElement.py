import BaseApp
from locators import Navigation


class HeaderElement(BaseApp):

    currency_locators = {
        "EUR": Navigation.LOCATOR_CURRENCY_EUR_BUTTON,
        "GBR": Navigation.LOCATOR_CURRENCY_GBP_BUTTON,
        "USD": Navigation.LOCATOR_CURRENCY_USD_BUTTON
    }

    def change_currency(self, currency):
        self.find_element(self.driver, Navigation.LOCATOR_CURRENCY_BUTTON).click()
        cur = self.find_element(self.driver, self.currency_locators[currency])
        cur_char = (cur.text)[0]
        cur.click()
        return cur_char
