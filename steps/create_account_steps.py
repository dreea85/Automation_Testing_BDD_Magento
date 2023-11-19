from behave import *


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