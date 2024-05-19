# Created by macbookpro at 16/5/24
Feature: Login Test of CareApps
  # Enter feature description here
  In this feature, different positive and negative test cases will be designed as such most of the test cases
  can be covered

  Scenario: User can login with valid email and valid password
    Given User can enter to the https://staging.careapps.co.uk/auth/login
    When User will input valid email
    And User will input valid password
    And User will click remember me toggle button
    And User will click login button
    Then User will verify Login successful if they saw CareApp Logo on the up right corner

  Scenario: User can login with invalid email and valid password
    Given User can enter to the https://staging.careapps.co.uk/auth/login
    When User will input invalid email
    And User will input valid password
    And User will click remember me toggle button
    And User will click login button
    Then User will see No User Found pop up modal

  Scenario: User can login with valid email and invalid password
    Given User can enter to the https://staging.careapps.co.uk/auth/login
    When User will input valid email
    And User will input invalid password
    And User will click remember me toggle button
    And User will click login button
    Then User will see password is invalid

  Scenario: User can login with invalid email and invalid password
    Given User can enter to the https://staging.careapps.co.uk/auth/login
    When User will input invalid email
    And User will input invalid password
    And User will click remember me toggle button
    And User will click login button
    Then User will see No User Found pop up modal

  Scenario: User can login with valid email and valid password with unchecked remember me button
    Given User can enter to the https://staging.careapps.co.uk/auth/login
    When User will input valid email
    And User will input valid password
    And User will click login button
    Then User will verify Login successful if they saw CareApp Logo on the up right corner


