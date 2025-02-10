Feature: Persist fields when recording vaccination

@persistValues
  Scenario Outline: Persist fields when recording a vaccination
    Given I login to RAVS and set vaccinator details with <site> and <care_model> and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    And I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
    And when I click confirm and save button, I should see a record saved dialogue
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    And I start to record the vaccination for a new patient <new_patient_name> with nhs number <new_nhs_number>
    Then the delivery team, vaccine and vaccine product selection should persist on the choose vaccine page
    And the patient's eligibility, assessment date, legal mechanism, assessing clinician, assessment outcome selection must persist on the assessment screen
    And the patient's consent answer, consent given by, consenting clinician, selection must persist on the consent screen
    And the patient's vaccinated answer, vaccine product, vaccinate date, care model, batch number, vaccinator should persist


    Examples:
      | index | nhs_number | site  | care_model | eligibility | assess_date | consent | vaccination | vaccination_date | name | dob   | address  | chosen_vaccine | batch_number | batch_expiry_date | new_nhs_number | new_patient_name |
      | 0 | 9693632109 | ALBERT HOUSE  | Vaccination Centre open to the public | yes | today  | yes  | yes | today   | Bill GARTON |  23/6/1946 |   1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | COVID-19   | AUTOMATION-SJ1   | 19/10/2026 | 9472710255 | DELICE PINKER |
      | 0 | 9693632109 | ALBERT HOUSE  | Care home | yes | today  | yes  | yes | today   | Bill GARTON |  23/6/1946 |   1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | COVID-19   | AUTOMATION-SJ1   | 19/10/2026 | 9472710255 | DELICE PINKER |

@persistValues
  Scenario Outline: Fields should not persist when user changes vaccine product when recording a vaccination
    Given I login to RAVS and set vaccinator details with <site> and <care_model> and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    And I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
    And when I click confirm and save button, I should see a record saved dialogue
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    And I start to record the vaccination for a new patient <new_patient_name> with nhs number <new_nhs_number>
    And I change the delivery team on the choose vaccine page
    Then the patient's eligibility, assessment date, legal mechanism, assessing clinician, assessment outcome selection must not persist on the assessment screen
    And the patient's consent answer, consent given by, consenting clinician, selection must not persist on the consent screen
    And the patient's vaccinated answer, vaccine product, vaccinate date, care model, batch number, vaccinator should not persist

    Examples:
      | index | nhs_number | site  | care_model | eligibility | assess_date | consent | vaccination | vaccination_date | name | dob   | address  | chosen_vaccine | batch_number | batch_expiry_date | new_nhs_number | new_patient_name |
      | 0 | 9693632109 | ALBERT HOUSE  | Vaccination Centre open to the public | yes | today  | yes  | yes | today   | Bill GARTON |  23/6/1946 |   1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | COVID-19   | AUTOMATION-SJ1   | 19/10/2026 | 9472710255 | DELICE PINKER |
