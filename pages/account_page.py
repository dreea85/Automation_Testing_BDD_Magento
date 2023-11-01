
from base_page import BasePage

class AccountPage(BasePage):

    def check_current_url(self):
        expected_url = "https://magento.softwaretestingboard.com/customer/account/"
        actual_url = self.browser.current_url
        assert expected_url == actual_url

