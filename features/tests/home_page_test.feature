# Created by macbookpro at 21/5/24
Feature: Home page verification
  In this feature, we will verify certain elements are present or not in the home page.

  Background: User can login with valid email and valid password
    Given User can enter to the https://staging.careapps.co.uk/auth/login
    When User will input valid email
    And User will input valid password
    And User will click remember me toggle button
    And User will click login button
    Then User will verify Login successful if they saw CareApp Logo on the up right corner

   Scenario: User will able to see the chart of Total job, Viewed Application, Unseen Application, Accepted Application,
     Submitted Application, Jobs, Completion Rate
    When User will verify Login successful if they saw CareApp Logo on the up right corner
     Then User will verify if total job cart present
     Then User will verify if viewed application cart present
     Then User will verify if unseen application cart present
     Then User will verify if total job application cart present
     Then User will verify if accepted application cart present
     Then User will verify if submitted application cart present
     Then User will verify if jobs cart present
     Then User will verify if completion ratio present
     When User will click job application button
     Then User will verify Candidate List text is present
     When User will click back button of browser
     When User will click view jobs button
     Then User will verify Job Board text is present