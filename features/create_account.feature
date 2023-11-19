Feature: Test the functionality of the create an account page
  Background:
    Given I am on the testing board login page
  Scenario: Successfully creating a new account
    When I click on "Create an Account" button
    Then I am redirected to the registration page
    When I fill in the registration form with valid data
    And I submit the form
    Then I should be redirected to the account confirmation page
    And the user successfully logs out

#
#  Scenario: Attempting to create an account with an existing email
#    When I click on "Create an Account" button
#    Then I am redirected to the registration page
#    When I fill in the registration form with an email that is already in use
#    And I submit the form
#    Then I should see an error message indicating the email is already registered
#
#  Scenario Outline: Attempting to create an account with invalid data
#    When I click on "Create an Account" button
#    Then I am redirected to the registration page
#    When I fill in the registration form with invalid data "<first_name>", "<last_name>", "<email>", "<password>", "<confirm_pass>"
#    And I submit the form
#    Then I should see error messages "<account_creation_error_messages>" indicating the invalid fields
#
#  Examples:
#    |first_name  |  last_name | email  |  password  | confirm_pass | account_creation_error_messages    |