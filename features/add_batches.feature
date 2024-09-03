Feature: Add Batches to vaccine

  @addbatches
  Scenario: Add vaccine batches page should launch
    Given I am logged into the RAVS app
    When I am on the vaccines page
    And I click on an available add batch link
    Then the add batch page should be launched

  @addbatches
  Scenario Outline: Add batch to vaccine
    Given I am on the RAVS home page
    When I am on the vaccines page
    And I view product for the <vaccine_type> on <site>
    And I enter <batch_number>
    Then the batch is already added to site warning should appear

    Examples:
      | site          | vaccine  | vaccine_type                      | batch_number |
      | NEELIMA HOUSE | COVID-19 | Comirnaty Original/Omicron BA.4-5 | SD7YY2-24    |
