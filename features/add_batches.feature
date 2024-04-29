Feature: Add Batches to vaccine


@addbatches
  Scenario: Add vaccine batches page should launch
    Given I am logged into the RAVS app
    When I am on the vaccine settings page 
    And I click add batches button
    Then the add vaccine batches page should be launched

@addbatches
  Scenario Outline: Add batch to vaccine
    Given I am on the RAVS home page
    When I am on the vaccine settings page
    And I click add batches button
    And I select <site>, <vaccine>, <vaccinetype> and enter <batchprefix>, <batchsuffix>
    And I enter <expirydate>
    And I click Add batch button
    And I click confirm choices button
    And I click confirm button
    Then the batch is already added to site warning should appear

Examples:
|site          | vaccine  | vaccinetype | batchprefix | batchsuffix | expirydate |
|NEELIMA HOUSE | COVID-19 | Comirnaty Original/Omicron BA.4-5 | SD7YY2 | 24 | 2/6/2024 |