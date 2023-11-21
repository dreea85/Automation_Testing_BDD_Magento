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


  Scenario Outline: Attempting to create an account with an existing email
    When I click on "Create an Account" button
    Then I am redirected to the registration page
    When I fill in the registration form with an email that is already in use: "<first_name>", "<last_name>", "<email>", "<password>", "<confirm_pass>"
    And I submit the form
    Then I should see an error message "<message>" indicating the email is already registered

  Examples:
    | first_name | last_name | email                      | password        | confirm_pass    | message                                                                                                                                                      |
    | Anna       | Pecorino  | annapecorino4055@gmail.com | Hailascoala123! | Hailascoala123! | There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account. |


  Scenario: Attempting to create an account with invalid data
    When I click on "Create an Account" button
    Then I am redirected to the registration page
    When I attempt to create accounts with the following data
      | first_name | last_name | email                 | password      | confirm_pass  |
      | Dave       | Stan      | davestan123@gmail.com | 1q2w3e!       | 1q2w3e!       |
      | Dave       | Stan      | davestan123@gmail.com | Vineiarna123! | Vineiarna123  |
      | Dave       | Stan      | davestan123@gmail     | Vineiarna123! | Vineiarna123! |
      | Dave       | Stan      | davestan123@gmail     | Vineiarna123! | Vineiarna123  |
      | Dave       | Stan      | davestan123@gmail     | 1q2w3e!       | 1q2w3e!       |
      | Dave       | Stan      | None                  | 1q2w3e!       | 1q2w3e!       |
      | Dave       | Stan      | davestan123@gmail     | None          | 1q2w3e!       |
      | Dave       | Stan      | davestan123@gmail     | 1q2w3e!       | None          |

    And I submit the form
    Then I should see appropriate error messages