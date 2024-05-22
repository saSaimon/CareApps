# Created by macbookpro at 22/5/24
Feature: In this feature user will try to check if the forget password is working or not.
  User will try to reset password

  Scenario: Positive Forgot Password Test
    Given User can enter to the https://staging.careapps.co.uk/auth/login
    When User will click forgot password button
    And User will input asadiqulsaimon@gmail.com in forgot password page
    And User will click send now button
    Then User will verify the email is sent and a success text is shown

  Scenario: Negative Forgot Password Test
    Given User can enter to the https://staging.careapps.co.uk/auth/login
    When User will click forgot password button
    And User will input asadiqulsaimon@gmail in forgot password page
    Then User will see email is not valid validation message