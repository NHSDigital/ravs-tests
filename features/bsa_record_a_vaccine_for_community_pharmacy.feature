Feature: Business services authority (BSA) - Record vaccine for community pharmacies

  @bsarecordvaccine
  Scenario Outline: Record a vaccine at community pharmacy - Add
    Given I login to RAVS as a community pharmacist and set vaccinator details with <site> and <care_model> as community pharmacy and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    And the immunisation history of the patient should be updated in the patient details page

    Examples:
      | index | nhs_number | site  | care_model | eligibility | assess_date | consent | vaccination | vaccination_date | name | dob   | address  | chosen_vaccine | batch_number | batch_expiry_date |
      | 0 | 9693632109 | Leeds Pharmacy  | Outreach event | yes | today  | yes  | yes | today    | Bill GARTON |  23/6/1946 |   1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | COVID-19   | AUTOMATION-SJ1   | 19/10/2026 |
      | 1 | 9693632109 | Leeds Pharmacy  | Vaccination Centre | yes | today  | yes  | yes | today-15   | Bill GARTON |  23/6/1946 |   1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | COVID-19   | AUTOMATION-SJ1   | 19/10/2026 |
      | 2 | 9693632109 | Leeds Pharmacy  | Hospital hub for staff and patients | yes | today  | yes  | yes | today-16   | Bill GARTON |  23/6/1946 |   1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | COVID-19   | AUTOMATION-SJ1   | 19/10/2026 |
      | 3 | 9693632109 | Leeds Pharmacy  | Community pharmacy | yes | today  | yes  | yes | today-13   | Bill GARTON |  23/6/1946 |   1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | COVID-19   | AUTOMATION-SJ1   | 19/10/2026 |
      | 11 | 9450134391 | Leeds Pharmacy | Community pharmacy | yes | today-3 | yes | yes  | today-3 | MARIAN PIESSE | 17/7/1994 | 2 BIRCH STREET, LYTHAM ST. ANNES, LANCS, FY8 5DT | Flu | AUTOMATION-QI | 19/10/2026 |
      | 11 | 9450134391 | Leeds Pharmacy | Community pharmacy | yes| today | yes | yes  | today-91 | MARIAN PIESSE | 17/7/1994 | 2 BIRCH STREET, LYTHAM ST. ANNES, LANCS, FY8 5DT | Flu | AUTOMATION-QI | 19/10/2026 |
      | 2 | 9450134391 | Leeds Pharmacy | Community pharmacy | yes| today | yes | yes  | today-92 | MARIAN PIESSE | 17/7/1994 | 2 BIRCH STREET, LYTHAM ST. ANNES, LANCS, FY8 5DT | Flu | AUTOMATION-QI | 19/10/2026 |
      | 11 | 9450134391 | Leeds Pharmacy | Hospital hub for staff and patients | yes | today | yes | yes  | today-89 | MARIAN PIESSE | 17/7/1994 | 2 BIRCH STREET, LYTHAM ST. ANNES, LANCS, FY8 5DT | Flu | AUTOMATION-QI | 19/10/2026 |
      | 12 | 9450134391 | Leeds Pharmacy | Community pharmacy | yes | today | yes | yes  |  today-121 | MARIAN PIESSE | 17/7/1994 | 2 BIRCH STREET, LYTHAM ST. ANNES, LANCS, FY8 5DT | Flu | AUTOMATION-QI | 19/10/2026 |

  @bsarecordvaccine
  Scenario Outline: Record a maternity vaccine at community pharmacy with nhs number - Add
    Given I login to RAVS as a community pharmacist and set vaccinator details with <site> and <care_model> as community pharmacy and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the pregnant patient's <eligibility> with the details of due date as <due_date> and assessment date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    And the immunisation history of the patient should be updated in the patient details page

    Examples:
      | index | nhs_number | site   | care_model      | eligibility | due_date | assess_date | consent | vaccination | vaccination_date | name  | dob    | address     | chosen_vaccine  | batch_number | batch_expiry_date |
      |  4 | 9473629885 | Leeds Pharmacy | Outreach event | yes | today+50 | today-4 | yes | yes | today-3 | MARGIE PUCKEY | 27/5/1924 | MANSART COURT, 10 OLIVE SHAPLEY AVENUE, MANCHESTER, M20 6QB | Respiratory syncytial virus (RSV) | 	AUTOMATION-ABR | 1/2/2026 |
      | 0 | 9693632109 | Leeds Pharmacy | Vaccination Centre | yes | today | today | yes | yes | today | Bill GARTON | 23/6/1946 | 1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | Pertussis | AUTOMATION-AVS | 19/10/2027 |
      | 1 | 9693632109 | Leeds Pharmacy | Vaccination Centre | yes | today+100 | today-1 | yes | yes | today-1  | Bill GARTON | 23/6/1946 | 1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | Pertussis |  AUTOMATION-BIS | 19/10/2028 |
      | 2 | 9470040228 | Leeds Pharmacy | Hospital hub for staff and patients | yes | today+290 | today-1 | yes | yes | today  | HERBERT HAAG  | 14/12/1922 | 10 COASTAL ROAD, HEST BANK, LANCASTER, LA2 6HN | Pertussis | AUTOMATION-RVS | 19/2/2029 |
      | 3 | 9472710255 | Leeds Pharmacy  | Housebound patient's home | yes | today+5 | today-3 | yes | yes | today-2 | DELICE PINKER | 10/11/1926 | HARDCRAGG HOUSE, HARDCRAGG WAY, GRANGE-OVER-SANDS, CUMBRIA, LA11 6BH | Respiratory syncytial virus (RSV) |  AUTOMATION-ARX | 19/10/2026 |
      # | 4 | 9473629885 | BECCLES HOUSE | Outreach event | yes | today+50 | today-4 | yes | yes | today-3  | MARGIE PUCKEY |  27/5/1924 | MANSART COURT, 10 OLIVE SHAPLEY AVENUE, MANCHESTER, M20 6QB | Respiratory syncytial virus (RSV) |  AREX2-15A | 19/10/2026 |   - # This test is no longer needed as Arexvy has been decommissioned on 29th Nov 2024


