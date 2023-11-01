
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage


class LoginPage(BasePage):
    INPUT_EMAIL = (By.NAME, "login[username]")
    INPUT_PASSWORD = (By.NAME, "login[password]")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "fieldset>div>div>button>span")
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'div[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
    ERROR_MESSAGE_SHORT = (By.XPATH, '//div[contains(text(),"This is a required field.")]')
    DROPDOWN = (By.XPATH, '(//button[@data-action="customer-menu-toggle"])[1]')
    LOGOUT_BUTTON = (By.XPATH, '(// a[contains(text(), "Sign Out")])[1]')

    def navigate_to_login_page(self):
        self.browser.get(self.BASE_URL)

    def set_email(self):
        email = self.find(self.INPUT_EMAIL)
        email.send_keys("annapecorino4055@gmail.com")

    def set_password(self):
        password = self.find(self.INPUT_PASSWORD)
        password.send_keys("Hailascoala123!")

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
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )

        expected_error = error_message
        actual_error = self.find(self.ERROR_MESSAGE).text
        print(f"Expected_error: {expected_error}")
        print(f"Actual_error: {actual_error}")
        assert expected_error == actual_error

    def check_error_msg_short(self, error_message_short):
        expected_error = error_message_short
        actual_error = self.find(self.ERROR_MESSAGE_SHORT).text
        print(f"Expected_error: {expected_error}")
        print(f"Actual_error: {actual_error}")
        assert expected_error == actual_error

    def button_logout(self):
        self.find(self.DROPDOWN).click()
        self.find(self.LOGOUT_BUTTON).click()
