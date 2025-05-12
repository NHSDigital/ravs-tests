Feature: Login Feature

Scenario: Login button is visible
  Given I access the ravs web app
  Then the login button should be visible

Scenario: NHS sign in page should be visible
  Given I access the ravs web app
  When I click on the log in button
  Then the NHS sign in page should be visible

@login
Scenario Outline: Sign in should fail based on credentials provided
  Given I access the ravs web app
  When I click on the log in button
  And I provide the <emailAddress> and <password>
  And the NHS sign in button is clicked
  Then sign in should <status>

Examples:
|emailAddress                           | password        | status|
|neelima.guntupalli1@nhs.net-valid      | pass            | pass  |
# |None                                   | password        | fail  |
# # |neelima.guntupalli1@nhs.net            | password        | fail  |
# # |neelima.guntupalli1@nhs.net            | None            | fail  |
# |invalid_email_address                  | password        | fail  |
# # |neelima.guntupalli1@nhs.net            | short           | fail  |
# |long_email_address@nhs.net             | password        | fail  |
# # |neelima.guntupalli1@nhs.net            | long_password_that_exceeds_max_length           | fail  |
