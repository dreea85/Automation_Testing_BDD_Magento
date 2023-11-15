Feature: Test the functionality of the login page
  Background:
    Given I am on the testing board login page
  Scenario: Login Successful when using correct email and correct password
    When I insert correct email and password
    And I click on the login button
    Then I can login into the application and see the user's account page
    And the user logs out


  Scenario Outline: Verify login failure with detailed error message for incorrect credentials
    When I insert email "<email>" and password "<password>"
    And I click on the login button
    Then the message "<error_message>" is displayed
  Examples:
    | email                      | password        | error_message                                                                                              |
    | anapecorinox@gmail.com     | Hailascoala123! | The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.|
    | annapecorino4055@gmail.com | 123!            | The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.|
    | anapecorinox@gmail.com     | 123!            | The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.|

  Scenario Outline: Verify login failure with short error message for incorrect credentials
    When I insert email "<email>" and password "<password>"
    And I click on the login button
    Then the short message "<error_message_short>" is displayed
  Examples:
    | email                      | password        | error_message_short       |
    | annapecorino4055@gmail.com | None            | This is a required field. |
    | anapecorinox@gmail.com     | None            | This is a required field. |
    | None                       | None            | This is a required field. |
    | None                       | Hailascoala123! | This is a required field. |
    | None                       | 123!            | This is a required field. |
    | None                       | None            | This is a required field. |

  Scenario Outline: Login Unsuccessful with Invalid Email Format and Password correct/incorrect
    When I insert email "<email>" and password "<password>"
    And I click on the login button
    Then the message "<invalid_email_message>" is displayed below the email field

  Examples:
    |email             | password        | invalid_email_message                                        |
    |annapecorino4055  | Hailascoala123! | Please enter a valid email address (Ex: johndoe@domain.com). |
    |annapecorino4055  | 123!            | Please enter a valid email address (Ex: johndoe@domain.com). |


  Scenario Outline: Login Unsuccessful with Invalid Email Format and Password None
    When I insert email "<email>" and password "<password>"
    And I click on the login button
    Then the message "<invalid_email_message>" is displayed below the email field
    And the short message "<error_message_short>" is displayed

    Examples:
    |email             | password  | invalid_email_message                                        | error_message_short       |
    |annapecorino4055  | None      | Please enter a valid email address (Ex: johndoe@domain.com). | This is a required field. |