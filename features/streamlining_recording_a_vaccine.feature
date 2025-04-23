@streamlining
Feature: Streamlining Recording vaccine

  Background:
  Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>
  And the logged in user is identified as a <clinician> (true/false)
  And I retrieve the vaccine product at index <index> for <chosen_vaccine>
  And I ensure that site has the batch number <batch_number> and expiry date <expiry_date> for the chosen vaccine

  @recordvaccine
  Scenario Outline: Record a vaccine with nhs number
    Given I click record vaccinations navigation link
    And I set vaccinator as <vaccinator>
    And I select vaccine - <chosen_vaccine>
    And I select vaccine product
    And I select batch
    And I select patient's eligibility for the vaccine
    And I select the location where vaccination was given
    And I enter the patient's NHS number - <nhs_number>
    And I select where the injection was given
    # And I confirm all details and click check and confirm button
    # Then the vaccination should be recorded successfully

    Examples:
    | index | user_role           | site     | clinician | chosen_vaccine | batch_number | expiry_date | vaccinator | nhs_number | care_model |
    | 0     | lead administrator | Leeds Pharmacy | True      | COVID-19       | AUTO-C-10-JN | 19/10/2031  | None | 9470040228 | community pharmacy |

  #     # | 2 | 9470040228 | Spire Cheshire Hospital  | Hospital hub for staff and patients | yes  | today-1  | yes | yes | today | HERBERT HAAG | 14/12/1922 | 10 COASTAL ROAD, HEST BANK, LANCASTER, LA2 6HN | COVID-19 |  AUTOMATION-C10  | 19/2/2026 |
  #     # | 3 | 9470057589 | Weaverham Surgery  | Care home | yes  | today-2 | yes | yes | today-1 | ROGER SEABORNE | 13/12/1922 | 10 ANN STREET, DALTON-IN-FURNESS, CUMBRIA, LA15 8BG | COVID-19  | 	AUTOMATION-C3 | 19/10/2026 |
  #     # | 4 | 9472710255 | Watling Street Surgery | Housebound patient's home | yes | today-3 | yes | yes  | today-2 | DELICE PINKER | 10/11/1926 | HARDCRAGG HOUSE, HARDCRAGG WAY, GRANGE-OVER-SANDS, CUMBRIA, LA11 6BH | COVID-19 | 	AUTOMATION-SJ1 | 19/10/2026 |
  #     # | 5 | 9473629885 | Spire Cheshire Hospital | Outreach event | yes | today-4 | yes | yes | today-3 | MARGIE PUCKEY | 27/5/1924 | MANSART COURT, 10 OLIVE SHAPLEY AVENUE, MANCHESTER, M20 6QB | COVID-19 | AUTOMATION-C30 | 19/10/2026 |
  #     # | 6 | 9437540233 | Weaverham Surgery  | Vaccination Centre | yes | today-5 | yes | yes | today-2 | RANDY FOGDEN | 8/6/1961 | 10 ASHVILLE TERRACE, MANCHESTER, M40 9WG | COVID-19   |  AUTOMATION-C10 | 19/10/2026 |
  #     # | 7 | 9474374228 | Watling Street Surgery | Hospital hub for staff and patients  | yes  | today-6 | yes | yes | today-3 | ORINDA JUDD | 20/7/1963 | 2 RECTORY PADDOCK, HALTON, LANCASTER, LA2 6LL | COVID-19 | AUTOMATION-C3 | 19/10/2026 |
  #     # | 8 | 9437580812 | Spire Cheshire Hospital | Care home | yes | today-7 | yes | yes | today-7 | INDIGO CATCHESIDE | 1/3/1959 | 12 CANBERRA STREET, MANCHESTER, M11 4WL | COVID-19 | AUTOMATION-SJ1 | 19/10/2026 |
  #     # | 9 | 9437599165 | Weaverham Surgery | Housebound patient's home | yes | today-30 | yes | yes | today-30 | CAWRDAV BOBBETT | 21/7/1959 | 127 ALINORA CRESCENT, GORING-BY-SEA, WORTHING, W SUSSEX, BN12 4HN | COVID-19 | AUTOMATION-C30 | 19/10/2026 |
  #     # | 10 | 9474335052 | Watling Street Surgery | Outreach event | yes | today-2 | yes | yes | today-2 | AMERY PIGGOTT | 20/4/1968 | 10 CONNAUGHT ROAD, LANCASTER, LA1 4BQ | COVID-19 | AUTOMATION-C10 | 19/10/2026 |
  #     # | 11 | 9437541817 | Spire Cheshire Hospital | Vaccination Centre | yes  | today-3 | yes | yes | today-1 | FLORINDA DUNNER |  27/3/1957 | 32 HOLLAND ROAD, MANCHESTER, M8 4NP | COVID-19 | AUTOMATION-C3 | 19/10/2026 |
  #     # | 12 | 9437540233 | Weaverham Surgery  | Hospital hub for staff and patients | yes | today-15 | yes | yes | today-7 | RANDY FOGDEN | 8/6/1961 | 10 ASHVILLE TERRACE, MANCHESTER, M40 9WG | COVID-19 | AUTOMATION-SJ1 | 19/10/2026 |
  #     # | 8 | 9474376638 | Watling Street Surgery | Care home | yes | today-32 | yes | yes | today-30 | PHYLLIDA ZYLKO | 6/2/1968 | BELL FARM BUNGALOW, CATON GREEN, BROOKHOUSE, LANCASTER, LA2 9JG      | Flu | AUTOMATION-QIHD | 19/10/2026 |
  #     # | 9 | 9474405174 | Spire Cheshire Hospital   | Housebound patient's home | yes | today | yes | yes | today | PHINEAS FAYLE | 4/9/1965 | 2 DIXON TERRACE, NETHER KELLET, CARNFORTH, LANCS, LA6 1EX | Flu | AUTOMATED-AQI | 19/10/2026 |
  #     # | 10 | 9474405174 | Weaverham Surgery  | Outreach event | yes | today-2 | yes  | yes | today | PHINEAS FAYLE | 4/9/1965 | 2 DIXON TERRACE, NETHER KELLET, CARNFORTH, LANCS, LA6 1EX | Flu | AUTOMATION-CBQI | 19/10/2026 |
  #     # | 11 | 9450134391 | Watling Street Surgery | Vaccination Centre | yes | today-3 | yes | yes  | today | MARIAN PIESSE | 17/7/1994 | 2 BIRCH STREET, LYTHAM ST. ANNES, LANCS, FY8 5DT | Flu | AUTOMATION-QI | 19/10/2026 |
  #     # | 12 | 9450140960 | Spire Cheshire Hospital | Hospital hub for staff and patients | yes | today-1  | yes | yes| today | DEANA GAMBLES | 5/9/1993 | 10 GRASMERE ROAD, LYTHAM ST. ANNES, LANCS, FY8 2HZ | Flu |  AUTOMATION-SJ1 | 19/10/2026 |
  #     # | 1 | 9450141444 | Weaverham Surgery  | Care home | yes | today-4 | yes | yes | today-2 | BRANDIE DYBLE | 25/8/1992 | 49 BLACKPOOL ROAD NORTH, LYTHAM ST. ANNES, LANCS, FY8 3DF | Flu  |  AUTOMATION-QI |  19/10/2026 |
  #     # | 2 | 9450141711 | Watling Street Surgery | Housebound patient's home | yes | today-2| yes | yes | today-1 | KRISTIA SIDAWAY | 24/6/1992 | 41 BALTIMORE ROAD, LYTHAM ST. ANNES, LANCS, FY8 3NY | Flu | AUTOMATION-IT | 19/10/2026  |
  #     # | 3 | 9450144699 | Spire Cheshire Hospital   | Outreach event  | yes | today-1 | yes | yes | today-1 | HOPE TULLY | 10/1/1993 | 2 CHAPEL CLOSE, WESHAM, PRESTON, PR4 3HB | Flu    |  AUTOMATION-LAIV | 19/10/2026 |
  #     # | 4 | 9437541817 | Weaverham Surgery  | Outreach event | yes | today | yes | yes | today | FLORINDA DUNNER |  27/3/1957 | 32 HOLLAND ROAD, MANCHESTER, M8 4NP | Flu | AUTOMATION-LAIV | 19/10/2026 |
  #     # | 5 | 9223638941 | Weaverham Surgery  | Outreach event | yes | today | yes | yes | today | MICHELLE DONNELLY |  05/5/1900 | 	6 WHESSOE ROAD, HARDWICK, STOCKTON-ON-TEES, CLEVELAND, TS19 8LB | Flu | AUTOMATION-LAIV | 19/10/2026 |
  #     # | 6 | 9449306125 | Weaverham Surgery  | Outreach event | yes | today | yes | yes | today | NEELY SCULLION |  14/09/1946 |	35 THE AVENUE, TADWORTH, SURREY, KT20 5DG | Flu | AUTOMATION-SJ1 | 19/10/2026 |
  #     # | 6 | 9449306125 | Weaverham Surgery  | Outreach event | yes | today | yes | yes | today | NEELY SCULLION |  14/09/1946 |	35 THE AVENUE, TADWORTH, SURREY, KT20 5DG | Flu | AUTOMATION-SJ1 | 19/10/2026 |
  #     # | 4 | 9727840361 | Weaverham Surgery  | Outreach event | yes | today | yes | yes | today | BOBBY TICKLE |  04/5/1983 |  1 Canning Way, LOUGHBOROUGH, Leics, LE11 5YA | COVID-19   |  AUTOMATION-C10 | 19/10/2026 |
  #     # | 5 | 9449303975 | Spire Regency Hospital  | Outreach event | yes | today | yes | yes | today | ROS METHERALL |  19/8/1999 |  	10 GREENACRES, BOOKHAM, LEATHERHEAD, SURREY, KT23 3NG | COVID-19   |  AUTOMATION-C10 | 19/10/2026 |
  #     # | 5 | 9449303975 | Spire Regency Hospital  | GP clinic | yes | today | yes | yes | today | ROS METHERALL |  19/8/1999 |  	10 GREENACRES, BOOKHAM, LEATHERHEAD, SURREY, KT23 3NG | COVID-19   |  AUTOMATION-C10 | 19/10/2026 |


  # ### This test is no longer needed because of the changes being made to vaccine and batch management ###
  #   # @recordvaccine
  # # Scenario Outline: Record a vaccine with nhs number and auto-select batch number as only one vaccine product
  # #   Given I login to RAVS and set vaccinator details with <site> and <care_model> and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
  # #   And I search for a patient with the NHS number in the find a patient screen
  # #   And I open the patient record by clicking on patient <name>
  # #   When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
  # #   And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
  # #   And I record <consent> with the details and click continue to vaccinate button
  # #   And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen without selecting batch number as the vaccine product has only one batch so it should be auto-selected
  # #   Then I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
  # #   And I click confirm and save button, I should see a record saved dialogue
  # #   And I search for a patient with the NHS number in the find a patient screen
  # #   And I open the patient record by clicking on patient <name>
  # #   And the immunisation history of the patient should be updated in the patient details page

  # #   Examples:
  # #     | index | nhs_number | site  | care_model | eligibility | assess_date | consent | vaccination | vaccination_date | name | dob   | address  | chosen_vaccine | batch_number | batch_expiry_date |
  # #     | 5 | 9449303975 | Spire Regency Hospital  | Outreach event | yes | today | yes | yes | today | ROS METHERALL |  19/8/1999 |  	10 GREENACRES, BOOKHAM, LEATHERHEAD, SURREY, KT23 3NG | COVID-19   |  AUTOMATION-C10 | 19/10/2026 |

  # @recordvaccine
  # Scenario Outline: Record a maternity vaccine with nhs number
  #   Given I set vaccinator details with <site> and <care_model> and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
  #   And I search for a patient with the NHS number in the find a patient screen
  #   And I open the patient record by clicking on patient <name>
  #   When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
  #   And I assess the pregnant patient's <eligibility> with the details of due date as <due_date> and assessment date as <assess_date> and click continue to record consent screen button
  #   And I record <consent> with the details and click continue to vaccinate button
  #   And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
  #   Then I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
  #   And I click confirm and save button, I should see a record saved dialogue
  #   And I search for a patient with the NHS number in the find a patient screen
  #   And I open the patient record by clicking on patient <name>
  #   And the immunisation history of the patient should be updated in the patient details page

  #   Examples:
  #     | index | nhs_number | site   | vaccination_location      | eligibility | due_date | assess_date | consent | vaccination | vaccination_date | name  | dob    | address     | chosen_vaccine  | batch_number | batch_expiry_date | care_model         | user_role          |
  #     |  4 | 9473629885 | Spire Regency Hospital | Outreach event | yes | today+50 | today-4 | yes | yes | today-3 | MARGIE PUCKEY | 27/5/1924 | MANSART COURT, 10 OLIVE SHAPLEY AVENUE, MANCHESTER, M20 6QB | Respiratory syncytial virus (RSV) | 	AUTOMATION-ABR | 1/2/2026 | Trust site | administrator      |

  #     # | 0 | 9693632109 | Weaverham Surgery | Vaccination Centre | yes | today | today | yes | yes | today | Bill GARTON | 23/6/1946 | 1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | Pertussis | AUTOMATION-AVS | 19/10/2027 |
  #     # | 1 | 9693632109 | Watling Street Surgery | Vaccination Centre | yes | today+100 | today-1 | yes | yes | today-1  | Bill GARTON | 23/6/1946 | 1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | Pertussis |  AUTOMATION-BIS | 19/10/2028 |
  #     # | 2 | 9470040228 | Spire Cheshire Hospital | Hospital hub for staff and patients | yes | today+290 | today-1 | yes | yes | today  | HERBERT HAAG  | 14/12/1922 | 10 COASTAL ROAD, HEST BANK, LANCASTER, LA2 6HN | Pertussis | AUTOMATION-RVS | 19/02/2029 |
  #     # | 3 | 9472710255 | Weaverham Surgery  | Housebound patient's home | yes | today+5 | today-3 | yes | yes | today-2 | DELICE PINKER | 10/11/1926 | HARDCRAGG HOUSE, HARDCRAGG WAY, GRANGE-OVER-SANDS, CUMBRIA, LA11 6BH | Respiratory syncytial virus (RSV) |  AUTOMATION-ARX | 19/10/2026 |
  #     # | 4 | 9473629885 | Watling Street Surgery | Outreach event | yes | today+50 | today-4 | yes | yes | today-3  | MARGIE PUCKEY |  27/5/1924 | MANSART COURT, 10 OLIVE SHAPLEY AVENUE, MANCHESTER, M20 6QB | Respiratory syncytial virus (RSV) |  AREX2-15A | 19/10/2026 |   - # This test is no longer needed as Arexvy has been decommissioned on 29th Nov 2024


