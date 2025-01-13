Feature: Add vaccine to site

  @addvaccine
  Scenario: Add vaccines page should launch
    Given I am logged into the RAVS app
    When I am on the vaccines page
    And I click add vaccine button
    Then the choose site page should be launched

  @addvaccine
  Scenario: Add vaccines navigation link should not be visible when logged in as recorder
    Given I am logged into the RAVS app as a recorder
    Then vaccines navigation link should not be visible

  @addvaccine
  Scenario: Vaccines navigation link should be visible when logged in as an administrator
    Given I am logged into the RAVS app as an administrator
    Then vaccines navigation link should be visible

  @addvaccine
  Scenario: Add vaccines page should be visible when logged in as an administrator
    Given I am logged into the RAVS app as an administrator
    When I click the vaccines navigation link
    Then the vaccines page should be visible
