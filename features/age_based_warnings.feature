Feature: Age based warnings

  Background:
    Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>

  Scenario Outline: Display warning based on age when recording a vaccine
    When I search for the patient with NHS number <nhs_number>
    And I proceed to record a vaccine for <vaccine_type> for all products
    Then the system should display the warnings <expected_warning_count>

    Examples:
      | nhs_number  | expected_warning_count | vaccine_type | care_model         | user_role           |  site               |
      | 9732091169  | 3                      | covid        | Trust site         | lead administrator  |  Weaverham Surgery  |
      | 9692237893  | 3                      | covid        | Trust site         | lead administrator  |  Weaverham Surgery  |
      | 9474335761  | 3                      | covid        | Community pharmacy | administrator       |  Aspire Pharmacy    |
      | 9450153485  | 3                      | covid        | Community pharmacy | administrator       |  Leeds Pharmacy     |
      | 9470472918  | 3                      | covid        | Branch surgery     | recorder            | Aire Valley Surgery (Rawdon)  |
      | 9473673388  | 2                      | covid        | Branch surgery     | recorder            | Aire Valley Surgery (Rawdon)  |
