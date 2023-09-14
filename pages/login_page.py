from selenium.webdriver.common.by import By

from base_page import BasePage

class LoginPage(BasePage):
    INPUT_EMAIL = (By.NAME, "login[username]")
    INPUT_PASSWORD = (By.NAME, "login[password]")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "fieldset>div>div>button>span")
    ERROR_MESSAGE = (By.XPATH, '//div[contains(text(),"The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.")]')
    SHORT_ERROR_MSG_EMAIL = (By.XPATH, '//div[contains(text(),"This is a required field.")]')
    SHORT_ERROR_MSG_PASS = (By.XPATH, '//div[contains(text(),"This is a required field.")]')
    DROPDOWN = (By.XPATH, '(//button[@data-action="customer-menu-toggle"])[1]')
    LOGOUT_BUTTON = (By.XPATH, '(// a[contains(text(), "Sign Out")])[1]')

    def navigate_to_login_page(self):
        self.browser.get(self.BASE_URL)


    def set_email(self):
        email = self.find(self.INPUT_EMAIL)
        email.send_keys("annapecorino4055@gmail.com")

    # def set_wrong_email(self):
    #     email = self.find(self.INPUT_EMAIL)
    #     email.send_keys("anapecorinox@gmail.com")

    def set_password(self):
        password = self.find(self.INPUT_PASSWORD)
        password.send_keys("Hailascoala123!")

    def set_wrong_password(self):
        password = self.find(self.INPUT_PASSWORD)
        password.send_keys("123!")

    def click_login_button(self):
        self.find(self.BUTTON_LOGIN).click()


    def insert_email(self, email):
        if email and email.lower() != "none":
            email_element = self.find(self.INPUT_EMAIL)
            email_element.clear()  # Clear the input field
            email_element.send_keys(email)


    def insert_password(self, password):
        if password and password.lower() != "none":
            password_element = self.find(self.INPUT_PASSWORD)
            password_element.clear()  # Clear the input field
            password_element.send_keys(password)


    def check_error_msg(self, error_message):
        expected_error = error_message
        actual_error = self.find(self.ERROR_MESSAGE).text
        print(f"Expected_error: {expected_error}")
        print(f"Actual_error: {actual_error}")
        assert expected_error == actual_error

    def check_short_error_msg_email(self, short_error_message_email):
        expected_error = short_error_message_email
        actual_error = self.find(self.SHORT_ERROR_MSG_EMAIL).text
        print(f"Expected_error: {expected_error}")
        print(f"Actual_error: {actual_error}")
        assert expected_error == actual_error

    def check_short_error_msg_pass(self, short_error_message_pass):
        expected_error = short_error_message_pass
        actual_error = self.find(self.SHORT_ERROR_MSG_PASS).text
        print(f"Expected_error: {expected_error}")
        print(f"Actual_error: {actual_error}")
        assert expected_error == actual_error

    def button_logout(self):
        self.find(self.DROPDOWN).click()
        self.find(self.LOGOUT_BUTTON).click()
