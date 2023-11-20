import time

from selenium.common import TimeoutException

from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CreateAccountPage(BasePage):
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a.action.create.primary span")
    INPUT_FIRST_NAME = (By.CSS_SELECTOR, "input.input-text.required-entry[title='First Name']")
    INPUT_LAST_NAME = (By.CSS_SELECTOR, "input.input-text.required-entry[title='Last Name']")
    INPUT_EMAIL = (By.CSS_SELECTOR, "input[type='email'][title='Email'][autocomplete='email']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[type='password'][title='Password'][autocomplete='off']")
    INPUT_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input[type='password'][title='Confirm Password'][autocomplete='off']")
    CREATE_ACCOUNT_REGISTRATION_BUTTON = (By.CSS_SELECTOR, "div.primary button.submit span")
    REGISTRATION_MESSAGE = (By.CSS_SELECTOR, 'div[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
    DROPDOWN = (By.CSS_SELECTOR, 'div.panel.header button')
    LOGOUT_BUTTON = (By.XPATH, '(// a[contains(text(), "Sign Out")])[1]')
    MY_ACCOUNT_TITLE = (By.CSS_SELECTOR, 'div.page-title-wrapper span')
    PASSWORD_MESSAGES = (By.CSS_SELECTOR, 'div.mage-error#password-error')
    PASSWORD_CONFIRMATION_MESSAGES = (By.CSS_SELECTOR, 'div.mage-error#password-confirmation-error')
    EMAIL_MESSAGES = (By.CSS_SELECTOR, 'div.mage-error#email_address-error')


    def check_current_url(self):
        expected_url = "https://magento.softwaretestingboard.com/customer/account/create/"
        actual_url = self.browser.current_url
        assert expected_url == actual_url


    def navigate_to_login_page(self):
        self.browser.get(self.BASE_URL)

    def click_create_account_button(self):
        self.find(self.CREATE_ACCOUNT_BUTTON).click()

    def redirect_to_create_account_page(self, expected_url):
        try:
            WebDriverWait(self.browser, 10).until(lambda browser: browser.current_url == expected_url)

            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.page-title-wrapper h1.page-title span"))   #locator for the title of the page " create new customer account"
            )
        except TimeoutError:
            raise AssertionError(f"Browser did not navigate to the expected URL: {expected_url}")

    def add_firstname(self):
        email = self.find(self.INPUT_FIRST_NAME)
        email.send_keys("Dany")

    def add_lastname(self):
        password = self.find(self.INPUT_LAST_NAME)
        password.send_keys("Stan")

    def add_email(self):
        timestamp = int(time.time())
        unique_email = f"danystan1_{timestamp}@gmail.com"
        email = self.find(self.INPUT_EMAIL)
        email.send_keys(unique_email)

    def add_password(self):
        password = self.find(self.INPUT_PASSWORD)
        password.send_keys("Crocodile1234!")

    def add_confirm_password(self):
        password = self.find(self.INPUT_CONFIRM_PASSWORD)
        password.send_keys("Crocodile1234!")

    def click_create_account_registration_button(self):
        self.find(self.CREATE_ACCOUNT_REGISTRATION_BUTTON).click()

    def redirect_to_my_account_page(self, expected_url):
        try:
            WebDriverWait(self.browser, 10).until(lambda browser: browser.current_url == expected_url)

            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.page-title-wrapper span'))
            )
        except TimeoutError:
            raise AssertionError(f"Browser did not navigate to the expected URL: {expected_url}")

    def button_logout_from_my_account(self):
        self.find(self.DROPDOWN).click()
        self.find(self.LOGOUT_BUTTON).click()

    def clear_registration_form(self):
        # Clear the input fields
        self.find(self.INPUT_FIRST_NAME).clear()
        self.find(self.INPUT_LAST_NAME).clear()
        self.find(self.INPUT_EMAIL).clear()
        self.find(self.INPUT_PASSWORD).clear()
        self.find(self.INPUT_CONFIRM_PASSWORD).clear()

    def fill_registration_form(self, first_name, last_name, email, password, confirm_pass):
        self.find(self.INPUT_FIRST_NAME).send_keys(first_name)
        self.find(self.INPUT_LAST_NAME).send_keys(last_name)
        self.find(self.INPUT_EMAIL).send_keys(email)
        self.find(self.INPUT_PASSWORD).send_keys(password)
        self.find(self.INPUT_CONFIRM_PASSWORD).send_keys(confirm_pass)

    def verify_error_messages(self, expected_error_messages):
        for locator, expected_messages in expected_error_messages.items():
            # Ensure expected_messages is a list for uniform processing
            if not isinstance(expected_messages, list):
                expected_messages = [expected_messages]

            # Find the actual error message on the page
            try:
                WebDriverWait(self.browser, 15).until(
                    EC.visibility_of_element_located(locator)
                )
                actual_message = self.find(locator).text
            except TimeoutException:
                assert False, f"Error message with locator {locator} not found."

            # Check if any of the expected messages match the actual message
            if not any(expected_message in actual_message for expected_message in expected_messages):
                expected_msg_str = "', '".join(expected_messages)
                assert False, f"None of the expected messages '{expected_msg_str}' found. Actual message: '{actual_message}'"
