from base_page import BasePage

class ForgotPasswordPage(BasePage):

    def check_forgot_password_url(self):
        expected_url = "https://magento.softwaretestingboard.com/customer/account/forgotpassword/"
        actual_url = self.browser.current_url
        assert expected_url == actual_url
