Feature: Persist fields when recording vaccination

  Background:
  Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>

@persistValues
  Scenario Outline: Persist fields when recording a vaccination
    Given I set vaccinator details with <site> and <vaccination_location> and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    And I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    And I start to record the vaccination for a new patient <new_patient_name> with nhs number <new_nhs_number>
    Then the delivery team, vaccine and vaccine product selection should persist on the choose vaccine page
    And the patient's eligibility, assessment date, legal mechanism, assessing clinician, assessment outcome selection must persist on the assessment screen
    And the patient's consent answer, consent given by, consenting clinician, selection must persist on the consent screen
    And the patient's vaccinated answer, vaccine product, vaccinate date, care model, batch number, vaccinator should persist

Examples:
  | index | nhs_number | site               | vaccination_location                          | eligibility | assess_date | consent | vaccination | vaccination_date | name        | dob        | address                                                   | chosen_vaccine | batch_number     | batch_expiry_date | new_nhs_number | new_patient_name | care_model         | user_role          |
  | 0     | 9693632109 | Weaverham Surgery  | Vaccination Centre open to the public       | yes         | today       | yes     | yes         | today            | Bill GARTON | 23/6/1946  | 1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | COVID-19       | AUTOMATION-SJ1   | 19/10/2026        | 9472710255     | DELICE PINKER    | Trust site         | lead administrator |
  | 0     | 9693632109 | Aspire Pharmacy  | Care home                                   | yes         | today       | yes     | yes         | today            | Bill GARTON | 23/6/1946  | 1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | COVID-19       | AUTOMATION-SJ1   | 19/10/2026        | 9472710255     | DELICE PINKER    | Community pharmacy | administrator      |


@persistValues
  Scenario Outline: Fields should not persist when user changes delivery team when recording a vaccination
    Given I set vaccinator details with <site> and <vaccination_location> and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date> and new delivery team <new_delivery_team>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    And I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    And I start to record the vaccination for a new patient <new_patient_name> with nhs number <new_nhs_number>
    And I change the delivery team on the choose vaccine page
    Then the patient's eligibility, assessment date, legal mechanism, assessing clinician, assessment outcome selection must not persist on the assessment screen
    And the patient's consent answer, consent given by, consenting clinician, selection must not persist on the consent screen
    And the patient's vaccinated answer, vaccine product, vaccinate date, care model, batch number, vaccinator should not persist

Examples:
  | index | nhs_number | site                               | vaccination_location                          | eligibility | assess_date | consent | vaccination | vaccination_date | name        | dob        | address                                                   | chosen_vaccine | batch_number     | batch_expiry_date | new_nhs_number | new_patient_name | care_model         | user_role          | new_delivery_team           |
  | 0     | 9693632109 | Weaverham Surgery                 | Vaccination Centre open to the public       | yes         | today       | yes     | yes         | today            | Bill GARTON | 23/6/1946  | 1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | COVID-19       | AUTOMATION-SJ1   | 19/10/2026        | 9472710255     | DELICE PINKER    | Trust site         | lead administrator | Spire Regency Hospital      |
  | 0     | 9693632109 | Aspire Pharmacy                   | Care home                                   | yes         | today       | yes     | yes         | today            | Bill GARTON | 23/6/1946  | 1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | COVID-19       | AUTOMATION-SJ1   | 19/10/2026        | 9472710255     | DELICE PINKER    | Community pharmacy | administrator      | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service      |

@persistValues
  Scenario Outline: Fields should not persist when user changes vaccine product when recording a vaccination
    Given I set vaccinator details with <site> and <vaccination_location> and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date> and new vaccine product <new_vaccine_product>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    And I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    And I start to record the vaccination for a new patient <new_patient_name> with nhs number <new_nhs_number>
    And I change the vaccination product on the choose vaccine page
    Then the patient's eligibility, assessment date, legal mechanism, assessing clinician, assessment outcome selection must not persist on the assessment screen
    And the patient's consent answer, consent given by, consenting clinician, selection must not persist on the consent screen
    And the patient's vaccinated answer, vaccine product, vaccinate date, care model, batch number, vaccinator should not persist

Examples:
  | index | nhs_number | site                     | vaccination_location | eligibility | assess_date | consent | vaccination | vaccination_date | name          | dob        | address                                          | chosen_vaccine | batch_number     | batch_expiry_date | new_nhs_number | new_patient_name | new_vaccine_product | care_model         | user_role          |
  | 5     | 9449303975 | Weaverham Surgery   | Outreach event       | yes         | today-1     | yes     | yes         | today-1          | ROS METHERALL | 19/8/1999  | 10 GREENACRES, BOOKHAM, LEATHERHEAD, SURREY, KT23 3NG | COVID-19       | AUTOMATION-C10   | 19/10/2026        | 9449306125     | NEELY SCULLION    | Flu                  | Trust site         | lead administrator |
  | 5     | 9449303975 | Aspire Pharmacy  | Outreach event       | yes         | today-1     | yes     | yes         | today-1          | ROS METHERALL | 19/8/1999  | 10 GREENACRES, BOOKHAM, LEATHERHEAD, SURREY, KT23 3NG | COVID-19       | AUTOMATION-C10   | 19/10/2026        | 9449306125     | NEELY SCULLION    | Flu                  | Community pharmacy | administrator      |

@persistValues
  Scenario Outline: Fields should not persist when user changes vaccine product type when recording a vaccination
    Given I set vaccinator details with <site> and <vaccination_location> and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date> and new random vaccine product type
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    And I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    And I start to record the vaccination for a new patient <new_patient_name> with nhs number <new_nhs_number>
    And I change the vaccination product type on the choose vaccine page
    Then the patient's eligibility, assessment date, legal mechanism, assessing clinician, assessment outcome selection must not persist on the assessment screen
    And the patient's consent answer, consent given by, consenting clinician, selection must not persist on the consent screen
    And the patient's vaccinated answer, vaccine product, vaccinate date, care model, batch number, vaccinator should not persist

Examples:
  | index | nhs_number | site                     | vaccination_location | eligibility | assess_date | consent | vaccination | vaccination_date | name          | dob        | address                                          | chosen_vaccine | batch_number     | batch_expiry_date | new_nhs_number | new_patient_name | care_model         | user_role          |
  | 5     | 9449303975 | Weaverham Surgery   | Outreach event       | yes         | today-1     | yes     | yes         | today-1          | ROS METHERALL | 19/8/1999  | 10 GREENACRES, BOOKHAM, LEATHERHEAD, SURREY, KT23 3NG | COVID-19       | AUTOMATION-C10   | 19/10/2026        | 9449306125     | NEELY SCULLION    | Trust site         | lead administrator |
  | 5     | 9449303975 | Aspire Pharmacy  | Outreach event       | yes         | today-1     | yes     | yes         | today-1          | ROS METHERALL | 19/8/1999  | 10 GREENACRES, BOOKHAM, LEATHERHEAD, SURREY, KT23 3NG | COVID-19       | AUTOMATION-C10   | 19/10/2026        | 9449306125     | NEELY SCULLION    |   Community pharmacy | administrator      |


