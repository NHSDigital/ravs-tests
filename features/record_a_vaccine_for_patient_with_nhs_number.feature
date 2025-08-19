@recordvaccine
Feature: Record vaccine

  Background:
    Given I am logged into the RAVS app as administrator into care model Trust site with <site>

  @recordvaccine
  Scenario Outline: Record a vaccine with nhs number
    Given I set vaccinator details with <site> and <vaccination_location> and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
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
      | index | nhs_number | site                    | vaccination_location                  | eligibility | assess_date | consent | vaccination | vaccination_date | name           | dob        | address                                                              | chosen_vaccine | batch_number    | batch_expiry_date |
      | 0     | 5990379013 | Weaverham Surgery       | Vaccination Centre open to the public | yes         | today       | yes     | yes         | today            | LAURIE RAMSAY  | 6/12/1953  | 01, Moore, Bishop, Essex, N8 7RE                                     | COVID-19       | AUTOMATION-SJ1  | 7/9/2025          |
      | 1     | 5990379013 | Spire Cheshire Hospital | Hospital hub for staff and patients   | yes         | today-1     | yes     | yes         | today            | LAURIE RAMSAY  | 6/12/1953  | 01, Moore, Bishop, Essex, N8 7RE                                     | COVID-19       | AUTOMATION-C10  | 19/2/2026         |
      | 2     | 9470057589 | Weaverham Surgery       | Care home                             | yes         | today-2     | yes     | yes         | today-1          | ROGER SEABORNE | 13/12/1922 | 10 ANN STREET, DALTON-IN-FURNESS, CUMBRIA, LA15 8BG                  | COVID-19       | AUTOMATION-C3   | 19/10/2026        |
      | 3     | 9472710255 | Watling Street Surgery  | Housebound patient's home             | yes         | today-3     | yes     | yes         | today-2          | DELICE PINKER  | 10/11/1926 | HARDCRAGG HOUSE, HARDCRAGG WAY, GRANGE-OVER-SANDS, CUMBRIA, LA11 6BH | COVID-19       | AUTOMATION-SJ1  | 19/10/2026        |
      | 0     | 9474376638 | Watling Street Surgery  | Care home                             | yes         | today-32    | yes     | yes         | today-30         | PHYLLIDA ZYLKO | 6/2/1968   | BELL FARM BUNGALOW, CATON GREEN, BROOKHOUSE, LANCASTER, LA2 9JG      | Flu            | AUTOMATION-QIHD | 19/10/2026        |
      | 1     | 9474405174 | Spire Cheshire Hospital | Housebound patient's home             | yes         | today       | yes     | yes         | today            | PHINEAS FAYLE  | 4/9/1965   | 2 DIXON TERRACE, NETHER KELLET, CARNFORTH, LANCS, LA6 1EX            | Flu            | AUTOMATED-AQI   | 19/10/2026        |
      | 2     | 9474405174 | Weaverham Surgery       | Outreach event                        | yes         | today-2     | yes     | yes         | today            | PHINEAS FAYLE  | 4/9/1965   | 2 DIXON TERRACE, NETHER KELLET, CARNFORTH, LANCS, LA6 1EX            | Flu            | AUTOMATION-CBQI | 19/10/2026        |
      | 3     | 9450134391 | Watling Street Surgery  | Vaccination Centre                    | yes         | today-3     | yes     | yes         | today            | MARIAN PIESSE  | 17/7/1994  | 2 BIRCH STREET, LYTHAM ST. ANNES, LANCS, FY8 5DT                     | Flu            | AUTOMATION-QI   | 19/10/2026        |
      | 4     | 9450140960 | Spire Cheshire Hospital | Hospital hub for staff and patients   | yes         | today-1     | yes     | yes         | today            | DEANA GAMBLES  | 5/9/1993   | 10 GRASMERE ROAD, LYTHAM ST. ANNES, LANCS, FY8 2HZ                   | Flu            | AUTOMATION-SJ1  | 19/10/2026        |
      | 5     | 9450141444 | Weaverham Surgery       | Care home                             | yes         | today-4     | yes     | yes         | today-2          | BRANDIE DYBLE  | 25/8/1992  | 49 BLACKPOOL ROAD NORTH, LYTHAM ST. ANNES, LANCS, FY8 3DF            | Flu            | AUTOMATION-QI   | 19/10/2026        |
      | 0     | 9727840361 | Weaverham Surgery       | Outreach event                        | yes         | today       | yes     | yes         | today            | BOBBY TICKLE   | 04/5/1983  | 1 Canning Way, LOUGHBOROUGH, Leics, LE11 5YA                         | MMR            | AUTOMATION-MVX  | 19/10/2026        |
      | 1     | 5998022750 | Spire Regency Hospital  | Outreach event                        | yes         | today       | yes     | yes         | today            | LAURIE QUINN   | 2/2/1941   | 18 Regent Street Oakham, MI, DH3 3UW                                 | MMR            | AUTOMATION-MPR  | 19/10/2026        |
      | 0     | 9474376638 | Watling Street Surgery  | Care home                             | yes         | today-32    | yes     | yes         | today-30         | PHYLLIDA ZYLKO | 6/2/1968   | BELL FARM BUNGALOW, CATON GREEN, BROOKHOUSE, LANCASTER, LA2 9JG      | Flu (London)   | AUTOMATION-QIHD | 19/10/2026        |
      | 1     | 9474405174 | Spire Cheshire Hospital | Housebound patient's home             | yes         | today       | yes     | yes         | today            | PHINEAS FAYLE  | 4/9/1965   | 2 DIXON TERRACE, NETHER KELLET, CARNFORTH, LANCS, LA6 1EX            | Flu (London)   | AUTOMATED-AQI   | 19/10/2026        |
      | 2     | 9474405174 | Weaverham Surgery       | Outreach event                        | yes         | today-2     | yes     | yes         | today            | PHINEAS FAYLE  | 4/9/1965   | 2 DIXON TERRACE, NETHER KELLET, CARNFORTH, LANCS, LA6 1EX            | Flu (London)   | AUTOMATION-CBQI | 19/10/2026        |
      | 3     | 9450134391 | Watling Street Surgery  | Vaccination Centre                    | yes         | today-3     | yes     | yes         | today            | MARIAN PIESSE  | 17/7/1994  | 2 BIRCH STREET, LYTHAM ST. ANNES, LANCS, FY8 5DT                     | Flu (London)   | AUTOMATION-QI   | 19/10/2026        |
      | 4     | 9450140960 | Spire Cheshire Hospital | Hospital hub for staff and patients   | yes         | today-1     | yes     | yes         | today            | DEANA GAMBLES  | 5/9/1993   | 10 GRASMERE ROAD, LYTHAM ST. ANNES, LANCS, FY8 2HZ                   | Flu (London)   | AUTOMATION-SJ1  | 19/10/2026        |
      | 5     | 9450141444 | Weaverham Surgery       | Care home                             | yes         | today-4     | yes     | yes         | today-2          | BRANDIE DYBLE  | 25/8/1992  | 49 BLACKPOOL ROAD NORTH, LYTHAM ST. ANNES, LANCS, FY8 3DF            | Flu (London)   | AUTOMATION-QI   | 19/10/2026        |
      | 0     | 9474376638 | Watling Street Surgery  | Care home                             | yes         | today-32    | yes     | yes         | today-30         | PHYLLIDA ZYLKO | 6/2/1968   | BELL FARM BUNGALOW, CATON GREEN, BROOKHOUSE, LANCASTER, LA2 9JG      | Pneumococcal   | AUTOMATION-QIHD | 19/10/2026        |
  ### This test is no longer needed because of the changes being made to vaccine and batch management ###
  # @recordvaccine
  # Scenario Outline: Record a vaccine with nhs number and auto-select batch number as only one vaccine product
  #   Given I login to RAVS and set vaccinator details with <site> and <care_model> and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
  #   And I search for a patient with the NHS number in the find a patient screen
  #   And I open the patient record by clicking on patient <name>
  #   When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
  #   And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
  #   And I record <consent> with the details and click continue to vaccinate button
  #   And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen without selecting batch number as the vaccine product has only one batch so it should be auto-selected
  #   Then I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
  #   And I click confirm and save button, I should see a record saved dialogue
  #   And I search for a patient with the NHS number in the find a patient screen
  #   And I open the patient record by clicking on patient <name>
  #   And the immunisation history of the patient should be updated in the patient details page

  #   Examples:
  #     | index | nhs_number | site  | care_model | eligibility | assess_date | consent | vaccination | vaccination_date | name | dob   | address  | chosen_vaccine | batch_number | batch_expiry_date |
  #     | 5 | 5998022750 | Spire Regency Hospital  | Outreach event | yes | today | yes | yes | today | LAURIE QUINN |  2/2/1941 |  		18 Regent Street Oakham, MI, DH3 3UW | COVID-19   |  AUTOMATION-C10 | 19/10/2026 |

  @recordvaccine
  Scenario Outline: Record a maternity vaccine with nhs number
    Given I set vaccinator details with <site> and <care_model> and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
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
      | index | nhs_number | site                    | vaccination_location                | eligibility | due_date  | assess_date | consent | vaccination | vaccination_date | name               | dob        | address                                                                     | chosen_vaccine                    | batch_number   | batch_expiry_date | care_model | user_role     |
      | 0     | 9449306605 | Weaverham Surgery       | Vaccination Centre                  | yes         | today     | today       | yes     | yes         | today            | Srinivasarao Patel | 3/3/2020   | 4 Calicut Lane2, Line 2, LINE 3, Berkshire, KT21 1EJ                        | Pertussis                         | AUTOMATION-AVS | 19/10/2027        | Trust site | administrator |
      | 1     | 9449306605 | Watling Street Surgery  | Vaccination Centre                  | yes         | today+100 | today-1     | yes     | yes         | today-1          | Srinivasarao Patel | 3/3/2020   | 4 Calicut Lane2, Line 2, LINE 3, Berkshire, KT21 1EJ                        | Pertussis                         | AUTOMATION-BIS | 19/10/2028        | Trust site | administrator |
      | 2     | 5990379013 | Spire Cheshire Hospital | Hospital hub for staff and patients | yes         | today+290 | today-1     | yes     | yes         | today            | LAURIE RAMSAY      | 6/12/1953  | 01, Moore, Bishop, Essex, N8 7RE                                            | Pertussis                         | AUTOMATION-RVS | 19/2/2029         | Trust site | administrator |
      | 3     | 9472710255 | Weaverham Surgery       | Housebound patient's home           | yes         | today+5   | today-3     | yes     | yes         | today-2          | DELICE PINKER      | 10/11/1926 | HARDCRAGG HOUSE, HARDCRAGG WAY, GRANGE-OVER-SANDS, CUMBRIA, LA11 6BH        | Respiratory syncytial virus (RSV) | AUTOMATION-ARX | 19/10/2026        | Trust site | administrator |
      | 4     | 5990374534 | Spire Regency Hospital  | Outreach event                      | yes         | today+50  | today-4     | yes     | yes         | today-3          | GABI FOSTER        | 6/6/2004   | CAMPUS CITY NEW CAMPUS 41 BERKELEY ROAD, WESTBURY PARK, Manchester, M16 0RA | Respiratory syncytial virus (RSV) | AUTOMATION-ABR | 1/2/2026          | Trust site | administrator |
