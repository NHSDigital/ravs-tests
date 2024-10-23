Feature: Add vaccine to site

  @addvaccine
  Scenario: Add vaccines page should launch
    Given I am logged into the RAVS app
    When I am on the vaccines page
    And I click add vaccine button
    Then the choose site page should be launched
