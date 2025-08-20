Feature: Age based warnings

  Background:
    Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>

  Scenario Outline: Display warning based on age when recording a vaccine
    When I search for the patient with NHS number <nhs_number>
    And I proceed to record a vaccine for <vaccine_type> for all products
    Then the system should display the warnings <expected_warning_count>

    Examples:
      | nhs_number | expected_warning_count | vaccine_type | care_model         | user_role          | site                         |
      | 9693297318 | 3                      | covid        | Trust site         | lead administrator | Weaverham Surgery            |
      | 9693297911 | 3                      | covid        | Trust site         | lead administrator | Weaverham Surgery            |
      | 5990002130 | 3                      | covid        | Community pharmacy | administrator      | Aspire Pharmacy              |
      | 5558557400 | 3                      | covid        | Community pharmacy | administrator      | Leeds Pharmacy               |
      | 5558569409 | 3                      | covid        | Branch surgery     | recorder           | Aire Valley Surgery (Rawdon) |
      | 5990393709 | 2                      | covid        | Branch surgery     | recorder           | Aire Valley Surgery (Rawdon) |
