Feature: Test the functionality of the login page

  #Scenario 1: correct email + correct password
  #Scenario 2: incorrect email + correct password
  #Scenario 3: correct email + incorrect password
  #Scenario 4: correct email + password None
  #Scenario 5: email None + correct password
  #Scenario 6: incorrect email + password None
  #Scenario 7: email None + incorrect password
  #Scenario 8: email None + password None
  #Scenario 9: incorrect email + incorrect password

  Scenario: Login Successful when using correct email and correct password
    Given I am on the testing board login page
    When I insert correct email and password
    And I click on the login button
    Then I can login into the application and see user's account page

"""
  Scenario: Login failed when using incorrect email and correct password
    Given I am on the testing board login page
    When I insert incorrect email and correct password
    And I click on the login button
    Then I am unable to login and the error message contains

  Scenario: Login failed when using correct email and incorrect password
    Given I am on the testing board login page
    When I insert correct email and incorrect password
    And I click on the login button
    Then I am unable to login and the error message contains

  Scenario: Login failed when using correct email and password None
    Given I am on the testing board login page
    When I insert correct email and password None
    And I click on the login button
    Then I am unable to login and the error message contains

  Scenario: Login failed when using email None and correct password
    Given I am on the testing board login page
    When I insert email None and correct password
    And I click on the login button
    Then I am unable to login and the error message contains

  Scenario: Login failed when using incorrect email and password None
    Given I am on the testing board login page
    When I insert incorrect email and password None
    And I click on the login button
    Then I am unable to login and the error message contains

  Scenario: Login failed when using email None and incorrect password
    Given I am on the testing board login page
    When I insert email None and incorrect password
    And I click on the login button
    Then I am unable to login and the error message contains

  Scenario: Login failed when using email None and password None
    Given I am on the testing board login page
    When I insert email None and password None
    And I click on the login button
    Then I am unable to login and the error message contains

  Scenario: Login failed when using incorrect email and incorrect password
    Given I am on the testing board login page
    When I insert incorrect email and incorrect password
    And I click on the login button
    Then I am unable to login and the error message contains
"""