Feature: Record vaccine

  @recordvaccine
  Scenario Outline: Record a vaccine with nhs number
    Given I login to RAVS and set vaccinator details with <site> and <care_model> and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
    And when I click confirm and save button, I should see a record saved dialogue
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    And the immunisation history of the patient should be updated in the patient details page

    Examples:
      | index | nhs_number | site  | care_model | eligibility | assess_date | consent | vaccination | vaccination_date | name | dob   | address  | chosen_vaccine | batch_number | batch_expiry_date |
      | 0 | 9693632109 | ALBERT HOUSE  | Vaccination Centre open to the public | yes | today  | yes  | yes | today   | Bill GARTON |  23/6/1946 |   1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | COVID-19   | SDYY2-01   | 19/10/2025 |
      | 1 | 9693632109 | BECCLES HOUSE | Vaccination centre open to the public | yes | today-1 | yes | yes  | today-1  | Bill GARTON |  23/6/1946 | 1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | COVID-19  | SDYY2-12B | 19/10/2025 |
      | 2 | 9470040228 | BIRCH HOUSE  | Hospital hub for staff and patients | yes  | today-1  | yes | yes | today | HERBERT HAAG | 14/12/1922 | 10 COASTAL ROAD, HEST BANK, LANCASTER, LA2 6HN | COVID-19 |  SB12345-12A  | 19/2/2026 |
      | 3 | 9470057589 | ALBERT HOUSE  | Care home | yes  | today-2 | yes | yes | today-1 | ROGER SEABORNE | 13/12/1922 | 10 ANN STREET, DALTON-IN-FURNESS, CUMBRIA, LA15 8BG | COVID-19  | SDYY2-13A | 19/10/2026 |
      | 4 | 9472710255 | BECCLES HOUSE | Housebound patient's home | yes | today-3 | yes | yes  | today-2 | DELICE PINKER | 10/11/1926 | HARDCRAGG HOUSE, HARDCRAGG WAY, GRANGE-OVER-SANDS, CUMBRIA, LA11 6BH | COVID-19 | SDYY2-14A | 19/10/2026 |
      | 5 | 9473629885 | BIRCH HOUSE | Outreach event | yes | today-4 | yes | yes | today-3 | MARGIE PUCKEY | 27/5/1924 | MANSART COURT, 10 OLIVE SHAPLEY AVENUE, MANCHESTER, M20 6QB | COVID-19 | SDYY2-15A | 19/10/2026 |
      | 6 | 9437540233 | ALBERT HOUSE  | Vaccination Centre | yes | today-5 | yes | yes | today-2 | RANDY FOGDEN | 8/6/1961 | 10 ASHVILLE TERRACE, MANCHESTER, M40 9WG | COVID-19   |  SDYY2-16A | 19/10/2026 |
      | 7 | 9474374228 | BECCLES HOUSE | Hospital hub for staff and patients  | yes  | today-6 | yes | yes | today-3 | ORINDA JUDD | 20/7/1963 | 2 RECTORY PADDOCK, HALTON, LANCASTER, LA2 6LL | COVID-19 | SDYY2-17A | 19/10/2026 |
      | 8 | 9437580812 | BIRCH HOUSE | Care home | yes | today-7 | yes | yes | today-7 | INDIGO CATCHESIDE | 1/3/1959 | 12 CANBERRA STREET, MANCHESTER, M11 4WL | COVID-19 | SDYY2-18A | 19/10/2026 |
      | 9 | 9437599165 | ALBERT HOUSE | Housebound patient's home | yes | today-30 | yes | yes | today-30 | CAWRDAV BOBBETT | 21/7/1959 | 127 ALINORA CRESCENT, GORING-BY-SEA, WORTHING, W SUSSEX, BN12 4HN | COVID-19 | SDYY2-18B | 19/10/2026 |
      | 10 | 9474335052 | BECCLES HOUSE | Outreach event | yes | today-2 | yes | yes | today-2 | AMERY PIGGOTT | 20/4/1968 | 10 CONNAUGHT ROAD, LANCASTER, LA1 4BQ | COVID-19 | SDYY2-18C | 19/10/2026 |
      | 11 | 9437541817 | BIRCH HOUSE | Vaccination Centre | yes  | today-3 | yes | yes | today-1 | FLORINDA DUNNER |  27/3/1957 | 32 HOLLAND ROAD, MANCHESTER, M8 4NP | COVID-19 | SDYY2-18D | 19/10/2026 |
      | 12 | 9437540233 | ALBERT HOUSE  | Hospital hub for staff and patients | yes | today-15 | yes | yes | today-7 | RANDY FOGDEN | 8/6/1961 | 10 ASHVILLE TERRACE, MANCHESTER, M40 9WG | COVID-19 | SDYY2-18E | 19/10/2026 |
      | 8 | 9474376638 | BECCLES HOUSE | Care home | yes | today-32 | yes | yes | today-30 | PHYLLIDA ZYLKO | 6/2/1968 | BELL FARM BUNGALOW, CATON GREEN, BROOKHOUSE, LANCASTER, LA2 9JG      | Flu | SDYY2-18F | 19/10/2026 |
      | 9 | 9474405174 | BIRCH HOUSE   | Housebound patient's home | yes | today | yes | yes | today | PHINEAS FAYLE | 4/9/1965 | 2 DIXON TERRACE, NETHER KELLET, CARNFORTH, LANCS, LA6 1EX | Flu | SDYY2-19A | 19/10/2026 |
      | 10 | 9474405174 | ALBERT HOUSE  | Outreach event | yes | today-2 | yes  | yes | today | PHINEAS FAYLE | 4/9/1965 | 2 DIXON TERRACE, NETHER KELLET, CARNFORTH, LANCS, LA6 1EX | Flu | SDYY2-14B | 5/5/2025 |
      | 11 | 9450134391 | BECCLES HOUSE | Vaccination Centre | yes | today-3 | yes | yes  | today | MARIAN PIESSE | 17/7/1994 | 2 BIRCH STREET, LYTHAM ST. ANNES, LANCS, FY8 5DT | Flu | SDYY2-14C | 19/10/2026 |
      | 12 | 9450140960 | BIRCH HOUSE | Hospital hub for staff and patients | yes | today-1  | yes | yes| today | DEANA GAMBLES | 5/9/1993 | 10 GRASMERE ROAD, LYTHAM ST. ANNES, LANCS, FY8 2HZ | Flu |  SDYY2-20A | 19/10/2026 |
      | 1 | 9450141444 | ALBERT HOUSE  | Care home | yes | today-4 | yes | yes | today-2 | BRANDIE DYBLE | 25/8/1992 | 49 BLACKPOOL ROAD NORTH, LYTHAM ST. ANNES, LANCS, FY8 3DF | Flu  |  SDYY2-21A |        5/5/2025 |
      | 2 | 9450141711 | BECCLES HOUSE | Housebound patient's home | yes | today-2| yes | yes | today-1 | KRISTIA SIDAWAY | 24/6/1992 | 41 BALTIMORE ROAD, LYTHAM ST. ANNES, LANCS, FY8 3NY | Flu | SDYY2-22A | 5/5/2025 |
      | 3 | 9450144699 | BIRCH HOUSE   | Outreach event  | yes | today-1 | yes | yes | today-1 | HOPE TULLY | 10/1/1993 | 2 CHAPEL CLOSE, WESHAM, PRESTON, PR4 3HB | Flu    |  SDYY2-23A | 19/10/2026 |
      | 4 | 9437541817 | ALBERT HOUSE  | Outreach event | yes | today | yes | yes | today | FLORINDA DUNNER |  27/3/1957 | 32 HOLLAND ROAD, MANCHESTER, M8 4NP | Flu | SDYY2-24A | 5/5/2025 |

  @recordvaccine
  Scenario Outline: Record a maternity vaccine with nhs number
    Given I login to RAVS and set vaccinator details with <site> and <care_model> and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <vaccine_type>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <vaccine_type>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the pregnant patient's <eligibility> with the details of due date as <due_date> and assessment date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
    And when I click confirm and save button, I should see a record saved dialogue
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    And the immunisation history of the patient should be updated in the patient details page

    Examples:
      | index | nhs_number | site   | care_model      | eligibility | due_date | assess_date | consent | vaccination | vaccination_date | name  | dob       | address                                             | chosen_vaccine            | vaccine_type | batch_number | batch_expiry_date |
      |  4 | 9473629885 | KINGSTON HOUSE | Outreach event | yes | today+50 | today-4 | yes   | yes | today-3  | MARGIE PUCKEY | 27/5/1924 | MANSART COURT, 10 OLIVE SHAPLEY AVENUE, MANCHESTER, M20 6QB | Respiratory syncytial virus (RSV) | Arexvy | RSVTEST2 |  31/12/2025 |
      # |     0 | 9693632109 | ALBERT HOUSE  | Vaccination Centre | yes | today     | today       | yes     | yes | today    | Bill GARTON   |  23/6/1946 |           1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | Pertussis                 | Adacel vaccine suspension  | ADAC1-27     |        19/10/2027 |
      # |     1 | 9693632109 | BECCLES HOUSE | Vaccination Centre | yes | today+100 | today-1     | yes     | yes | today-1  | Bill GARTON   |  23/6/1946 |           1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | Pertussis                 | Boostrix-IPV suspension    | BST01-28B    |        19/10/2028 |
      # |     2 | 9470040228 | BIRCH HOUSE   | Hospital hub for staff and patients       | yes | today+290 | today-1     | yes     | yes | today    | HERBERT HAAG  | 14/12/1922 |                       10 COASTAL ROAD, HEST BANK, LANCASTER, LA2 6HN | Pertussis                 | Repevax vaccine suspension | REPE11-29A   |         19/2/2029 |
      # |     3 | 9472710255 | ALBERT HOUSE  | Housebound patient's home | yes | today+5   | today-3     | yes     | yes | today-2  | DELICE PINKER | 10/11/1926 | HARDCRAGG HOUSE, HARDCRAGG WAY, GRANGE-OVER-SANDS, CUMBRIA, LA11 6BH | Respiratory syncytial virus (RSV) | Abrysvo            | ABRY2-14A    |        19/10/2026 |
      # |     4 | 9473629885 | BECCLES HOUSE | Outreach event    | yes | today+50  | today-4     | yes     | yes | today-3  | MARGIE PUCKEY |  27/5/1924 | MANSART COURT, 10 OLIVE SHAPLEY AVENUE, MANCHESTER, M20 6QB  | Respiratory syncytial virus (RSV) | Arexvy             | AREX2-15A    |        19/10/2026 |
