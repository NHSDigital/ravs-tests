Feature: Reports

  @reports
  Scenario: Create reports page should launch
    Given I am logged into the RAVS app
    When I click the reports navigation link
    Then the reports page should be displayed
