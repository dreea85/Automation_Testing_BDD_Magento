from behave import *

@given("I am on the testing board login page")
def step_impl(context):
    context.login_page.navigate_to_login_page()

@when("I insert correct email and password")
def step_impl(context):
    context.login_page.set_email()
    context.login_page.set_password()

@when("I click on the login button")
def step_impl(context):
    context.login_page.click_login_button()

@then("I can login into the application and see user's account page")
def step_impl(context):
    context.account_page.check_current_url()