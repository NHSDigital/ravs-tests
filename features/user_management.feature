Feature: User Management

@usermanagement
Scenario: Manage users page is displayed
  Given I am logged into the RAVS app
  When I click the manage users navigation link
  Then the manage users page should be displayed

@usermanagement
Scenario: Add User page should be displayed
  Given I am logged into the RAVS app
  When I click the manage users navigation link
  When I click the add user button
  Then the add user page should be displayed

@usermanagement
Scenario: Add user error messages should be displayed
  Given I am logged into the RAVS app
  When I click the manage users navigation link
  When I click the add user button
  And I click the continue to add user details button
  Then the error messages and links should be displayed for the missing fields

