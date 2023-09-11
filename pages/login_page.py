from selenium.webdriver.common.by import  By

from base_page import BasePage

class LoginPage(BasePage):
    INPUT_EMAIL = (By.NAME, "login[username]")
    INPUT_PASSWORD = (By.NAME, "login[password]")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "fieldset>div>div>button>span")
    # ERROR_MSG = (By.)

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