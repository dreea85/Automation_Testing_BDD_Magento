Feature: Test the functionality of the login page
  Background:
    Given I am on the testing board login page
  Scenario: Login Successful when using correct email and correct password
    When I insert correct email and password
    And I click on the login button
    Then I can login into the application and see the user's account page
    And the user logs out

  Scenario Outline: Check that we can not login into the application when providing incorrect credentials
    When I insert email "<email>" and password "<password>"
    And I click on the login button
    Then the message "<error_message>" is displayed
  Examples:
    | email                      | password        | error_message                                                                                              |
    | anapecorinox@gmail.com     | Hailascoala123! | The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.|
    | annapecorino4055@gmail.com | 123!            | The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.|
    | anapecorinox@gmail.com     | 123!            | The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.|

  Scenario Outline: Check that we can not login into the application when providing incorrect credentials
    When I insert email "<email>" and password "<password>"
    And I click on the login button
    Then a short message "<error_message_short>" is displayed
  Examples:
    | email                      | password        | error_message_short       |
    | annapecorino4055@gmail.com | None            | This is a required field. |
    | anapecorinox@gmail.com     | None            | This is a required field. |
    | None                       | None            | This is a required field. |
    | None                       | Hailascoala123! | This is a required field. |
    | None                       | 123!            | This is a required field. |
    | None                       | None            | This is a required field. |
