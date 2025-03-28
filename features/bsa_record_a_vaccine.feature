Feature: Business services authority (BSA) - Record vaccine

Background:
  Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>

  @bsarecordvaccine
  Scenario Outline: ADD - BSA Record a vaccine at community pharmacy (with and without sub sites) and branch surgery
    Given I set vaccinator details with <site> and set vaccinator details with <site> and <vaccination_location> and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <chosen_vaccine_type>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <chosen_vaccine_type>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue

  Examples:
  | index | nhs_number | site    | vaccination_location     | eligibility | assess_date | consent | vaccination | vaccination_date | name     | dob | address    | chosen_vaccine | chosen_vaccine_type    | batch_number     | batch_expiry_date | gender | user_role    | care_model |
  | 0     | 9470006143 | Leeds Pharmacy     | GP clinic   |yes  | today| yes     | yes  | today| TABBY FERN   | 22/02/2022 | CLEAR BECK HOUSE, TATHAM, LANCASTER, LA2 8PJ | Covid-19 | Spikevax JN.1   | AUTO-SJ-AP| 19/10/2026 | female | lead administrator | community pharmacy |
  | 0     | 9470006143 | Aspire Pharmacy  | GP clinic   |yes  | today| yes     | yes  | today-14   | TABBY FERN   | 22/02/2022 | CLEAR BECK HOUSE, TATHAM, LANCASTER, LA2 8PJ | Covid-19 | Comirnaty 3 JN.1   | AUTO-SJ-AP | 19/10/2026 | female | administrator | community pharmacy |
  | 1     | 9732596996 | Aire Valley Surgery (rawdon) | Vaccination Centre  | yes  | today| yes     | yes  | today-5  | Lisa WORTHY  | 30/6/2024  | 10 NORTON PARK VIEW, SHEFFIELD, S8 8GS      | COVID-19 | Comirnaty 30 JN.1|AUTO-30-APCSC    | 19/10/2026 | male   | recorder | branch surgery |
  | 2     | 9470006739 | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service|GP clinic   |yes  | today| yes     | yes  | today-30  | JANNETTE ARD | 09/12/2015 | 1 ST. MARTINS COURT, CONISTON, CUMBRIA, LA21 8HZ | Covid-19 | Comirnaty 10 JN.1  |AUTO-10-CSC      | 19/10/2026 | female | lead administrator | community pharmacy |
  # | 3     | 9470032640 | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service | GP clinic   |yes  | today| yes     | yes  | today-3    | SYBIL PELLING| 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Quadrivalent Influenza Vaccine – High Dose (QIV-HD)    | AUTO-QIHD-OM     | 19/10/2026 | male   | administrator | community pharmacy |
  # | 4     | 9650594000 | Aire Valley Surgery (rawdon) | GP clinic   |yes  | today| yes     | yes  | today-60   | Archie STRAIN| 30/07/2014 | 1 CONINGSBY DRIVE, GRIMSBY, S HUMBERSIDE, DN34 5HQ | Flu | Quadrivalent Influenza Vaccine (QIVe)| AUTO-QIVE-CSC    | 19/10/2026 | male   | lead administrator | branch surgery   |
  # | 5     | 9449303762 | Aire Valley Surgery (rawdon) | GP clinic   |yes  | today| yes     | yes  | today-5    | Pryderi Warnford-Davis | 14/04/2001 | 1 CRANLEIGH ROAD, ESHER, SURREY, KT10 8DF     | Flu | Adjuvanted Quadrivalent Influenza Vaccine (aQIV)  | AUTO-QIV-AP      | 19/10/2026 | female | administrator | branch surgery   |
  # | 6     | 9470011902 | Aire Valley Surgery (rawdon) | GP clinic   |yes  | today| yes     | yes  | today-12   | Katee TUZZIO | 27/05/2015 | BRIDGE END HOUSE, PARK ROAD, MILNTHORPE, CUMBRIA, LA7 7AN | Flu | Fluenz (LAIV)   |AUTO-F-CSC| 19/10/2026 | female | administrator | branch surgery   |
  | 7     | 9732743476 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | GP clinic | yes  | today| yes     | yes  | today-100  | Mike HEESOM  | 24/10/1992 | 2 CHAPEL YARD, BRIGG, S HUMBERSIDE, DN20 8JY   | Flu | Cell-based Quadrivalent Influenza Vaccine (QIVc)  | AUTO-QIVC-CSC    | 19/10/2026 | male   | recorder | community pharmacy |
  # | 8     | 9650594000 | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service|GP clinic   |yes  | today| yes     | yes  | today-200  | Archie STRAIN| 30/07/2014 | 1 CONINGSBY DRIVE, GRIMSBY, S HUMBERSIDE, DN34 5HQ | Flu | Quadrivalent Influenza Vaccine – High Dose (QIV-HD) | AUTO-QIHD-OM     | 19/10/2026 | female | lead administrator | community pharmacy |
  | 9     | 9470032640 | Aire Valley Surgery (rawdon)  | GP clinic   |yes  | today| yes     | yes  | today-12   | SYBIL PELLING | 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Quadrivalent Influenza Vaccine – High Dose (QIV-HD)    | AUTO-QIHD-OM     | 19/10/2026 | male   | administrator | branch surgery   |
  | 10    | 9470011902 | Aspire Pharmacy|GP clinic   |yes  | today| yes     | yes  | today  | KATEE TUZZIO | 27/05/2015 | BRIDGE END HOUSE, PARK ROAD, MILNTHORPE, CUMBRIA, LA7 7AN | Flu | Quadrivalent Influenza Vaccine (QIVe)| AUTO-QIVE-CSC    | 19/10/2026 | female | administrator | community pharmacy |
  | 11    | 9470032640 | Aire Valley Surgery (rawdon) | GP clinic   |yes  | today| yes     | yes  | today-5  | SYBIL PELLING| 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Influenza Tetra MYL (QIVe)| AUTO-ITM-CSC     | 19/10/2026 | male   | lead administrator | branch surgery   |
  # | 12    | 9470032640 | Aire Valley Surgery (rawdon) | GP clinic   |yes  | today| yes     | yes  | today-100  | SYBIL PELLING| 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Influenza Tetra MYL (QIVe)| AUTO-ITM-CSC     | 19/10/2026 | male   | lead administrator | branch surgery   |
  # | 12    | 9470032640 | Aire Valley Surgery (rawdon) | GP clinic   |yes  | today| yes     | yes  | today-5  | SYBIL PELLING| 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Influenza Tetra MYL (QIVe)| AUTO-ITM-CSC     | 19/10/2026 | male   | administrator | branch surgery   |

  @bsarecordvaccine
  Scenario Outline: DELETE - BSA Record a vaccine
    Given I set vaccinator details with <site> and set vaccinator details with <site> and <vaccination_location> and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <chosen_vaccine_type>, <batch_number> with <batch_expiry_date>
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
    | index | nhs_number | site    | vaccination_location     | eligibility | assess_date | consent | vaccination | vaccination_date | name     | dob | address    | chosen_vaccine | chosen_vaccine_type    | batch_number     | batch_expiry_date | gender | user_role    | care_model |
    # | 0     | 9470006143 | Leeds Pharmacy     | GP clinic   | yes  | today| yes     | yes  | today | TABBY FERN   | 22/02/2022 | CLEAR BECK HOUSE, TATHAM, LANCASTER, LA2 8PJ | Covid-19 | Spikevax JN.1   |AUTO-SJ-AP| 19/10/2026 | female | lead administrator | community pharmacy |
    | 0     | 9470006143 | Aspire Pharmacy |GP clinic   |yes  | today| yes     | yes  | today   | TABBY FERN   | 22/02/2022 | CLEAR BECK HOUSE, TATHAM, LANCASTER, LA2 8PJ | Covid-19 | Spikevax JN.1   |AUTO-SJ-AP| 19/10/2026 | female | administrator | community pharmacy |
    | 1     | 9732596996 | Leeds Pharmacy |Vaccination Centre  | yes  | today| yes     | yes  | today-20  | Lisa WORTHY  | 30/6/2024  | 10 NORTON PARK VIEW, SHEFFIELD, S8 8GS      | COVID-19 | Comirnaty 30 JN.1 |AUTO-30-APCSC    | 19/10/2026 | male   | recorder | community pharmacy |
    | 2     | 9470006739 | Aspire Pharmacy |GP clinic   |yes  | today| yes     | yes  | today-7  | JANNETTE ARD | 09/12/2015 | 1 ST. MARTINS COURT, CONISTON, CUMBRIA, LA21 8HZ | Covid-19 | Comirnaty 10 JN.1      |AUTO-10-CSC      | 19/10/2026 | female | lead administrator | community pharmacy |
    | 3     | 9470006739 | Aspire Pharmacy |GP clinic   |yes  | today| yes     | yes  | today-3  | JANNETTE ARD | 09/12/2015 | 1 ST. MARTINS COURT, CONISTON, CUMBRIA, LA21 8HZ | Covid-19 | Comirnaty 3 JN.1      |AUTO-10-CSC      | 19/10/2026 | female | lead administrator | community pharmacy |
    | 4     | 9470032640 | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service | GP clinic   |yes  | today| yes     | yes  | today-3    | SYBIL PELLING| 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Quadrivalent Influenza Vaccine – High Dose (QIV-HD)    | AUTO-QIHD-OM     | 19/10/2026 | male   | administrator | community pharmacy |
    | 5     | 9650594000 | Aire Valley Surgery (rawdon) | GP clinic   |yes  | today| yes     | yes  | today-60   | Archie STRAIN| 30/07/2014 | 1 CONINGSBY DRIVE, GRIMSBY, S HUMBERSIDE, DN34 5HQ | Flu | Quadrivalent Influenza Vaccine (QIVe)| AUTO-QIVE-CSC    | 19/10/2026 | male   | lead administrator | branch surgery   |
    | 6     | 9449303762 | Aire Valley Surgery (rawdon) | GP clinic   |yes  | today| yes     | yes  | today-5    | Pryderi Warnford-Davis | 14/04/2001 | 1 CRANLEIGH ROAD, ESHER, SURREY, KT10 8DF     | Flu | Adjuvanted Quadrivalent Influenza Vaccine (aQIV)  | AUTO-QIV-AP      | 19/10/2026 | female | administrator | branch surgery   |
    | 7     | 9470011902 | Aire Valley Surgery (rawdon) | GP clinic   |yes  | today| yes     | yes  | today-2   | Katee TUZZIO | 27/05/2015 | BRIDGE END HOUSE, PARK ROAD, MILNTHORPE, CUMBRIA, LA7 7AN | Flu | Fluenz (LAIV)   |AUTO-F-CSC| 19/10/2026 | female | administrator | branch surgery   |
    # | 7     | 9732743476 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | GP clinic | yes  | today| yes     | yes  | today-100  | Mike HEESOM  | 24/10/1992 | 2 CHAPEL YARD, BRIGG, S HUMBERSIDE, DN20 8JY   | Flu | Cell-based Quadrivalent Influenza Vaccine (QIVc)  | AUTO-QIVC-CSC    | 19/10/2026 | male   | recorder | community pharmacy |
    # | 8     | 9650594000 | Aspire Pharmacy|GP clinic   |yes  | today| yes     | yes  | today-200  | Archie STRAIN| 30/07/2014 | 1 CONINGSBY DRIVE, GRIMSBY, S HUMBERSIDE, DN34 5HQ | Flu | Quadrivalent Influenza Vaccine – High Dose (QIV-HD) | AUTO-QIHD-OM     | 19/10/2026 | female | lead administrator | community pharmacy |
    # | 9     | 9470032640 | Aire Valley Surgery (rawdon) | GP clinic   |yes  | today| yes     | yes  | today-12   | SYBIL PELLING| 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Quadrivalent Influenza Vaccine – High Dose (QIV-HD)    | AUTO-QIHD-OM     | 19/10/2026 | male   | administrator | branch surgery   |
    # | 10    | 9470011902 | Aspire Pharmacy|GP clinic   |yes  | today| yes     | yes  | today-121  | KATEE TUZZIO | 27/05/2015 | BRIDGE END HOUSE, PARK ROAD, MILNTHORPE, CUMBRIA, LA7 7AN | Flu | Quadrivalent Influenza Vaccine (QIVe)| AUTO-QIVE-CSC    | 19/10/2026 | female | administrator | community pharmacy |
    # | 11    | 9470032640 | Aire Valley Surgery (rawdon) | GP clinic   |yes  | today| yes     | yes  | today-365  | SYBIL PELLING | 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Influenza Tetra MYL (QIVe)| AUTO-ITM-4CSC     | 19/10/2026 | male   | lead administrator | branch surgery   |
    # | 12    | 9470032640 | Aire Valley Surgery (rawdon) | GP clinic   |yes  | today| yes     | yes  | today-100  | SYBIL PELLING| 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Influenza Tetra MYL (QIVe)| AUTO-ITM-CSC     | 19/10/2026 | male   | lead administrator | branch surgery   |
    # | 12    | 9470032640 | Aire Valley Surgery (rawdon) | GP clinic   |yes  | today| yes     | yes  | today-5  | SYBIL PELLING| 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Influenza Tetra MYL (QIVe)| AUTO-ITM-CSC     | 19/10/2026 | male   | administrator | branch surgery   |

@bsarecordvaccine
  Scenario Outline: SFLAG - BSA Record a vaccine
    Given I set vaccinator details with <site> and set vaccinator details with <site> and <vaccination_location> and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient <name>, <dob> and vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue

  Examples:
      | index | nhs_number | site  |vaccination_location  | eligibility | assess_date | consent | vaccination | vaccination_date | name   | dob | chosen_vaccine | batch_number    | batch_expiry_date | user_role| care_model |
      | 0     | 9733907723 | Aire Valley Surgery (rawdon)  |Outreach event   | yes  | today| yes     | yes  | today-14   | Sandra Ryan   | 07/04/1994 | COVID-19 | AUTO-C-SFLAG    | 19/10/2026| administrator    | Branch Surgery    |
      | 1     | 9733907723 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre     | yes  | today| yes     | yes  | today-5   | Sandra Ryan   | 07/04/1994 | Flu | AUTO-F-SFLAG    | 19/10/2026| lead administrator| Community Pharmacy |
      # | 2     | 9450127077 | Leeds Pharmacy   | GP clinic   | yes  | today| yes     | yes  | today-200  | LUDMILLA MCKSN-PDS-ALPHA-SENSITIVE   | 2/5/1974 | COVID-19 | AUTO-SJ-AP      | 19/10/2026| recorder  | Community Pharmacy    |
      # | 3     | 9450127077 | Aire Valley Surgery (rawdon)  |Vaccination Centre     | yes  | today| yes     | yes  | today-60   | LUDMILLA MCKSN-PDS-ALPHA-SENSITIVE   | 2/5/1974 | Flu | AUTO-QIVC-CSC   | 19/10/2026| lead administrator| Branch Surgery    |
      # | 4     | 9733907723 | Aspire Pharmacy   |Outreach event   | yes  | today| yes     | yes  | today-90   | Sandra Ryan   | 07/04/1994 | COVID-19 | AUTO-30-APCSC   | 19/10/2026| administrator    | Community Pharmacy |
      # | 5     | 9733907723 | Leeds Pharmacy   | GP clinic   | yes  | today| yes     | yes  | today-120  | Sandra Ryan   | 07/04/1994 | Flu | AUTO-QIHD-OM    | 19/10/2026| recorder  | Community Pharmacy    |
      # | 6     | 9450127077 | Aspire Pharmacy   | GP clinic   | yes  | today| yes     | yes  | today-100  | LUDMILLA MCKSN-PDS-ALPHA-SENSITIVE   | 2/5/1974 | COVID-19 | AUTO-SJ-AP      | 19/10/2026| lead administrator| Community Pharmacy |
      # | 7     | 9733907723 | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service | Outreach event   | yes  | today| yes     | yes  | today-5    | Sandra Ryan    | 7/4/1994    | Flu | AUTO-QIVE-CSC   | 19/10/2026| recorder  | Community Pharmacy |
      # | 8     | 9450127077 | Leeds Pharmacy   |GP clinic   | yes  | today| yes     | yes  | today-14   | LUDMILLA MCKSN-PDS-ALPHA-SENSITIVE   | 2/5/1974 |  Flu | AUTO-QIVC-CSC   | 19/10/2026| administrator    | Community Pharmacy    |
      # | 9     | 9450127077 | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service | Vaccination Centre     | yes  | today| yes     | yes  | today-30   | LUDMILLA MCKSN-PDS-ALPHA-SENSITIVE   | 2/5/1974 |  COVID-19 | AUTO-QIV-HD-OM  | 19/10/2026| lead administrator| Community Pharmacy |
      # | 10    | 9450127077 | Aire Valley Surgery (rawdon)  |Outreach event   | yes  | today| yes     | yes  | today-10   | LUDMILLA MCKSN-PDS-ALPHA-SENSITIVE   | 2/5/1974 |  Flu | AUTO-QIVC-OM    | 19/10/2026| administrator    | Branch Surgery    |

@bsarecordvaccine
  Scenario Outline: SUPERSEDED NEW - BSA Record a vaccine
    Given I set vaccinator details with <site> and set vaccinator details with <site> and <vaccination_location> and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue

Examples:
      | index | nhs_number   | site    |vaccination_location    | eligibility | assess_date | consent | vaccination | vaccination_date | name    | dob | address  |chosen_vaccine | batch_number     | batch_expiry_date | user_role | care_model |
      | 0     | 9467361590   | Aire Valley Surgery (rawdon)    |Outreach event    | yes  | today| yes     | yes  | today-9    | WALLIS ADEYEMO  | 19/4/2015  | 1 MIDLAND ROAD, LEEDS, LS6 1BQ  | COVID-19 | AUTO-SUP-C-1     | 19/10/2026 | lead administrator | Branch Surgery    |
      | 8     | 9734250221   | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre      | yes  | today| yes     | yes  | today-20   | BARAK SELIGMANN | 26/5/2016  | 170 WEELSBY ROAD, GRIMSBY, S HUMBERSIDE, DN32 8QQ | Flu | AUTO-SUP-N-F     | 19/10/2026 | recorder    | Community Pharmacy |
      # | 1     | 3508118053   | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Outreach event    | yes  | today| yes     | yes  | today-9    | WALLIS ADEYEMO  | 19/4/2015  | 1 MIDLAND ROAD, LEEDS, LS6 1BQ  | COVID-19 | AUTO-SUPER-C-1   | 19/10/2026 | administrator      | Community Pharmacy |
      # | 2     | 9734250221   | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service | Vaccination Centre      | yes  | today| yes     | yes  | today-30   | BARAK SELIGMANN | 26/5/2016  | 170 WEELSBY ROAD, GRIMSBY, S HUMBERSIDE, DN32 8QQ | Flu | AUTO-SUP-N-F     | 19/10/2026 | recorder    | Community Pharmacy |
      # | 3     | 9467361590   | Leeds Pharmacy      |Vaccination Centre      | yes  | today| yes     | yes  | today-9    | WALLIS ADEYEMO  | 19/4/2015  | 1 MIDLAND ROAD, LEEDS, LS6 1BQ  | COVID-19 | AUTO-SUP-C-1     | 19/10/2026 | lead administrator | Community Pharmacy |
      # | 4     | 3508118053   | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre      | yes  | today| yes     | yes  | today-30   | WALLIS ADEYEMO  | 19/4/2015  | 1 MIDLAND ROAD, LEEDS, LS6 1BQ  | COVID-19 | AUTO-SUPER-C-1   | 19/10/2026 | administrator      | Community Pharmacy |
      # | 5     | 9734250221   | Aire Valley Surgery (rawdon)    |Outreach event    | yes  | today| yes     | yes  | today-60   | BARAK SELIGMANN | 26/5/2016  | 170 WEELSBY ROAD, GRIMSBY, S HUMBERSIDE, DN32 8QQ | Flu | AUTO-SUP-N-F     | 19/10/2026 | recorder    | Branch Surgery    |
      # | 6     | 9467361590   | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service | Vaccination Centre      | yes  | today| yes     | yes  | today-14   | WALLIS ADEYEMO  | 19/4/2015  | 1 MIDLAND ROAD, LEEDS, LS6 1BQ  | COVID-19 | AUTO-SUP-C-1     | 19/10/2026 | lead administrator | Community Pharmacy    |
      # | 7     | 3508118053   | Leeds Pharmacy      |Outreach event    | yes  | today| yes     | yes  | today-30   | WALLIS ADEYEMO  | 19/4/2015  | 1 MIDLAND ROAD, LEEDS, LS6 1BQ  | COVID-19 | AUTO-SUPER-C-1   | 19/10/2026 | administrator      | Community Pharmacy |


@bsarecordvaccine
  Scenario Outline: SUPERSEDED OLD - BSA Record a vaccine
    Given I set vaccinator details with <site> and set vaccinator details with <site> and <vaccination_location> as GP clinic and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue

Examples:
    | index | nhs_number  | site    |vaccination_location  | eligibility | assess_date | consent | vaccination | vaccination_date | name    | chosen_vaccine | batch_number     | batch_expiry_date | care_model | user_role |
    | 0     | 9449304033  | Aire Valley Surgery (rawdon)| Vaccination Centre    | yes  | today| yes     | yes  | today-8   | BARAK SELIGMANN | Flu | AUTO-SUP-O-F      | 19/10/2026 | Branch Surgery    | lead administrator |
    | 1     | 9449304033  | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre    | yes  | today| yes     | yes  | today-14   | BARAK SELIGMANN | COVID-19 | AUTO-SUP-O-C      | 19/10/2026 | Community Pharmacy | administrator      |
    # | 2     | 3508118053  | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre    | yes  | today| yes     | yes  | today-60   | WALLIS ADEYEMO  | Flu | AUTO-SUP-O-F      | 19/10/2026 | Community Pharmacy | recorder    |
    # | 3     | 3508118053  | Leeds Pharmacy      |Vaccination Centre    | yes  | today| yes     | yes  | today-10   | WALLIS ADEYEMO  | COVID-19 | AUTO-SUP-O-C      | 19/10/2026 | Community Pharmacy | lead administrator |
    # | 4     | 9449304033  | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service | Vaccination Centre    | yes  | today| yes     | yes  | today-9    | BARAK SELIGMANN | Flu | AUTO-SUP-O-F      | 19/10/2026 | Community Pharmacy | administrator      |
    # | 5     | 9449304033  | Leeds Pharmacy      |Vaccination Centre    | yes  | today| yes     | yes  | today-60   | BARAK SELIGMANN | COVID-19 | AUTO-SUP-O-C      | 19/10/2026 | Community Pharmacy | lead administrator |
    # | 6     | 3508118053  | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre    | yes  | today| yes     | yes  | today-30   | WALLIS ADEYEMO  | Flu | AUTO-SUP-O-F      | 19/10/2026 | Community Pharmacy | recorder    |
    # | 7     | 3508118053  | Aire Valley Surgery (rawdon)| Vaccination Centre    | yes  | today| yes     | yes  | today-5    | WALLIS ADEYEMO  | COVID-19 | AUTO-SUP-O-C      | 19/10/2026 | Branch Surgery    | administrator      |

@bsarecordvaccine
  Scenario Outline: DECEASED - BSA Record a vaccine
    Given I set vaccinator details with <site> and set vaccinator details with <site> and <vaccination_location> as GP clinic and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue

  Examples:
    | index | nhs_number  | site      |vaccination_location  | eligibility | assess_date | consent | vaccination | vaccination_date | name      | dob| address     |chosen_vaccine | batch_number    | batch_expiry_date | user_role | care_model |
    | 0     | 9449304424  | Aire Valley Surgery (rawdon) | Outreach event   | yes  | today| yes     | yes  | today-9   | John Test | 02/01/1997 | 121C, Durants Road, ENFIELD, EN3 7DG | COVID-19 | AUTO-DEC-SJ1     | 19/10/2026 | lead administrator | Branch Surgery    |
    | 1     | 9449304424  | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre   | yes  | today | yes     | yes  | today-15  | John Test | 02/01/1997 | 121C, Durants Road, ENFIELD, EN3 7DG | Flu | AUTO-DEC-F-SJ1   | 19/10/2026 | administrator      | Community Pharmacy |
    # | 2     | 9449304424  | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service | Vaccination Centre   | yes  | today| yes     | yes  | today-25  | John Test | 02/01/1997 | 121C, Durants Road, ENFIELD, EN3 7DG | COVID-19 | AUTO-DEC-SJ1     | 19/10/2026 | recorder    | Community Pharmacy |
    # | 3     | 9449304424  | Leeds Pharmacy | Vaccination Centre   | yes  | today| yes     | yes  | today-10  | John Test | 02/01/1997 | 121C, Durants Road, ENFIELD, EN3 7DG | Flu | AUTO-DEC-F-SJ1   | 19/10/2026 | lead administrator | Community Pharmacy |
    # | 4     | 9449304424  | Aspire Pharmacy | Outreach event   | yes  | today| yes     | yes  | today-30  | John Test | 02/01/1997 | 121C, Durants Road, ENFIELD, EN3 7DG | COVID-19 | AUTO-DEC-SJ1     | 19/10/2026 | administrator      | Community Pharmacy |

@bsarecordvaccine
  Scenario Outline: LOCAL - BSA Record a vaccine
    Given I set vaccinator details with <site> and set vaccinator details with <site> and <vaccination_location> as GP clinic and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I create a random patient locally
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue

Examples:
    | index | site|vaccination_location    | eligibility | assess_date | consent | vaccination | vaccination_date | chosen_vaccine | batch_number    | batch_expiry_date | user_role | care_model |
    | 0     | Aire Valley Surgery (rawdon)    | Outreach event     | yes  | today| yes     | yes  | today-6   | COVID-19 | AUTO-LOCAL-C     | 19/10/2026 | lead administrator | Branch Surgery    |
    | 1     | Aire Valley Surgery (rawdon)    | Vaccination Centre | yes  | today| yes     | yes  | today-30   | Flu | AUTO-LOCAL-F     | 19/10/2026 | administrator      | Branch Surgery    |
    # | 2     | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre | yes  | today| yes     | yes  | today-60   | COVID-19 | AUTO-LOCAL-C     | 19/10/2026 | recorder    | Community Pharmacy |
    # | 3     | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre | yes  | today| yes     | yes  | today-10   | Flu | AUTO-LOCAL-F     | 19/10/2026 | lead administrator | Community Pharmacy |
    # | 4     | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service | Vaccination Centre | yes  | today| yes     | yes  | today-90   | COVID-19 | AUTO-LOCAL-C     | 19/10/2026 | administrator      | Community Pharmacy |
    # | 5     | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service | Vaccination Centre | yes  | today| yes     | yes  | today-5    | Flu | AUTO-LOCAL-F     | 19/10/2026 | recorder    | Community Pharmacy |
    # | 6     | Leeds Pharmacy   |Vaccination Centre | yes  | today| yes     | yes  | today-50   | COVID-19 | AUTO-LOCAL-C     | 19/10/2026 | lead administrator | Community Pharmacy |
    # | 7     | Leeds Pharmacy   |Vaccination Centre | yes  | today| yes     | yes  | today-20   | Flu | AUTO-LOCAL-F     | 19/10/2026 | administrator      | Community Pharmacy |

  @bsarecordvaccine
  Scenario Outline: MATERNITY NO SUB SITES - Record a maternity vaccine at GP clinic with nhs number - Add and delete
    Given I set vaccinator details with <site> and set vaccinator details with <site> and <vaccination_location> as GP clinic and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the pregnant patient's <eligibility> with the details of due date as <due_date> and assessment date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Continue to Check and confirm screen
    Then I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
    And I click confirm and save button, I should see a record saved dialogue

  Examples:
    | index | nhs_number  | site|vaccination_location|eligibility | due_date   | assess_date | consent | vaccination | vaccination_date | name   | dob | address       |chosen_vaccine  | batch_number   | batch_expiry_date | user_role  | care_model |
    | 4     | 9473629885  | Aire Valley Surgery (rawdon)  | Outreach event|yes  | today+50   | today-4     | yes     | yes  | today-3   | MARGIE PUCKEY      | 27/5/1924  | MANSART COURT, 10 OLIVE SHAPLEY AVENUE, MANCHESTER, M20 6QB    | Respiratory syncytial virus (RSV)   | AUTOMATION-ABR | 1/2/2026   | lead administrator | Branch Surgery    |
    | 0     | 9470004272  | Leeds Pharmacy |Vaccination Centre  |yes  | today      | today| yes     | yes  | today| JOJO LANE   | 06/07/2015 | 10 RAKESMOOR LANE, BARROW-IN-FURNESS, LA14 4LG| Pertussis| AUTOMATION-AVS | 19/10/2027 | administrator      | Community Pharmacy |
    # | 1     | 9469998626  | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre  |yes  | today+100  | today-1     | yes     | yes  | today-1   | JONNY CONOPO| 05/03/2015 | 1 DAISY BANK, LANCASTER, LA1 3JW |Pertussis| AUTOMATION-BIS | 19/10/2028 | recorder    | Community Pharmacy |
    # | 2     | 9470040228  | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service | Hospital hub for staff and patients| yes  | today+290  | today-1     | yes     | yes  | today| HERBERT HAAG| 14/12/1922 | 10 COASTAL ROAD, HEST BANK, LANCASTER, LA2 6HN| Pertussis| AUTO-RVS | 19/02/2029 | lead administrator | Community Pharmacy |
    # | 3     | 9472710255  | Aspire Pharmacy |Housebound patient's home  | yes  | today+5    | today-3     | yes     | yes  | today-2   | DELICE PINKER      | 10/11/1926 | HARDCRAGG HOUSE, HARDCRAGG WAY, GRANGE-OVER-SANDS, CUMBRIA, LA11 6BH | Respiratory syncytial virus (RSV)   | AUTOMATION-ARX | 19/10/2026 | administrator      | Community Pharmacy |
    # | 5     | 9473629885  | Leeds Pharmacy |Vaccination Centre  |yes  | today+10   | today-2     | yes     | yes  | today-5   | MARGIE PUCKEY      | 27/5/1924  | MANSART COURT, 10 OLIVE SHAPLEY AVENUE, MANCHESTER, M20 6QB    | Pertussis| AUTOMATION-XYZ | 19/10/2026 | recorder    | Community Pharmacy |
    # | 6     | 9470004272  | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service | Vaccination Centre  |yes  | today+70   | today-1     | yes     | yes  | today-1   | JOJO LANE   | 06/07/2015 | 10 RAKESMOOR LANE, BARROW-IN-FURNESS, LA14 4LG| Respiratory syncytial virus (RSV)   |AUTOMATION-XYZ | 19/10/2026 | lead administrator | Community Pharmacy |
    # | 7     | 9469998626  | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Housebound patient's home  | yes  | today+120  | today-2     | yes     | yes  | today-4   | JONNY CONOPO| 05/03/2015 | 1 DAISY BANK, LANCASTER, LA1 3JW |Respiratory syncytial virus (RSV)| AUTOMATION-XYZ | 19/10/2026 | administrator      | Community Pharmacy |
    #   # | 4 | 9473629885 | Watling Street Surgery | Outreach event | yes | today+50 | today-4 | yes | yes | today-3  | MARGIE PUCKEY |  27/5/1924 | MANSART COURT, 10 OLIVE SHAPLEY AVENUE, MANCHESTER, M20 6QB | Respiratory syncytial virus (RSV) |  AREX2-15A | 19/10/2026 |   - # This test is no longer needed as Arexvy has been decommissioned on 29th Nov 2024

@bsarecordvaccine
Scenario Outline: NO - Record a vaccine and choose no vaccination decision on the last screen in a GP clinic
    Given I set vaccinator details with <site> and set vaccinator details with <site> and <vaccination_location> as GP clinic and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    And I see the patient's address <address> and gender <gender>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Save and return button

Examples:
    | index | nhs_number  | site    |vaccination_location | eligibility | assess_date | consent | vaccination | vaccination_date | name| dob | address  |chosen_vaccine | batch_number     | batch_expiry_date | gender | care_model| user_role|
    | 4     | 9437541817  | Aire Valley Surgery (rawdon) | Outreach event | no  | today| yes     | no  | today| FLORINDA DUNNER | 27/03/1957 | 32 HOLLAND ROAD, MANCHESTER, M8 4NP    | Flu | AUTO-NO-F-SJ1     | 19/10/2026| female | Branch Surgery   | administrator    |
    | 0     | 9469997956  | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre     | yes  | today| no     | yes | today| SOLOMON DAZLEY  | 30/01/2016 | 10 BROOK STREET, LANCASTER, LA1 1SL    | COVID-19 | AUTO-NO-C-SJ1     | 19/10/2026| male   | Community Pharmacy | lead administrator|
    | 4     | 9437541817  | Leeds Pharmacy   | Outreach event | no   | today| yes     | no  | today| FLORINDA DUNNER | 27/03/1957 | 32 HOLLAND ROAD, MANCHESTER, M8 4NP    | Flu | AUTO-NO-F-SJ1     | 19/10/2026| female | Community Pharmacy   | administrator    |
    # | 0     | 9469997956  | Leeds Pharmacy   | Vaccination Centre   | yes  | today| yes     | yes | today| SOLOMON DAZLEY  | 30/01/2016 | 10 BROOK STREET, LANCASTER, LA1 1SL    | COVID-19 | AUTO-NO-C-SJ1     | 19/10/2026| male   | Community Pharmacy   | lead administrator|
    # | 4     | 9437541817  | Aspire Pharmacy   | Outreach event | yes  | today| no      | no  | today| FLORINDA DUNNER | 27/03/1957 | 32 HOLLAND ROAD, MANCHESTER, M8 4NP    | Flu | AUTO-NO-F-SJ1     | 19/10/2026| female | Community Pharmacy | administrator    |
    # | 0     | 9469997956  | Aspire Pharmacy   | Vaccination Centre   | yes  | today| yes     | yes | today| SOLOMON DAZLEY  | 30/01/2016 | 10 BROOK STREET, LANCASTER, LA1 1SL    | COVID-19 | AUTO-NO-C-SJ1     | 19/10/2026| male   | Community Pharmacy| lead administrator|
    # | 4     | 9437541817  | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service | Outreach event | yes  | today| yes     | no  | today| FLORINDA DUNNER | 27/03/1957 | 32 HOLLAND ROAD, MANCHESTER, M8 4NP    | Flu | AUTO-NO-F-SJ1     | 19/10/2026| female | Community Pharmacy| administrator    |
    # | 0     | 9469997956  | Aire Valley Surgery (rawdon) | Vaccination Centre   | yes  | today| yes     | yes | today| SOLOMON DAZLEY  | 30/01/2016 | 10 BROOK STREET, LANCASTER, LA1 1SL    | COVID-19 | AUTO-NO-C-SJ1     | 19/10/2026| male   | Branch Surgery   | lead administrator|
    # | 4     | 9437541817  | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service   | Outreach event | yes  | today| no      | no  | today| FLORINDA DUNNER | 27/03/1957 | 32 HOLLAND ROAD, MANCHESTER, M8 4NP    | Flu | AUTO-NO-F-SJ1     | 19/10/2026| female | Community Pharmacy | recorder   |
    # | 0     | 9469997956  | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Outreach event | yes  | today| yes     | yes | today| SOLOMON DAZLEY  | 30/01/2016 | 10 BROOK STREET, LANCASTER, LA1 1SL    | COVID-19 | AUTO-NO-C-SJ1     | 19/10/2026| male   | Community Pharmacy | recorder   |

@bsarecordvaccine
  Scenario Outline: NO MATERNITY - Record a maternity vaccine and choose no vaccination decision on the last screen in a GP clinic
    Given I set vaccinator details with <site> and set vaccinator details with <site> and <vaccination_location> as GP clinic and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the pregnant patient's <eligibility> with the details of due date as <due_date> and assessment date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Save and return button

    Examples:
      | index | nhs_number | site   | vaccination_location      | eligibility | due_date | assess_date | consent | vaccination | vaccination_date | name  | dob    | address     | chosen_vaccine  | batch_number | batch_expiry_date | care_model| user_role|
      |  1 | 9473629885 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Outreach event | no | today+50 | today-4 | yes | no | today-3 | MARGIE PUCKEY | 27/5/1924 | MANSART COURT, 10 OLIVE SHAPLEY AVENUE, MANCHESTER, M20 6QB | Respiratory syncytial virus (RSV) | 	AUTO-ABR | 1/2/2026 | Community Pharmacy | recorder   |
      | 2 | 9470040228 | Aspire Pharmacy - Ormskirk - Covid Local Vaccination Service | Hospital hub for staff and patients | yes | today+290 | today-1 | no | no | today  | HERBERT HAAG  | 14/12/1922 | 10 COASTAL ROAD, HEST BANK, LANCASTER, LA2 6HN | Pertussis | AUTO-RVS | 19/2/2029 | Community Pharmacy   | administrator    |
      |  4 | 9473629885 | Aire Valley Surgery (rawdon) | Outreach event | yes | today+50 | today-4 | yes | no | today-3 | MARGIE PUCKEY | 27/5/1924 | MANSART COURT, 10 OLIVE SHAPLEY AVENUE, MANCHESTER, M20 6QB | Respiratory syncytial virus (RSV) | 	AUTO-ABR | 1/2/2026 | Branch Surgery   | administrator    |
      # | 2 | 9470040228 | Aire Valley Surgery (rawdon) | Hospital hub for staff and patients | yes | today+290 | today-1 | yes | no | today  | HERBERT HAAG  | 14/12/1922 | 10 COASTAL ROAD, HEST BANK, LANCASTER, LA2 6HN | Pertussis | AUTO-RVS | 19/2/2029 | Branch Surgery   | administrator    |


