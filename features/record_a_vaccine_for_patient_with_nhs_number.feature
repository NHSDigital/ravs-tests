Feature: Record vaccine

@recordvaccine
Scenario Outline: Record a vaccine with nhs number
    Given I login to RAVS and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <vaccine_type>, <batch_number> with <batch_expiry_date>
    And I set the vaccinator details with <site> and <care_model>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <vaccine_type>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details with <dose_amount> and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
    And when I click confirm and save button, the immunisation history of the patient should be updated in the patient details page

Examples:
    | index | nhs_number | site | care_model |  eligibility | assess_date | consent | vaccination | vaccination_date | name | dob | address | chosen_vaccine | vaccine_type | batch_number | batch_expiry_date | dose_amount |
    | 0 | 9693632109 | NEELIMA HOUSE | Vaccination Centre |    yes        | today | yes     | yes  | today | Bill GARTON | 	23/6/1946 | 	1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | COVID-19 | Comirnaty Original/Omicron BA.4-5 | SDYY2-12 | 19/10/2025  | 0.3 |
    | 1 | 9693632109 | NEELIMA HOUSE | Vaccination Centre |   yes        | today | yes     | yes  | today-1 | Bill GARTON | 	23/6/1946 | 	1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | COVID-19 | Comirnaty Original/Omicron BA.4-5 | SDYY2-12 | 19/10/2025  | 0.3 |
    | 2 | 9470040228 | FRAZER HOUSE | Hospital Hub |   yes  | today-1 |  yes     | yes  | today  | HERBERT HAAG | 14/12/1922 | 10 COASTAL ROAD, HEST BANK, LANCASTER, LA2 6HN | COVID-19 | Comirnaty 30 Omicron XBB.1.5 | sb12345-12 | 19/2/2026 | 0.3 |
    | 3 | 9470057589   | NEELIMA HOUSE | Care Home |   yes    | today-2  | yes     | yes  | today-1 | ROGER SEABORNE | 13/12/1922 | 10 ANN STREET, DALTON-IN-FURNESS, CUMBRIA, LA15 8BG |  COVID-19 | Comirnaty 3 Omicron XBB.1.5 | SDYY2-13 | 19/20/2026 | 0.3 |
    | 4 | 9472710255   | NEELIMA HOUSE | Home Of Housebound Patient |   yes     | today-3     | yes     | yes  | today-2 | DELICE PINKER | 	10/11/1926 | HARDCRAGG HOUSE, HARDCRAGG WAY, GRANGE-OVER-SANDS, CUMBRIA, LA11 6BH | COVID-19 | Comirnaty 10 Omicron XBB.1.5 | SDYY2-14 | 19/20/2026 | 0.3 |
    | 5 | 9473629885   | NEELIMA HOUSE | Off-site Outreach Event |   yes    | today-4     | yes     | yes   | today-3 | MARGIE PUCKEY | 	27/5/1924 | 	MANSART COURT, 10 OLIVE SHAPLEY AVENUE, MANCHESTER, M20 6QB | COVID-19 | Spikevax XBB.1.5 | SDYY2-15 | 19/20/2026 | 0.3 |
    | 6 | 9437540233   | FRAZER HOUSE | Vaccination Centre |   yes    | today -5    | yes     | yes  | today-2 | RANDY FOGDEN | 	8/6/1961 | 		10 ASHVILLE TERRACE, MANCHESTER, M40 9WG | COVID-19 | Spikevax XBB.1.5 | SDYY2-16 | 19/20/2026 | 0.3 |
    | 7 | 9474374228  | NEELIMA HOUSE | Hospital Hub |  yes    | today-6    | yes     | yes  | today-3 | ORINDA JUDD | 	20/7/1963 |  2 RECTORY PADDOCK, HALTON, LANCASTER, LA2 6LL | COVID-19 | Spikevax XBB.1.5 | SDYY2-17 | 19/20/2026 | 0.3 |
    | 8 | 9437580812  | NEELIMA HOUSE | Care Home |  yes    | today-7     | yes     | yes  | today-7 | INDIGO CATCHESIDE | 		1/3/1959  |  	12 CANBERRA STREET, MANCHESTER, M11 4WL | COVID-19 | Comirnaty Original/Omicron BA.4-5 | SDYY2-18 | 19/20/2026 | 0.3 |
    | 9 | 9437599165   |  NEELIMA HOUSE | Home Of Housebound Patient  | yes    | today-30    | yes     | yes   | today-30 | CAWRDAV BOBBETT | 			21/7/1959  |  		127 ALINORA CRESCENT, GORING-BY-SEA, WORTHING, W SUSSEX, BN12 4HN | COVID-19 | Comirnaty 30 Omicron XBB.1.5 | SDYY2-18 | 19/20/2026 | 0.5 |
    | 10 | 9474335052 | NEELIMA HOUSE | Off-site Outreach Event |  yes        | yes   | today    | yes  | today | AMERY PIGGOTT | 	20/4/1968  |  10 CONNAUGHT ROAD, LANCASTER, LA1 4BQ | COVID-19 | Comirnaty 3 Omicron XBB.1.5 | SDYY2-18 | 19/20/2026 | 0.3 |
    | 11 | 9437541817 | PAUL TOWERS |  Vaccination Centre |  yes    | today    | yes     | yes  | today | FLORINDA DUNNER | 				27/3/1957  |  32 HOLLAND ROAD, MANCHESTER, M8 4NP | COVID-19 | Comirnaty 10 Omicron XBB.1.5 | SDYY2-18 | 19/20/2026 | 0.5 |
    | 12 | 9437540233  | PAUL TOWERS | Hospital Hub | yes   | today       | yes     | yes   | today | RANDY FOGDEN | 		8/6/1961  |  	10 ASHVILLE TERRACE, MANCHESTER, M40 9WG  | COVID-19 | Spikevax XBB.1.5 | SDYY2-18 | 19/20/2026 | 0.3 |
    | 8 | 9474376638   |  PAUL TOWERS | Care Home | yes    | today      | yes     | yes   | today | PHYLLIDA ZYLKO | 	6/2/1968  |  BELL FARM BUNGALOW, CATON GREEN, BROOKHOUSE, LANCASTER, LA2 9JG | Flu | Fluenz Tetra - LAIV | SDYY2-18 | 19/20/2026 | 0.3 |
    | 9 | 9474405174   |  PAUL TOWERS | Home Of Housebound Patient | yes   | today       | yes     | yes   | today | PHINEAS FAYLE | 	4/9/1965  |  2 DIXON TERRACE, NETHER KELLET, CARNFORTH, LANCS, LA6 1EX | Flu | Fluenz Tetra - LAIV | SDYY2-19 | 19/20/2026 | 0.3 |
    | 10 | 9474405174 |  PAUL TOWERS | Off-site Outreach Event |  yes     | today   | yes    | yes  | today| PHINEAS FAYLE | 	4/9/1965  |  2 DIXON TERRACE, NETHER KELLET, CARNFORTH, LANCS, LA6 1EX | Flu | Quadrivalent Influenza vaccine - QIVe | SDYY2-14 | 19/20/2026 | 0.3 |
    | 11 | 9450134391   |  SCOTT HOSPITAL |  Vaccination Centre | yes  | today     | yes     | yes  | today  | MARIAN PIESSE | 	17/7/1994 |  2 BIRCH STREET, LYTHAM ST. ANNES, LANCS, FY8 5DT | Flu | Quadrivalent Influvac sub-unit Tetra - QIVe | SDYY2-14 | 19/20/2026 | 0.3 |
    | 12 | 9450140960   |  SCOTT HOSPITAL |   Hospital Hub  |  yes  | today    | yes     | yes | today | DEANA GAMBLES | 	5/9/1993 |  10 GRASMERE ROAD, LYTHAM ST. ANNES, LANCS, FY8 2HZ  | Flu | 	Flucelvax Tetra - QIVc | SDYY2-20 | 19/20/2026 |  0.3 |
    | 1 | 9450141444   |  SCOTT HOSPITAL |   Care Home | yes  | today    | yes     | yes  | today | BRANDIE DYBLE | 	25/8/1992 |  	49 BLACKPOOL ROAD NORTH, LYTHAM ST. ANNES, LANCS, FY8 3DF  | Flu | 	Supemtek - QIVr | SDYY2-21 | 19/20/2026 | 0.3 |
    | 2 | 9450141711   |  SCOTT HOSPITAL |  Home Of Housebound Patient | yes  | today    | yes     | yes   | today | KRISTIA SIDAWAY | 	24/6/1992 |  	41 BALTIMORE ROAD, LYTHAM ST. ANNES, LANCS, FY8 3NY  | Flu | 	Fluad Tetra - aQIV | SDYY2-22 | 19/20/2026 | 0.3 |
    | 3 | 9450144699  |  SCOTT HOSPITAL |  Off-site Outreach Event |  yes  | today    | yes     | yes  | today-1 | HOPE TULLY |		10/1/1993 |  	2 CHAPEL CLOSE, WESHAM, PRESTON, PR4 3HB  | Flu | 	Cell-based Quadrivalent - QIVc | SDYY2-23 | 19/20/2026 | 0.3 |
    | 4 | 9437541817   |  FRAZER HOUSE |  Off-site Outreach Event |yes   | today   | yes     | yes | today | FLORINDA DUNNER |	27/3/1957 |  		32 HOLLAND ROAD, MANCHESTER, M8 4NP  | Flu | 	Adjuvanted Quadrivalent - aQIV | SDYY2-24 | 19/20/2026 | 0.3 |

