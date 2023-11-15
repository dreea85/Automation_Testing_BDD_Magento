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


# @then('the short message "{error_message_short}" is displayed below the password field')
# def step_impl(context, error_message_short):
#     context.login_obj.check_error_msg_short(error_message_short)

@then('the message "{invalid_email_message}" is displayed below the email field')
def step_impl(context, invalid_email_message):
    context.login_obj.check_invalid_email_message(invalid_email_message)


@then('the message "{error_message}" is displayed')
def step_impl(context, error_message):
    context.login_obj.check_error_msg(error_message)

@then('the short message "{error_message_short}" is displayed')
def step_impl(context, error_message_short):
    context.login_obj.check_error_msg_short(error_message_short)

@then("the user logs out")
def step_impl(context):
    context.login_obj.button_logout()

