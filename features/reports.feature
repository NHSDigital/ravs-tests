Feature: Reports

  @reports
  Scenario: "Reports" page is displayed
    Given I am logged into the RAVS app
    When I click the reports navigation link
    Then the reports page should be displayed

  Scenario: "Choose dates" page is displayed
    Given I am logged into the RAVS app
    When I click the reports navigation link
    And I click the create report button
    Then the choose dates page should be displayed

  Scenario Outline: Create report for an organization with no location sites
    Given I am logged into the RAVS app with the <username>
    When I click the reports navigation link
    Then the `No vaccination data to report on` message should be displayed
    And the Create report button should be disabled

  Examples:
  | username                                      |
  | neelima.guntupalli1+no_location_sites@nhs.net |
