Feature: Dashboard

  Scenario Outline: Dashboard for an organization with no location sites
    Given I am logged into the RAVS app with the username <username>
    Then the <site> name should be visible on the dashboard page
    And the today vaccinations count should be 0
    And the past 7 days vaccinations count should be 0
    And the past month's vaccinations count should be 0
    And the add vaccines link should be visible
    And the add users link should be visible
    And the find a patient link should be visible
    And the create a report link should not be visible

    Examples:
      | username                                      | site                        |
      | neelima.guntupalli1+no_location_sites@nhs.net | Tquila Automation Ltd. (Uk) |

  Scenario Outline: Create a report link should be visible for lead administrators and administrators
    Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>
    Then the add vaccines link should not be visible
    And the add users link should not be visible
    And the find a patient link should not be visible
    And the create a report link should be visible

    Examples:
      | care_model          | user_role             | site                          |
      | Trust site          | lead administrator    | Weaverham Surgery             |
      | Branch surgery      | administrator         | Aire Valley Surgery (Rawdon)  |

  Scenario Outline: Create a report link should not be visible for recorders
    Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>
    Then the add vaccines link should not be visible
    And the add users link should not be visible
    And the find a patient link should not be visible
    And the create a report link should not be visible

    Examples:
      | care_model          | user_role        | site                                                          |
      | Community pharmacy  | recorder         | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service  |

