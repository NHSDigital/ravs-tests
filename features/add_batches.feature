Feature: Add Batches to vaccine

  @addbatches
  Scenario: Add vaccine batches page should launch
    Given I am logged into the RAVS app
    When I am on the vaccines page
    And I click on an available add batch link
    Then the add batch page should be launched

  @addbatches
  Scenario: Error messages should appear when no values are entered
    Given I am logged into the RAVS app
    When I am on the vaccines page
    And I click on an available add batch link
    And I click continue to confirm batch details page
    Then the error messages and error links should appear highlighting missing required fields

  @addbatches
  Scenario Outline: Add batch to vaccine
    Given I am on the RAVS home page
    When I am on the vaccines page
    And I view product for the existing vaccine in an existing site
    And I enter batch number  that already exists and expiry date
    Then the batch is already added to site warning should appear

    Examples:
      | site         | vaccine  | vaccine_type  | batch_number     |
      | ALBERT HOUSE | COVID-19 | Spikevax JN.1 | AB2345-Y7890     |
