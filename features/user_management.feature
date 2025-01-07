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

@usermanagement
Scenario: Deactivated users page should be displayed
  Given I am logged into the RAVS app
  When I click the manage users navigation link
  When I click the deactivated users link
  Then the deactivated users page should be displayed

@usermanagement
Scenario: Reactivate user page should be displayed
  Given I am logged into the RAVS app
  When I click the manage users navigation link
  When I click the deactivated users link
  When I click the reactivate user link
  Then the reactivate user page should be displayed

@usermanagement
Scenario: Change user details page should launch
  Given I am logged into the RAVS app
  When I click the manage users navigation link
  When I click the change user details link
  Then the change user details page should be displayed

@usermanagement
Scenario: Change user details
  Given I am logged into the RAVS app
  When I click the manage users navigation link
  When I click the change user details link
  When I change the user's <detail>
  When I click continue to save the changed detail
  Then the user's new details should be visible in the user management table

Examples:
| detail              |
| clinician           |
| recorder            |
| administrator       |
| lead administrator  |


