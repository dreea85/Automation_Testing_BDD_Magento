from behave import *

from pages.create_account_page import CreateAccountPage


@when('I click on "Create an Account" button')
def step_impl(context):
    context.create_account_obj.click_create_account_button()

@then('I am redirected to the registration page')
def step_impl(context):
    expected_url = "https://magento.softwaretestingboard.com/customer/account/create/"
    context.create_account_obj.redirect_to_create_account_page(expected_url)

@when('I fill in the registration form with valid data')
def step_impl(context):
    context.create_account_obj.add_firstname()
    context.create_account_obj.add_lastname()
    context.create_account_obj.add_email()
    context.create_account_obj.add_password()
    context.create_account_obj.add_confirm_password()

@when('I submit the form')
def step_impl(context):
    context.create_account_obj.click_create_account_registration_button()

@then('I should be redirected to the account confirmation page')
def step_impl(context):
    expected_url = "https://magento.softwaretestingboard.com/customer/account/"
    context.create_account_obj.redirect_to_my_account_page(expected_url)

@then("the user successfully logs out")
def step_impl(context):
    context.create_account_obj.button_logout_from_my_account()


@when('I attempt to create accounts with the following data')
def step_impl(context):
    for row in context.table:
        context.create_account_obj.clear_registration_form()
        first_name = row['first_name']
        last_name = row['last_name']
        email = row['email']
        password = row['password']
        confirm_pass = row['confirm_pass']
        context.create_account_obj.fill_registration_form(first_name, last_name, email, password, confirm_pass)
        context.create_account_obj.click_create_account_registration_button()

        # Reset the form for the next iteration, if necessary

@then('I should see appropriate error messages')
def step_impl(context):
    expected_errors = {
        CreateAccountPage.PASSWORD_MESSAGES: [
            "Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing spaces will be ignored.",
            "This is a required field."
            ],
        CreateAccountPage.PASSWORD_CONFIRMATION_MESSAGES: [
            "Please enter the same value again.",
            "This is a required field."
            ],
        CreateAccountPage.EMAIL_MESSAGES: [
            "Please enter a valid email address (Ex: johndoe@domain.com).",
            "This is a required field."
            ]
    }
    context.create_account_obj.verify_error_messages(expected_errors)