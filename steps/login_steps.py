from behave import *

@given("I am on the testing board login page")
def step_impl(context):
    context.login_obj.navigate_to_login_page()

@when("I insert correct email and password")
def step_impl(context):
    context.login_obj.set_email()
    context.login_obj.set_password()

@when("I click on the login button")
def step_impl(context):
    context.login_obj.click_login_button()


@then("I can login into the application and see the user's account page")
def step_impl(context):
    context.account_page.check_current_url()

@when('I insert email "{email}" and password "{password}"')
def step_impl(context, email, password):
    context.login_obj.insert_email(email)
    context.login_obj.insert_password(password)


@then('the message "{error_message}" is displayed')
def step_impl(context, error_message):
    context.login_obj.check_error_msg(error_message)


@then('the email field message "{short_error_message_pass}" is displayed')
def step_impl(context, short_error_message_email):
    context.login_obj.check_short_error_msg_email(short_error_message_email)

@then('the password field message "{short_error_message_email}" is displayed')
def step_impl(context, short_error_message_pass):
    context.login_obj.check_short_error_msg_pass(short_error_message_pass)

@then("the user logs out")
def step_impl(context):
    context.login_obj.button_logout()
