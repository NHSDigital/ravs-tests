Feature: Age based warnings

  Scenario Outline: Display warning based on age when recording a vaccine
    Given I am logged into the RAVS app
    When I search for the patient with NHS number <nhs_number>
    And I proceed to record a vaccine for <vaccine_type> for all products
    Then the system should display the warnings <expected_warning_count>

    Examples:
      | nhs_number  | expected_warning_count    | vaccine_type |
      | 9732091169  | 3                         | covid        |
      | 9692237893  | 3                         | covid        |
      | 9474335761  | 3                         | covid        |
      | 9450153485  | 3                         | covid        |
      | 9470472918  | 3                         | covid        |
      | 9473673388  | 2                         | covid        |
