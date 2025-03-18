Feature: User Management


  Background:
  Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>

@usermanagement
Scenario: Add user error messages should be displayed
  When I click the manage users navigation link
  And I click the add user button
  And I click the continue to add user details button
  Then the error messages and links should be displayed for the missing fields

    Examples:
    | care_model |  user_role | site        |
    | Trust site |  lead administrator | Weaverham Surgery    |
    | Community pharmacy  |  lead administrator | Aspire Pharmacy  |
    | Branch surgery  |  lead administrator | Aire Valley Surgery (rawdon)  |

@usermanagement
Scenario: Deactivated users page should be displayed
  When I click the manage users navigation link
  And I click the deactivated users link
  Then the deactivated users page should be displayed

    Examples:
    | care_model |  user_role | site        |
    | Trust site |  lead administrator | Weaverham Surgery    |
    | Community pharmacy  |  lead administrator | Aspire Pharmacy  |
    | Branch surgery  |  lead administrator | Aire Valley Surgery (rawdon)  |

@usermanagement
Scenario: Reactivate user page should be displayed
  When I click the manage users navigation link
  And I click the deactivated users link
  And I click the reactivate user link
  Then the reactivate user page should be displayed

    Examples:
    | care_model |  user_role | site        |
    | Trust site |  lead administrator | Weaverham Surgery    |
    | Community pharmacy  |  lead administrator | Aspire Pharmacy  |
    | Branch surgery  |  lead administrator | Aire Valley Surgery (rawdon)  |

@usermanagement
Scenario: Change user details page should launch
  When I click the manage users navigation link
  And I click the change user details link
  Then the change user details page should be displayed

    Examples:
    | care_model |  user_role | site        |
    | Trust site |  lead administrator | Weaverham Surgery    |
    | Community pharmacy  |  lead administrator | Aspire Pharmacy  |
    | Branch surgery  |  lead administrator | Aire Valley Surgery (rawdon)  |

@usermanagement
Scenario: Change user details
  When I click the manage users navigation link
  And I click the change user details link
  And I change the user's <detail>
  And I click continue to save the changed detail
  Then the user's new details should be visible in the user management table

Examples:
| detail    | care_model     | user_role | site      |
| clinician | Trust site     | lead administrator | Weaverham Surgery  |
| recorder  | Community pharmacy | lead administrator  | Aspire Pharmacy    |
| administrator  | Branch surgery | lead administrator  | Aire Valley Surgery (rawdon)|
| lead administrator | Trust site     | lead administrator | Weaverham Surgery  |

@usermanagement
Scenario: Add user details - Check and confirm page should be visible
  When I click the manage users navigation link
  And I click the add user button
  And I enter the <first_name>, <last_name>, <nhs_email_address>
  And I select <clinician_status>
  And I select <permission_level>
  And I click the continue to add user details button
  Then the check and confirm user screen should be visible

Examples:
| first_name | last_name  | nhs_email_address  | clinician_status | permission_level    | site  | care_model    | user_role    |
| Automated  | administrator | neelima.guntupalli1+admin_automated@nhs.net | yes | administrator   | Weaverham Surgery   | Trust site    | lead administrator    |
| Automated  | administrator  | neelima.guntupalli1+admin_automated@nhs.test   | yes | administrator   | Aspire Pharmacy | Community pharmacy| lead administrator    |
| Automated  | tester   | automated.tester@nhs.net | yes | recorder   | Aire Valley Surgery | Branch surgery  | lead administrator |
| Automated  | lead administrator | automated.tester@nhs.net  | no  | lead administrator  | Weaverham Surgery   | Trust site    | lead administrator |
| Bethany    | lead administrator | bethany.north4+lead_administrator_automated@rmh.nhs.uk  | no  | lead administrator  | Leeds Pharmacy  | Community pharmacy| lead administrator|
| Bethany    | administrator | bethany.north4+administrator_automated@stockport.nhs.uk | no  | administrator   | Aspire Pharmacy | Community pharmacy| lead administrator    |
| Bethany    | recorder  | bethany.north4+recorder_automated@swast.nhs.uk | no  | recorder   | Aire Valley Surgery | Branch surgery    | lead administrator     |
| Bethany    | recorder  | bethany.north4+recorder_automated@nhs.scot     | no  | recorder   | Weaverham Surgery   | Trust site    | lead administrator     |
| Bethany    | recorder  | bethany.north4+recorder_automated@nhs.uk  | no  | recorder   | Leeds Pharmacy  | Community pharmacy| lead administrator     |


@usermanagement
Scenario: User management should not be visible if logged in as recorder
  Then user management navigation link should not be visible

    Examples:
    | care_model |  user_role | site        |
    | Trust site |  recorder | Weaverham Surgery    |
    | Community pharmacy  |  recorder | Aspire Pharmacy  |
    | Branch surgery  |  recorder | Aire Valley Surgery (rawdon)  |

@usermanagement
Scenario: User management should not be visible if logged in as administrator
  Then user management navigation link should not be visible

    Examples:
    | care_model |  user_role | site        |
    | Trust site |  administrator | Weaverham Surgery    |
    | Community pharmacy  |  administrator | Aspire Pharmacy  |
    | Branch surgery  |  administrator | Aire Valley Surgery (rawdon)  |

@usermanagement
Scenario: User management should be visible if logged in as lead administrator
  Then user management navigation link should be visible

@usermanagement
Scenario: Change details in the check and confirm user screen when adding a new user
  When I click the manage users navigation link
  And I click the add user button
  And I enter the <first_name>, <last_name>, <nhs_email_address>
  And I select <clinician_status>
  And I select <permission_level>
  And I click the continue to add user details button
  And I click the change user's <detail> detail link
  And I change the detail to the <new_detail>
  And continue to check and confirm screen
  Then the new detail should be visible on the check and confirm screen

Examples:
| first_name | last_name    | nhs_email_address    | clinician_status | permission_level | detail | new_detail | site   | care_model    | user_role  |
| Manual  | administrator   | automated.tester@nhs.net | Yes   | administrator    | name   | Automated recorder  | Aspire Pharmacy | Community pharmacy| lead administrator  |
| Automated  | tester    | automated.tester@nhs.net  | Yes | recorder    | clinician_status    | No    | Aire Valley Surgery | Branch surgery    | lead administrator  |
| Automated  | lead administrator | automated.tester@nhs.net  | No  | lead administrator   | permission_level    | Recorder   | Weaverham Surgery   | Trust site    | lead administrator |
| Automated  | administrator  | automated.tester@nhs.net  | No  | lead administrator   | email_address   | neelima.guntupalli1+automated_tester@nhs.net | Leeds Pharmacy  | Community pharmacy| lead administrator  |



