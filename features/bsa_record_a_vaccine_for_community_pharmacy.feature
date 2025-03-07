Feature: Business services authority (BSA) - Record vaccine for community pharmacies

  @bsarecordvaccine
  Scenario Outline: ADD - NO SUBSITES - Record a vaccine at community pharmacy
    Given I login to RAVS as a community pharmacist to the <site> and set vaccinator details with <site> and <care_model> as community pharmacy and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue

    Examples:
      | index | nhs_number | site  | care_model | eligibility | assess_date | consent | vaccination | vaccination_date | name | dob   | address  | chosen_vaccine | batch_number | batch_expiry_date |
      | 0 | 9693632109 | Leeds Pharmacy  | Outreach event | yes | today  | yes  | yes | today    | Bill GARTON |  23/6/1946 |   1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | COVID-19   | AUTOMATION-SJ1   | 19/10/2026 |
      | 1 | 9732596996 | Leeds Pharmacy  | Vaccination Centre | yes | today  | yes  | yes | today-15   | Lisa WORTHY |  30/6/2024 |   10 NORTON PARK VIEW, SHEFFIELD, S8 8GS  | COVID-19   | AUTOMATION-SJ1   | 19/10/2026 |
      | 2 | 9732743476 | Leeds Pharmacy  | Hospital hub for staff and patients | yes | today  | yes  | yes | today-16   | Mike HEESOM |  24/10/1992 |   2 CHAPEL YARD, BRIGG, S HUMBERSIDE, DN20 8JY | COVID-19   | AUTOMATION-SJ1   | 19/10/2026 |
      | 3 | 9449306494 | Leeds Pharmacy  | Community pharmacy | yes | today  | yes  | yes | today-13   | Reynolds Ryan |  27/03/2001 |   Jamie Street, Jaketown, KDDTG5, SW16 6JR | COVID-19   | AUTOMATION-SJ1   | 19/10/2026 |
      | 11 | 9450134391 | Leeds Pharmacy | Community pharmacy | yes | today-3 | yes | yes  | today-3 | MARIAN PIESSE | 17/7/1994 | 2 BIRCH STREET, LYTHAM ST. ANNES, LANCS, FY8 5DT | Flu | AUTOMATION-QI | 19/10/2026 |
      | 11 | 9450134391 | Leeds Pharmacy | Community pharmacy | yes| today | yes | yes  | today-91 | MARIAN PIESSE | 17/7/1994 | 2 BIRCH STREET, LYTHAM ST. ANNES, LANCS, FY8 5DT | Flu | AUTOMATION-QI | 19/10/2026 |
      | 2 | 9450134391 | Leeds Pharmacy | Community pharmacy | yes| today | yes | yes  | today-92 | MARIAN PIESSE | 17/7/1994 | 2 BIRCH STREET, LYTHAM ST. ANNES, LANCS, FY8 5DT | Flu | AUTOMATION-QI | 19/10/2026 |
      | 11 | 9450134391 | Leeds Pharmacy | Hospital hub for staff and patients | yes | today | yes | yes  | today-89 | MARIAN PIESSE | 17/7/1994 | 2 BIRCH STREET, LYTHAM ST. ANNES, LANCS, FY8 5DT | Flu | AUTOMATION-QI | 19/10/2026 |
      | 12 | 9470011902 | Leeds Pharmacy | Community pharmacy | yes | today | yes | yes  |  today-121 | KATEE TUZZIO | 27/05/2015 | BRIDGE END HOUSE, PARK ROAD, MILNTHORPE, CUMBRIA, LA7 7AN | Flu | AUTOMATION-QI | 19/10/2026 |


  @bsarecordvaccine
  Scenario Outline: ADD PHARMACY WITH SUB SITES - Record a vaccine at community pharmacy
    Given I login to RAVS as a community pharmacist to the <site> and set vaccinator details with <site> and <care_model> as community pharmacy and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <chosen_vaccine_type>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <chosen_vaccine_type>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue

    Examples:
      | index | nhs_number | site  | care_model | eligibility | assess_date | consent | vaccination | vaccination_date | name | dob   | address  | chosen_vaccine | chosen_vaccine_type | batch_number | batch_expiry_date |
      | 0 | 9470006143 | Aspire Pharmacy | Community pharmacy | yes | today | yes | yes  |  today-5 | TABBY FERN | 2202/2022 | CLEAR BECK HOUSE, TATHAM, LANCASTER, LA2 8PJ | Covid-19 | Spikevax JN.1 | AUTO-SJ-AP | 19/10/2026 |
      | 1 | 9732596996 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service  | Vaccination Centre | yes | today  | yes  | yes | today-15   | Lisa WORTHY |  30/6/2024 |  10 NORTON PARK VIEW, SHEFFIELD, S8 8GS  | COVID-19   | Comirnaty 30 JN.1 | AUTO-30-APCSC   | 19/10/2026 |
      | 2 | 9470006739 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Community pharmacy | yes | today | yes | yes  |  today-11 | JANNETTE ARD | 09/12/2015 | 1 ST. MARTINS COURT, CONISTON, CUMBRIA, LA21 8HZ | Covid-19 | Comirnaty 10 JN.1 | AUTO-10-CSC | 19/10/2026 |
      | 3 | 9470032640 | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service | Community pharmacy | yes | today | yes | yes  |  today-3 | SYBIL PELLING | 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Covid-19 | Comirnaty 3 JN.1 | AUTO-3-OM | 19/10/2026 |
      | 4 | 9650594000 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Community pharmacy | yes | today | yes | yes  |  today-60 | Archie STRAIN | 30/07/2014 | 1 CONINGSBY DRIVE, GRIMSBY, S HUMBERSIDE, DN34 5HQ | Flu | Quadrivalent Influenza Vaccine (QIVe) | AUTO-QIVE-CSC | 19/10/2026 |
      | 5 | 9732743476 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Community pharmacy | yes | today | yes | yes  |  today-3 | Mike HEESOM  | 24/10/1992 | 2 CHAPEL YARD, BRIGG, S HUMBERSIDE, DN20 8JY  | Flu | Cell-based Quadrivalent Influenza Vaccine (QIVc) | AUTO-QIVC-CSC | 19/10/2026 |
      | 6 | 9449303762 | Aspire Pharmacy | Community pharmacy | yes | today | yes | yes  |  today-5 | Pryderi Warnford-Davis | 14/04/2001 | 1 CRANLEIGH ROAD, ESHER, SURREY, KT10 8DF | Flu | Adjuvanted Quadrivalent Influenza Vaccine (aQIV) | AUTO-QIV-AP | 19/10/2026 |
      | 7 | 9470011902 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Community pharmacy | yes | today | yes | yes  |  today-2 | KATEE TUZZIO | 27/05/2015 | BRIDGE END HOUSE, PARK ROAD, MILNTHORPE, CUMBRIA, LA7 7AN | Flu | Fluenz (LAIV) | AUTO-F-CSC | 19/10/2026 |
      | 8 | 9650594000 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Community pharmacy | yes | today | yes | yes  |  today-12 | Archie STRAIN | 30/07/2014 | 1 CONINGSBY DRIVE, GRIMSBY, S HUMBERSIDE, DN34 5HQ | Flu | Influenza Tetra MYL (QIVe)  | AUTO-ITM-CSC | 19/10/2026 |
      | 9 | 9470032640 | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service | Community pharmacy | yes | today | yes | yes  |  today-14 | SYBIL PELLING | 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Quadrivalent Influenza Vaccine – High Dose (QIV-HD) | AUTO-QIHD-OM | 19/10/2026 |


  @bsarecordvaccine
  Scenario Outline: DELETE - PHARMACY WITH SUB SITES - Record a vaccine at community pharmacy
    Given I login to RAVS as a community pharmacist to the <site> and set vaccinator details with <site> and <care_model> as community pharmacy and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <chosen_vaccine_type>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <chosen_vaccine_type>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    And the immunisation history of the patient should be updated in the patient details page

    Examples:
      | index | nhs_number | site  | care_model | eligibility | assess_date | consent | vaccination | vaccination_date | name | dob   | address  | chosen_vaccine | chosen_vaccine_type | batch_number | batch_expiry_date |
      | 0 | 9470006143 | Aspire Pharmacy | Community pharmacy | yes | today | yes | yes  |  today-5 | TABBY FERN | 2202/2022 | CLEAR BECK HOUSE, TATHAM, LANCASTER, LA2 8PJ | Covid-19 | Spikevax JN.1 | AUTO-SJ-AP | 19/10/2026 |
      | 9 | 9470032640 | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service | Community pharmacy | yes | today | yes | yes  |  today-14 | SYBIL PELLING | 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Quadrivalent Influenza Vaccine – High Dose (QIV-HD) | AUTO-QIHD-OM | 19/10/2026 |

@bsarecordvaccine
  Scenario Outline: SFLAG - Record a vaccine at community pharmacy
    Given I login to RAVS as a community pharmacist to the <site> and set vaccinator details with <site> and <care_model> as community pharmacy and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient <name>, <dob> and vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue

    Examples:
      | index | nhs_number | site  | care_model | eligibility | assess_date | consent | vaccination | vaccination_date | name | dob   |  chosen_vaccine | batch_number | batch_expiry_date |
      | 0 | 9733907723 | Aspire Pharmacy  | Outreach event | yes | today  | yes  | yes | today-14    | Sandra Ryan |  7/4/1994 | COVID-19   | AUTO-C-SFLAG   | 19/10/2026 |
      | 1 | 9733907723 | Leeds Pharmacy  | Vaccination Centre | yes | today  | yes  | yes | today-30  |Sandra Ryan |  7/4/1994 | Flu  | AUTO-F-SFLAG   | 19/10/2026 |

@bsarecordvaccine
  Scenario Outline: SUPERSEDED NEW - Record a vaccine at community pharmacy
    Given I login to RAVS as a community pharmacist to the <site> and set vaccinator details with <site> and <care_model> as community pharmacy and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue

    Examples:
      | index | nhs_number | site  | care_model | eligibility | assess_date | consent | vaccination | vaccination_date | name | dob   | address |  chosen_vaccine | batch_number | batch_expiry_date |
      | 0 | 9467361590 | Leeds Pharmacy  | Outreach event | yes | today  | yes  | yes | today-9  | WALLIS ADEYEMO |  19/4/2015 |	1 MIDLAND ROAD, LEEDS, LS6 1BQ | COVID-19   | AUTO-SUP-C-1   | 19/10/2026 |
      | 1 | 3508118053 | Leeds Pharmacy  | Outreach event | yes | today  | yes  | yes | today-9  | WALLIS ADEYEMO |  19/4/2015 | 	1 MIDLAND ROAD, LEEDS, LS6 1BQ |COVID-19   | AUTO-SUPER-C-1   | 19/10/2026 |
      | 2 | 9734250221 | Leeds Pharmacy  | Vaccination Centre | yes | today  | yes  | yes | today-30  | BARAK SELIGMANN |  26/5/2016 | 170 WEELSBY ROAD, GRIMSBY, S HUMBERSIDE, DN32 8QQ | Flu  | AUTO-SUP-N-F  | 19/10/2026 |

@bsarecordvaccine
  Scenario Outline: SUPERSEDED OLD - Record a vaccine at community pharmacy
    Given I login to RAVS as a community pharmacist to the <site> and set vaccinator details with <site> and <care_model> as community pharmacy and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue

    Examples:
      | index | nhs_number | site  | care_model | eligibility | assess_date | consent | vaccination | vaccination_date | name | chosen_vaccine | batch_number | batch_expiry_date |
      | 2 | 9449304033 | Leeds Pharmacy  | Vaccination Centre | yes | today  | yes  | yes | today-30  | BARAK SELIGMANN |  Flu  | AUTO-SUP-O-F   | 19/10/2026 |
      | 3 | 9449304033 | Aspire Pharmacy  | Vaccination Centre | yes | today  | yes  | yes | today-5  | BARAK SELIGMANN |  Covid-19  | AUTO-SUP-O-C | 19/10/2026 |

@bsarecordvaccine
  Scenario Outline: DECEASED - Record a vaccine at community pharmacy
    Given I login to RAVS as a community pharmacist to the <site> and set vaccinator details with <site> and <care_model> as community pharmacy and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue

    Examples:
      | index | nhs_number | site  | care_model | eligibility | assess_date | consent | vaccination | vaccination_date | name | dob   | address |  chosen_vaccine | batch_number | batch_expiry_date |
      | 0 | 9449304424 | Leeds Pharmacy  | Outreach event | yes | today  | yes  | yes | today-9    | John Test |  2/1/1997 |	121C, Durants Road, ENFIELD, EN3 7DG | COVID-19   | AUTO-DEC-SJ1   | 19/10/2026 |
      | 0 | 9449304424 | Aspire Pharmacy  | Outreach event | yes | today  | yes  | yes | today-9    | John Test |  2/1/1997 |	121C, Durants Road, ENFIELD, EN3 7DG | Flu   | AUTO-DEC-F-SJ1   | 19/10/2026 |

@bsarecordvaccine
  Scenario Outline: LOCAL - Record a vaccine at community pharmacy
    Given I login to RAVS as a community pharmacist to the <site> and set vaccinator details with <site> and <care_model> as community pharmacy and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I create a random patient locally
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue

    Examples:
      | index | site  | care_model | eligibility | assess_date | consent | vaccination | vaccination_date | chosen_vaccine | batch_number | batch_expiry_date |
      | 0 |  Leeds Pharmacy  | Outreach event | yes | today  | yes  | yes | today    |  COVID-19   | AUTO-LOCAL-C  | 19/10/2026 |
      | 1 |  Leeds Pharmacy  | Vaccination Centre | yes | today  | yes  | yes | today    | Flu     | AUTO-LOCAL-F  | 19/10/2026 |

  @bsarecordvaccine
  Scenario Outline: MATERNITY NO SUB SITES - Record a maternity vaccine at community pharmacy with nhs number - Add and delete
    Given I login to RAVS as a community pharmacist to the <site> and set vaccinator details with <site> and <care_model> as community pharmacy and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the pregnant patient's <eligibility> with the details of due date as <due_date> and assessment date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue

    Examples:
      | index | nhs_number | site   | care_model      | eligibility | due_date | assess_date | consent | vaccination | vaccination_date | name  | dob    | address     | chosen_vaccine  | batch_number | batch_expiry_date |
      |  4 | 9473629885 | Leeds Pharmacy | Outreach event | yes | today+50 | today-4 | yes | yes | today-3 | MARGIE PUCKEY | 27/5/1924 | MANSART COURT, 10 OLIVE SHAPLEY AVENUE, MANCHESTER, M20 6QB | Respiratory syncytial virus (RSV) | 	AUTOMATION-ABR | 1/2/2026 |
      | 0 | 9470004272 | Leeds Pharmacy | Vaccination Centre | yes | today | today | yes | yes | today | JOJO LANE | 06/07/2015 | 10 RAKESMOOR LANE, BARROW-IN-FURNESS, LA14 4LG  | Pertussis | AUTOMATION-AVS | 19/10/2027 |
      | 1 | 9469998626 | Leeds Pharmacy | Vaccination Centre | yes | today+100 | today-1 | yes | yes | today-1  | JONNY CONOPO | 05/03/2015 | 1 DAISY BANK, LANCASTER, LA1 3JW | Pertussis |  AUTOMATION-BIS | 19/10/2028 |
      | 2 | 9470040228 | Leeds Pharmacy | Hospital hub for staff and patients | yes | today+290 | today-1 | yes | yes | today  | HERBERT HAAG  | 14/12/1922 | 10 COASTAL ROAD, HEST BANK, LANCASTER, LA2 6HN | Pertussis | AUTOMATION-RVS | 19/02/2029 |
      | 3 | 9472710255 | Leeds Pharmacy  | Housebound patient's home | yes | today+5 | today-3 | yes | yes | today-2 | DELICE PINKER | 10/11/1926 | HARDCRAGG HOUSE, HARDCRAGG WAY, GRANGE-OVER-SANDS, CUMBRIA, LA11 6BH | Respiratory syncytial virus (RSV) |  AUTOMATION-ARX | 19/10/2026 |
      # | 4 | 9473629885 | BECCLES HOUSE | Outreach event | yes | today+50 | today-4 | yes | yes | today-3  | MARGIE PUCKEY |  27/5/1924 | MANSART COURT, 10 OLIVE SHAPLEY AVENUE, MANCHESTER, M20 6QB | Respiratory syncytial virus (RSV) |  AREX2-15A | 19/10/2026 |   - # This test is no longer needed as Arexvy has been decommissioned on 29th Nov 2024


# @bsarecordvaccine
#   Scenario Outline: NO SUB SITES - Record a vaccine at community pharmacy - Add and edit
#     Given I login to RAVS as a community pharmacist to the <site> and set vaccinator details with <site> and <care_model> as community pharmacy and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
#     And I search for a patient with the NHS number in the find a patient screen
#     And I open the patient record by clicking on patient <name>
#     When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
#     And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
#     And I record <consent> with the details and click continue to vaccinate button
#     And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
#     Then I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
#     And I click confirm and save button, I should see a record saved dialogue

#     Examples:
#       | index | nhs_number | site  | care_model | eligibility | assess_date | consent | vaccination | vaccination_date | name | dob   | address  | chosen_vaccine | batch_number | batch_expiry_date |
#       | 12 | 9470011902 | Leeds Pharmacy | Community pharmacy | yes | today | yes | yes  |  today-121 | KATEE TUZZIO | 27/05/2015 | BRIDGE END HOUSE, PARK ROAD, MILNTHORPE, CUMBRIA, LA7 7AN | COVID-19 | AUTO-C-QI | 19/10/2026 |
#       | 12 | 9470011902 | Leeds Pharmacy | Community pharmacy | yes | today | yes | yes  |  today-121 | KATEE TUZZIO | 27/05/2015 | BRIDGE END HOUSE, PARK ROAD, MILNTHORPE, CUMBRIA, LA7 7AN | Flu | AUTOMATION-F-QI | 19/10/2026 |

# @bsarecordvaccine
#   Scenario Outline: NO SUB SITES - Record a vaccine at community pharmacy - Add and edit
#     Given I login to RAVS as a community pharmacist to the <site> and set vaccinator details with <site> and <care_model> as community pharmacy and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
#     And I search for a patient with the NHS number in the find a patient screen
#     And I open the patient record by clicking on patient <name>
#     When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
#     And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
#     And I record <consent> with the details and click continue to vaccinate button
#     And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
#     Then I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
#     And I click confirm and save button, I should see a record saved dialogue

#     Examples:
#       | index | nhs_number | site  | care_model | eligibility | assess_date | consent | vaccination | vaccination_date | name | dob   | address  | chosen_vaccine | batch_number | batch_expiry_date |
#       | 12 | 9470011902 | Leeds Pharmacy | Community pharmacy | yes | today | yes | yes  |  today-121 | KATEE TUZZIO | 27/05/2015 | BRIDGE END HOUSE, PARK ROAD, MILNTHORPE, CUMBRIA, LA7 7AN | Flu | AUTO-QI | 19/10/2026 |

@bsarecordvaccine
Scenario Outline: NO - Record a vaccine and choose no vaccination decision on the last screen in a community pharmacy
    Given I login to RAVS as a community pharmacist to the <site> and set vaccinator details with <site> and <care_model> as community pharmacy and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    And I see the patient's address <address> and gender <gender>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Save and return button

  Examples:
    | index | nhs_number | site | care_model | eligibility | assess_date | consent | vaccination | vaccination_date | name    | dob        | address    | chosen_vaccine | batch_number     | batch_expiry_date |  gender |
    | 4 | 9437541817 | Leeds Pharmacy  | Outreach event | yes | today | yes | no | today | FLORINDA DUNNER |  27/03/1957 | 32 HOLLAND ROAD, MANCHESTER, M8 4NP | Flu | AUTO-NO-F-SJ1 | 19/10/2026 | female |
    | 0 | 9469997956 | Leeds Pharmacy  | Outreach event | yes | today  | yes  | no | today  | SOLOMON DAZLEY  |  30/01/2016 |   10 BROOK STREET, LANCASTER, LA1 1SL | COVID-19   | AUTO-NO-C-SJ1   | 19/10/2026 | male |
    | 4 | 9437541817 | Leeds Pharmacy  | Outreach event | no | today | yes | no | today | FLORINDA DUNNER |  27/03/1957 | 32 HOLLAND ROAD, MANCHESTER, M8 4NP | Flu | AUTO-NO-F-SJ1 | 19/10/2026 | female |
    | 0 | 9469997956 | Leeds Pharmacy  | Outreach event | no | today  | yes  | no | today  | SOLOMON DAZLEY  |  30/01/2016 |   10 BROOK STREET, LANCASTER, LA1 1SL | COVID-19   | AUTO-NO-C-SJ1   | 19/10/2026 | male |
    | 4 | 9437541817 | Leeds Pharmacy  | Outreach event | yes | today | no | no | today | FLORINDA DUNNER |  27/03/1957 | 32 HOLLAND ROAD, MANCHESTER, M8 4NP | Flu | AUTO-NO-F-SJ1 | 19/10/2026 | female |
    | 0 | 9469997956 | Leeds Pharmacy  | Outreach event | yes | today  | no  | no | today  | SOLOMON DAZLEY  |  30/01/2016 |   10 BROOK STREET, LANCASTER, LA1 1SL | COVID-19   | AUTO-NO-C-SJ1   | 19/10/2026 | male |

@bsarecordvaccine
  Scenario Outline: NO MATERNITY - Record a maternity vaccine and choose no vaccination decision on the last screen in a community pharmacy
    Given I login to RAVS as a community pharmacist to the <site> and set vaccinator details with <site> and <care_model> as community pharmacy and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the pregnant patient's <eligibility> with the details of due date as <due_date> and assessment date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Save and return button

    Examples:
      | index | nhs_number | site   | care_model      | eligibility | due_date | assess_date | consent | vaccination | vaccination_date | name  | dob    | address     | chosen_vaccine  | batch_number | batch_expiry_date |
      |  4 | 9473629885 | Leeds Pharmacy | Outreach event | yes | today+50 | today-4 | yes | no | today-3 | MARGIE PUCKEY | 27/5/1924 | MANSART COURT, 10 OLIVE SHAPLEY AVENUE, MANCHESTER, M20 6QB | Respiratory syncytial virus (RSV) | 	AUTO-ABR | 1/2/2026 |
      | 2 | 9470040228 | Leeds Pharmacy | Hospital hub for staff and patients | yes | today+290 | today-1 | yes | no | today  | HERBERT HAAG  | 14/12/1922 | 10 COASTAL ROAD, HEST BANK, LANCASTER, LA2 6HN | Pertussis | AUTO-RVS | 19/2/2029 |

  # @bsarecordvaccine
  # Scenario Outline: Record a vaccine at community pharmacy - Edit
  #   Given I login to RAVS as a community pharmacist to the <site> and set vaccinator details with <site> and <care_model> as community pharmacy and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
  #   And I search for a patient with the NHS number in the find a patient screen
  #   And I open the patient record by clicking on patient <name>
  #   When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
  #   And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
  #   And I record <consent> with the details and click continue to vaccinate button
  #   And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
  #   Then I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
  #   And I click confirm and save button, I should see a record saved dialogue

  #   Examples:
  #     | index | nhs_number | site  | care_model | eligibility | assess_date | consent | vaccination | vaccination_date | name | dob   | address  | chosen_vaccine | batch_number | batch_expiry_date |
  #     | 0 | 9693632109 | Leeds Pharmacy  | Outreach event | yes | today  | yes  | yes | today    | Bill GARTON |  23/6/1946 |   1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | COVID-19   | AUTOMATION-SJ1   | 19/10/2026 |

  @bsarecordvaccine
  Scenario Outline: AGE BASED WARNINGS - Display warning based on age when recording a vaccine at community pharmacy
    Given I login to RAVS as a community pharmacist to the <site>
    When I search for the patient with NHS number <nhs_number>
    And I proceed to record a vaccine for <vaccine_type> for all products
    Then the system should display the warnings <expected_warning_count>

    Examples:
      | nhs_number  | expected_warning_count    | vaccine_type | site               |
      | 9732091169  | 3                         | covid          | Leeds Pharmacy   |
      | 9692237893  | 3                         | covid          | Aspire Pharmacy  |
      | 9474335761  | 3                         | covid          | Aspire Pharmacy  |
      | 9450153485  | 3                         | covid          | Leeds Pharmacy   |
      | 9470472918  | 3                         | covid          | Leeds Pharmacy   |
      | 9473673388  | 2                         | covid          | Leeds Pharmacy   |
