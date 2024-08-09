Feature: Add vaccine to site


@addvaccine
  Scenario: Add vaccines page should launch
    Given I am logged into the RAVS app
    When I am on the vaccine settings page
    And I click add vaccines button
    Then the add vaccines page should be launched

@addvaccine
  Scenario Outline: Vaccine already added to site warning should appear
    Given I am on the RAVS home page
    When I am on the vaccine settings page
    And I click add vaccines button
    And I select <site>, <vaccine>, <vaccineType>
    Then the vaccine is already added to site warning should appear

Examples:
|site          | vaccine  | vaccineType|
|NEELIMA HOUSE | COVID-19 | Comirnaty Original/Omicron BA.4-5 |
|NEELIMA HOUSE | Flu      | Fluenz Tetra - LAIV               |


