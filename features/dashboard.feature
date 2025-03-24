Feature: Dashboard

  Scenario Outline: Dashboard for an organization with no location sites
    Given I am logged into the RAVS app with the <username>
    Then the <site> name should be visible on the dashboard page
    And the today vaccinations count should be 0
    And the past 7 days vaccinations count should be 0
    And the past month's vaccinations count should be 0
    And the create a report link should be visible

    Examples:
      | username                                      | site                        |
      | neelima.guntupalli1+no_location_sites@nhs.net | Tquila Automation Ltd. (uk) |
