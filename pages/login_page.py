
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
    DROPDOWN = (By.CSS_SELECTOR, 'div.panel.header button')
    LOGOUT_BUTTON = (By.XPATH, '(// a[contains(text(), "Sign Out")])[1]')
    INVALID_EMAIL_MSG = (By.CSS_SELECTOR, "div#email-error")
    FORGOTTEN_PASS = (By.CSS_SELECTOR, "div.secondary a.action.remind span")
    RESET_PASSWORD_BUTTON = (By.CSS_SELECTOR, "div.primary button.submit span")
    EMAIL_TO_RESET_PASS = (By.XPATH, "//input[@type='email'][@name='email'][@id='email_address']")
    RESET_MESSAGE = (By.CSS_SELECTOR, 'div[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
    PAGE_TITLE_FORGOT_PASS = (By.CSS_SELECTOR, "div.page-title-wrapper h1.page-title span")
    ERROR_MSG_ON_PASSWORD_RESET_PAGE = (By.CSS_SELECTOR, "input#email_address + div.mage-error")
    INPUT_EMAIL_ON_RESET_PASS_PAGE = (By.CSS_SELECTOR, "input#email_address")


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

    def check_invalid_email_message(self, invalid_email_message):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.INVALID_EMAIL_MSG)
        )
        expected_error = invalid_email_message
        actual_error = self.find(self.INVALID_EMAIL_MSG).text
        print(f"Expected_error: {expected_error}")
        print(f"Actual_error: {actual_error}")
        assert expected_error == actual_error

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

    def click_forgot_password_button(self):
        self.find(self.FORGOTTEN_PASS).click()

    def wait_for_redirect(self, expected_url):
        try:
            WebDriverWait(self.browser, 10).until(lambda browser: browser.current_url == expected_url)

            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.page-title-wrapper h1.page-title span"))
            )
        except TimeoutError:
            raise AssertionError(f"Browser did not navigate to the expected URL: {expected_url}")

    def enter_email_for_reset(self, email):
        self.find(self.EMAIL_TO_RESET_PASS).send_keys(email)

    def click_reset_password_button(self):
        self.find(self.RESET_PASSWORD_BUTTON).click()

    def verify_return_to_login_page(self):
        assert "login" in self.browser.current_url

        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((self.RESET_MESSAGE))
        )
        confirmation_message = self.find(self.RESET_MESSAGE).text
        assert "If there is an account associated with annapecorino4055@gmail.com you will receive an email with a link to reset your password." in confirmation_message

    def verify_reset_email_sent_message(self):
        message = self.find(self.RESET_MESSAGE).text
        assert "If there is an account associated with annapecorino4055@gmail.com you will receive an email with a link to reset your password." in message

    def insert_email_on_reset_pass_page(self, email):
        if email and email.lower() != "none":
            email_element = self.find(self.INPUT_EMAIL_ON_RESET_PASS_PAGE)
            email_element.clear()  # Clear the input field
            email_element.send_keys(email)


    def verify_error_message_on_reset_pass_page(self, expected_message):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.ERROR_MSG_ON_PASSWORD_RESET_PAGE)
        )
        actual_message = self.find(self.ERROR_MSG_ON_PASSWORD_RESET_PAGE).text
        assert expected_message in actual_message, f"Expected '{expected_message}', got '{actual_message}' instead."
