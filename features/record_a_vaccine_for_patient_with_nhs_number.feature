Feature: Record vaccine 

@recordvaccine
Scenario Outline: Record a vaccine with nhs number
    Given I login to RAVS and get patient details from <data_file>
    And set the vaccinator details
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record and click choose vaccine button
    When I choose the vaccine and vaccine type and click continue
    And I assess the patient's eligibility with the details and click continue to record consent screen button
    And I record consent with the details and click continue to vaccinate button
    And I enter vaccination details and click Continue to Check and confirm screen
    Then I need to be able to see the patient details on the check and confirm screen
    And when I click confirm and save button, the immunisation hitsory of the patient should be updated in the patient details page

Examples: 
    | data_file                                                     |
    | record_vaccine_data_all_yes_9693632109.json                   |
    | record_vaccine_data_all_yes_9470040228.json                   |
    | record_vaccine_data_all_yes_9470057589.json                   |
    | record_vaccine_data_not_eligible_consented_vaccinated.json    |
    | record_vaccine_data_not_eligible_not_consented.json           |