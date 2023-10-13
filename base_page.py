from browser import Browser

class BasePage(Browser):
    BASE_URL = "https://magento.softwaretestingboard.com/customer/account/login"

    def find(self, locator):
        return self.browser.find_element(*locator)

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def click(self, locator):
        self.find(locator).click()

    def get_text(self, locator):
        return self.find(locator).text
