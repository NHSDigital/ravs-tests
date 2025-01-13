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
  And I click the add user button
  And I click the continue to add user details button
  Then the error messages and links should be displayed for the missing fields

@usermanagement
Scenario: Deactivated users page should be displayed
  Given I am logged into the RAVS app
  When I click the manage users navigation link
  And I click the deactivated users link
  Then the deactivated users page should be displayed

@usermanagement
Scenario: Reactivate user page should be displayed
  Given I am logged into the RAVS app
  When I click the manage users navigation link
  And I click the deactivated users link
  And I click the reactivate user link
  Then the reactivate user page should be displayed

@usermanagement
Scenario: Change user details page should launch
  Given I am logged into the RAVS app
  When I click the manage users navigation link
  And I click the change user details link
  Then the change user details page should be displayed

@usermanagement
Scenario: Change user details
  Given I am logged into the RAVS app
  When I click the manage users navigation link
  And I click the change user details link
  And I change the user's <detail>
  And I click continue to save the changed detail
  Then the user's new details should be visible in the user management table

Examples:
| detail              |
| clinician           |
| recorder            |
| administrator       |
| lead administrator  |

@usermanagement
Scenario: Add user details - Check and confirm page should be visible
  Given I am logged into the RAVS app
  When I click the manage users navigation link
  And I click the add user button
  And I enter the <first_name>, <last_name>, <nhs_email_address>
  And I select <clinician_status>
  And I select <permission_level>
  And I click the continue to add user details button
  Then the check and confirm user screen should be visible

Examples:
| first_name | last_name           | nhs_email_address                                    | clinician_status | permission_level |
| Automated  | administrator       | neelima.guntupalli1+administrator_automated@nhs.net  | yes              | administrator    |
| Automated  | tester              | automated.tester@nhs.net                             | yes              | recorder         |
| Automated  | lead administrator  | automated.tester@nhs.net                             | no               | lead administrator         |


@usermanagement
Scenario: User management should not be visible if logged in as recorder
  Given I am logged into the RAVS app as a recorder
  Then user management navigation link should not be visible

@usermanagement
Scenario: User management should not be visible if logged in as administrator
  Given I am logged into the RAVS app as an administrator
  Then user management navigation link should not be visible




