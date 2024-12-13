Feature: User Management

@usermanagement
Scenario: Manage users page is displayed
  Given I am logged into the RAVS app
  When I click the manage users navigation link
  Then the manage users page should be displayed
