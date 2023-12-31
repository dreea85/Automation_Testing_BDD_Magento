from browser import Browser
from pages.create_account_page import CreateAccountPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage


def before_all(context):
    context.browser = Browser()
    context.login_obj = LoginPage()
    context.account_page = AccountPage()
    context.forgot_password_page = ForgotPasswordPage()
    context.create_account_obj = CreateAccountPage()



# def after_all(context):
#     context.browser.close()

def after_scenario(context, scenario):
    if 'web' in context.tags:
        context.browser.quit()
