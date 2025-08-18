Feature: Add Batches to vaccine

  Background:
    Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>

  @addbatches
  Scenario: Add vaccine batches page should launch
    When I am on the vaccines page
    And I click on an available add batch link
    Then the add batch page should be launched

    Examples:
      | care_model         | user_role          | site                         |
      | Trust site         | lead administrator | Weaverham Surgery            |
      | Community pharmacy | administrator      | Aspire Pharmacy              |
      | Branch surgery     | administrator      | Aire Valley Surgery (Rawdon) |

  @addbatches
  Scenario: Error messages should appear when no values are entered
    When I am on the vaccines page
    And I click on an available add batch link
    And I click continue to confirm batch details page
    Then the error messages and error links should appear highlighting missing required fields

    Examples:
      | care_model         | user_role          | site                         |
      | Trust site         | lead administrator | Weaverham Surgery            |
      | Community pharmacy | administrator      | Aspire Pharmacy              |
      | Branch surgery     | administrator      | Aire Valley Surgery (Rawdon) |


  @addbatches
  Scenario: Error message should appear when batch expiry date is in the past
    When I am on the vaccines page
    And I click on an available add batch link
    And I enter batch expiry date in the past
    Then the error message and error link should appear highlighting batch expiry date is in past

    Examples:
      | care_model         | user_role          | site                         |
      | Trust site         | lead administrator | Weaverham Surgery            |
      | Community pharmacy | administrator      | Aspire Pharmacy              |
      | Branch surgery     | administrator      | Aire Valley Surgery (Rawdon) |

  @addbatches
  Scenario Outline: Add batch to vaccine
    When I am on the vaccines page
    And I view product for the existing <vaccine_type> in an existing <site>
    And I enter <batch_number> that already exists with <expiry_date> and <pack_size>
    Then the batch is already added to site warning should appear

    Examples:
      | care_model         | user_role          | site                         | vaccine  | vaccine_type  | batch_number   | expiry_date | pack_size   |
      | Trust site         | lead administrator | Weaverham Surgery            | COVID-19 | Spikevax JN.1 | AUTOMATION-SJ1 | 19/10/2026  | -           |
      | Community pharmacy | administrator      | Aspire Pharmacy              | COVID-19 | Spikevax JN.1 | AUTOMATION-SJ1 | 19/10/2026  | Single vial |
      | Branch surgery     | administrator      | Aire Valley Surgery (Rawdon) | COVID-19 | Spikevax JN.1 | AUTOMATION-SJ1 | 19/10/2026  | 10 vials    |
