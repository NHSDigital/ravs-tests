Feature: Add vaccine to site

  @addvaccine
  Scenario: Add vaccines page should launch
    Given I am logged into the RAVS app
    When I am on the vaccines page
    And I click add vaccine button
    Then the choose site page should be launched

  @addvaccine
  Scenario Outline: Vaccine already added to site warning should appear
    Given I am on the RAVS home page
    When I am on the vaccines page
    And I click add vaccine button
    And I select <site>, <vaccine>, <vaccineType>
    Then the vaccine is already added to site warning should appear

    Examples:
      | site         | vaccine  | vaccineType                 |
      | ALBERT HOUSE | COVID-19 | Spikevax JN.1               |
      | ALBERT HOUSE | Flu      | Flucelvax Tetra - QIVc      |
