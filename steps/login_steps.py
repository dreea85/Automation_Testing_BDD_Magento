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

#Below are the steps for testing the functionality of the "forgot password" page
@when('I click on "Forgot Your Password?"')
def step_impl(context):
    context.login_obj.click_forgot_password_button()

@when('I am redirected to another page')
def step_impl(context):
    expected_url = "https://magento.softwaretestingboard.com/customer/account/forgotpassword/"
    context.login_obj.wait_for_redirect(expected_url)

@when("I enter an email address")
def step_impl(context):
    context.login_obj.enter_email_for_reset("annapecorino4055@gmail.com")
@when("I submit the password reset request")
def step_impl(context):
    context.login_obj.click_reset_password_button()

@then("I should return to the login page")
def step_impl(context):
    context.login_obj.verify_return_to_login_page()

@then("see the message that the email to reset the password was sent")
def step_impl(context):
    context.login_obj.verify_reset_email_sent_message()

@then('I decide to cancel the request by going back to the previous page')
def step_impl(context):
    context.login_obj.go_back()

@when('I enter an invalid email format "{email}"')
def step_impl(context, email):
    context.login_obj.insert_email_on_reset_pass_page(email)

@then('I should see an error message "{message_invalid_email}"')
def step_impl(context, message_invalid_email):
    context.login_obj.verify_error_message_on_reset_pass_page(message_invalid_email)