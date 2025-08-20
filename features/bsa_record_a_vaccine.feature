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
      | index | nhs_number | site                                                                              | vaccination_location | eligibility | assess_date | consent | vaccination | vaccination_date | name           | dob        | address                                                                     | chosen_vaccine | chosen_vaccine_type | batch_number  | batch_expiry_date | gender | user_role          | care_model         |
      | 0     | 5990365004 | Leeds Pharmacy                                                                    | GP clinic            | yes         | today       | yes     | yes         | today            | ALANA MRAZ     | 22/02/2022 | CAMPUS CITY NEW CAMPUS 41 BERKELEY ROAD, WESTBURY PARK, Manchester, M16 0RA | COVID-19       | Spikevax JN.1       | AUTO-SJ-AP    | 19/10/2026        | female | lead administrator | community pharmacy |
      | 0     | 5990365004 | Aspire Pharmacy                                                                   | GP clinic            | yes         | today       | yes     | yes         | today-14         | ALANA MRAZ     | 22/02/2022 | CAMPUS CITY NEW CAMPUS 41 BERKELEY ROAD, WESTBURY PARK, Manchester, M16 0RA | COVID-19       | Comirnaty 3 JN.1    | AUTO-SJ-AP    | 19/10/2026        | female | administrator      | community pharmacy |
      | 1     | 5990365624 | Aire Valley Surgery (Rawdon)                                                      | Vaccination Centre   | yes         | today       | yes     | yes         | today-5          | DALLAS KING    | 30/6/2024  | 10 NORTON PARK VIEW, SHEFFIELD, S8 8GS                                      | COVID-19       | Comirnaty 30 JN.1   | AUTO-30-APCSC | 19/10/2026        | male   | recorder           | branch surgery     |
      | 2     | 5990366043 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | GP clinic            | yes         | today       | yes     | yes         | today-30         | AINSLEY INGHAM | 09/12/2015 | CAMPUS CITY NEW CAMPUS 41 BERKELEY ROAD, WESTBURY PARK, Manchester, M16 0RA | COVID-19       | Comirnaty 10 JN.1   | AUTO-10-CSC   | 19/10/2026        | female | lead administrator | community pharmacy |
  # | 3     | 9470032640 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | GP clinic   |yes  | today| yes     | yes  | today-3    | SYBIL PELLING| 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Quadrivalent Influenza Vaccine – High Dose (QIV-HD)    | AUTO-QIHD-OM     | 19/10/2026 | male   | administrator | community pharmacy |
  # | 4     | 5998019903 | Aire Valley Surgery (Rawdon) | GP clinic   |yes  | today| yes     | yes  | today-60   | OAKLEY UDDIN| 30/07/2014 | 31 Earl'S Court Road Hatfield, MD, YO22 4EG | Flu | Quadrivalent Influenza Vaccine (QIVe)| AUTO-QIVE-CSC    | 19/10/2026 | male   | lead administrator | branch surgery   |
  # | 5     | 9449303762 | Aire Valley Surgery (Rawdon) | GP clinic   |yes  | today| yes     | yes  | today-5    | Pryderi Warnford-Davis | 14/04/2001 | 1 CRANLEIGH ROAD, ESHER, SURREY, KT10 8DF     | Flu | Adjuvanted Quadrivalent Influenza Vaccine (aQIV)  | AUTO-QIV-AP      | 19/10/2026 | female | administrator | branch surgery   |
  # | 6     | 9470011902 | Aire Valley Surgery (Rawdon) | GP clinic   |yes  | today| yes     | yes  | today-12   | Katee TUZZIO | 27/05/2015 | BRIDGE END HOUSE, PARK ROAD, MILNTHORPE, CUMBRIA, LA7 7AN | Flu | Fluenz (LAIV)   |AUTO-F-CSC| 19/10/2026 | female | administrator | branch surgery   |

  #commented

  # | 7     | 5998005341 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | GP clinic | yes  | today| yes     | yes  | today-100  | ELVIN MANSELL  | 6/12/1953 | Ilfracombe 7 Goodge Street Mo, MO, YO26 5JZ   | Flu | Cell-based Quadrivalent Influenza Vaccine (QIVc)  | AUTO-QIVC-CSC    | 19/10/2026 | male   | recorder | community pharmacy |

  # | 8     | 5998019903 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service|GP clinic   |yes  | today| yes     | yes  | today-200  | OAKLEY UDDIN| 30/07/2014 | 31 Earl'S Court Road Hatfield, MD, YO22 4EG | Flu | Quadrivalent Influenza Vaccine – High Dose (QIV-HD) | AUTO-QIHD-OM     | 19/10/2026 | female | lead administrator | community pharmacy |

  # commented these below 3


  # | 9     | 9470032640 | Aire Valley Surgery (Rawdon)  | GP clinic   |yes  | today| yes     | yes  | today-12   | SYBIL PELLING | 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Quadrivalent Influenza Vaccine – High Dose (QIV-HD)    | AUTO-QIHD-OM     | 19/10/2026 | male   | administrator | branch surgery   |
  # | 10    | 9470011902 | Aspire Pharmacy|GP clinic   |yes  | today| yes     | yes  | today  | KATEE TUZZIO | 27/05/2015 | BRIDGE END HOUSE, PARK ROAD, MILNTHORPE, CUMBRIA, LA7 7AN | Flu | Quadrivalent Influenza Vaccine (QIVe)| AUTO-QIVE-CSC    | 19/10/2026 | female | administrator | community pharmacy |
  # | 11    | 9470032640 | Aire Valley Surgery (Rawdon) | GP clinic   |yes  | today| yes     | yes  | today-5  | SYBIL PELLING| 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Influenza Tetra MYL (QIVe)| AUTO-ITM-CSC     | 19/10/2026 | male   | lead administrator | branch surgery   |


  # | 12    | 9470032640 | Aire Valley Surgery (Rawdon) | GP clinic   |yes  | today| yes     | yes  | today-100  | SYBIL PELLING| 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Influenza Tetra MYL (QIVe)| AUTO-ITM-CSC     | 19/10/2026 | male   | lead administrator | branch surgery   |
  # | 12    | 9470032640 | Aire Valley Surgery (Rawdon) | GP clinic   |yes  | today| yes     | yes  | today-5  | SYBIL PELLING| 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Influenza Tetra MYL (QIVe)| AUTO-ITM-CSC     | 19/10/2026 | male   | administrator | branch surgery   |

  @bsarecordvaccine
  #skipped because these tests are trying to assert a delete when they shouldn't be able to. Double fail = pass??
  @skip
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
      | index | nhs_number | site            | vaccination_location | eligibility | assess_date | consent | vaccination | vaccination_date | name           | dob        | address                                                                     | chosen_vaccine | chosen_vaccine_type | batch_number  | batch_expiry_date | gender | user_role          | care_model         |
      # | 0     | 5990365004 | Leeds Pharmacy     | GP clinic   | yes  | today| yes     | yes  | today | ALANA MRAZ   | 22/02/2022 | CAMPUS CITY NEW CAMPUS 41 BERKELEY ROAD, WESTBURY PARK, Manchester, M16 0RA | COVID-19 | Spikevax JN.1   |AUTO-SJ-AP| 19/10/2026 | female | lead administrator | community pharmacy |
      | 0     | 5990365004 | Aspire Pharmacy | GP clinic            | yes         | today       | yes     | yes         | today            | ALANA MRAZ     | 22/02/2022 | CAMPUS CITY NEW CAMPUS 41 BERKELEY ROAD, WESTBURY PARK, Manchester, M16 0RA | COVID-19       | Spikevax JN.1       | AUTO-SJ-AP    | 19/10/2026        | female | administrator      | community pharmacy |
      | 1     | 5990365624 | Leeds Pharmacy  | Vaccination Centre   | yes         | today       | yes     | yes         | today-20         | DALLAS KING    | 30/6/2024  | 10 NORTON PARK VIEW, SHEFFIELD, S8 8GS                                      | COVID-19       | Comirnaty 30 JN.1   | AUTO-30-APCSC | 19/10/2026        | male   | recorder           | community pharmacy |
      | 2     | 5990366043 | Aspire Pharmacy | GP clinic            | yes         | today       | yes     | yes         | today-7          | AINSLEY INGHAM | 09/12/2015 | CAMPUS CITY NEW CAMPUS 41 BERKELEY ROAD, WESTBURY PARK, Manchester, M16 0RA | COVID-19       | Comirnaty 10 JN.1   | AUTO-10-CSC   | 19/10/2026        | female | lead administrator | community pharmacy |
      | 3     | 5990366043 | Aspire Pharmacy | GP clinic            | yes         | today       | yes     | yes         | today-3          | AINSLEY INGHAM | 09/12/2015 | CAMPUS CITY NEW CAMPUS 41 BERKELEY ROAD, WESTBURY PARK, Manchester, M16 0RA | COVID-19       | Comirnaty 3 JN.1    | AUTO-10-CSC   | 19/10/2026        | female | lead administrator | community pharmacy |

  # commented these below 4

  # | 4     | 9470032640 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | GP clinic   |yes  | today| yes     | yes  | today-3    | SYBIL PELLING| 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Quadrivalent Influenza Vaccine – High Dose (QIV-HD)    | AUTO-QIHD-OM     | 19/10/2026 | male   | administrator | community pharmacy |
  # | 5     | 5998019903 | Aire Valley Surgery (Rawdon) | GP clinic   |yes  | today| yes     | yes  | today-60   | OAKLEY UDDIN| 30/07/2014 | 31 Earl'S Court Road Hatfield, MD, YO22 4EG | Flu | Quadrivalent Influenza Vaccine (QIVe)| AUTO-QIVE-CSC    | 19/10/2026 | male   | lead administrator | branch surgery   |
  # | 6     | 9449303762 | Aire Valley Surgery (Rawdon) | GP clinic   |yes  | today| yes     | yes  | today-5    | Pryderi Warnford-Davis | 14/04/2001 | 1 CRANLEIGH ROAD, ESHER, SURREY, KT10 8DF     | Flu | Adjuvanted Quadrivalent Influenza Vaccine (aQIV)  | AUTO-QIV-AP      | 19/10/2026 | female | administrator | branch surgery   |
  # | 7     | 9470011902 | Aire Valley Surgery (Rawdon) | GP clinic   |yes  | today| yes     | yes  | today-2   | Katee TUZZIO | 27/05/2015 | BRIDGE END HOUSE, PARK ROAD, MILNTHORPE, CUMBRIA, LA7 7AN | Flu | Fluenz (LAIV)   |AUTO-F-CSC| 19/10/2026 | female | administrator | branch surgery   |


  # | 7     | 5998005341 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | GP clinic | yes  | today| yes     | yes  | today-100  | ELVIN MANSELL  | 6/12/1953 | Ilfracombe 7 Goodge Street Mo, MO, YO26 5JZ   | Flu | Cell-based Quadrivalent Influenza Vaccine (QIVc)  | AUTO-QIVC-CSC    | 19/10/2026 | male   | recorder | community pharmacy |
  # | 8     | 5998019903 | Aspire Pharmacy|GP clinic   |yes  | today| yes     | yes  | today-200  | OAKLEY UDDIN| 30/07/2014 | 31 Earl'S Court Road Hatfield, MD, YO22 4EG | Flu | Quadrivalent Influenza Vaccine – High Dose (QIV-HD) | AUTO-QIHD-OM     | 19/10/2026 | female | lead administrator | community pharmacy |
  # | 9     | 9470032640 | Aire Valley Surgery (Rawdon) | GP clinic   |yes  | today| yes     | yes  | today-12   | SYBIL PELLING| 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Quadrivalent Influenza Vaccine – High Dose (QIV-HD)    | AUTO-QIHD-OM     | 19/10/2026 | male   | administrator | branch surgery   |
  # | 10    | 9470011902 | Aspire Pharmacy|GP clinic   |yes  | today| yes     | yes  | today-121  | KATEE TUZZIO | 27/05/2015 | BRIDGE END HOUSE, PARK ROAD, MILNTHORPE, CUMBRIA, LA7 7AN | Flu | Quadrivalent Influenza Vaccine (QIVe)| AUTO-QIVE-CSC    | 19/10/2026 | female | administrator | community pharmacy |
  # | 11    | 9470032640 | Aire Valley Surgery (Rawdon) | GP clinic   |yes  | today| yes     | yes  | today-365  | SYBIL PELLING | 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Influenza Tetra MYL (QIVe)| AUTO-ITM-4CSC     | 19/10/2026 | male   | lead administrator | branch surgery   |
  # | 12    | 9470032640 | Aire Valley Surgery (Rawdon) | GP clinic   |yes  | today| yes     | yes  | today-100  | SYBIL PELLING| 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Influenza Tetra MYL (QIVe)| AUTO-ITM-CSC     | 19/10/2026 | male   | lead administrator | branch surgery   |
  # | 12    | 9470032640 | Aire Valley Surgery (Rawdon) | GP clinic   |yes  | today| yes     | yes  | today-5  | SYBIL PELLING| 17/12/2015 | 50 ST. GEORGES QUAY, LANCASTER, LA1 1SA | Flu | Influenza Tetra MYL (QIVe)| AUTO-ITM-CSC     | 19/10/2026 | male   | administrator | branch surgery   |

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
      | index | nhs_number | site                         | vaccination_location | eligibility | assess_date | consent | vaccination | vaccination_date | name         | dob        | chosen_vaccine | batch_number | batch_expiry_date | user_role     | care_model     |
      | 0     | 5558785314 | Aire Valley Surgery (Rawdon) | Outreach event       | yes         | today       | yes     | yes         | today-14         | ANDRE SANTOS | 01/01/1991 | COVID-19       | AUTO-C-SFLAG | 19/10/2026        | administrator | Branch Surgery |


  # | 1     | 5558785314 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre     | yes  | today| yes     | yes  | today-5   | ANDRE SANTOS   | 01/01/1991 | Flu | AUTO-F-SFLAG    | 19/10/2026| lead administrator| Community Pharmacy |


  # | 2     | 9450127077 | Leeds Pharmacy   | GP clinic   | yes  | today| yes     | yes  | today-200  | LUDMILLA MCKSN-PDS-ALPHA-SENSITIVE   | 2/5/1974 | COVID-19 | AUTO-SJ-AP      | 19/10/2026| recorder  | Community Pharmacy    |
  # | 3     | 9450127077 | Aire Valley Surgery (Rawdon)  |Vaccination Centre     | yes  | today| yes     | yes  | today-60   | LUDMILLA MCKSN-PDS-ALPHA-SENSITIVE   | 2/5/1974 | Flu | AUTO-QIVC-CSC   | 19/10/2026| lead administrator| Branch Surgery    |
  # | 4     | 5558785314 | Aspire Pharmacy   |Outreach event   | yes  | today| yes     | yes  | today-90   | ANDRE SANTOS   | 01/01/1991 | COVID-19 | AUTO-30-APCSC   | 19/10/2026| administrator    | Community Pharmacy |
  # | 5     | 5558785314 | Leeds Pharmacy   | GP clinic   | yes  | today| yes     | yes  | today-120  | ANDRE SANTOS   | 01/01/1991 | Flu | AUTO-QIHD-OM    | 19/10/2026| recorder  | Community Pharmacy    |
  # | 6     | 9450127077 | Aspire Pharmacy   | GP clinic   | yes  | today| yes     | yes  | today-100  | LUDMILLA MCKSN-PDS-ALPHA-SENSITIVE   | 2/5/1974 | COVID-19 | AUTO-SJ-AP      | 19/10/2026| lead administrator| Community Pharmacy |
  # | 7     | 5558785314 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Outreach event   | yes  | today| yes     | yes  | today-5    | ANDRE SANTOS    | 1/1/1991    | Flu | AUTO-QIVE-CSC   | 19/10/2026| recorder  | Community Pharmacy |
  # | 8     | 9450127077 | Leeds Pharmacy   |GP clinic   | yes  | today| yes     | yes  | today-14   | LUDMILLA MCKSN-PDS-ALPHA-SENSITIVE   | 2/5/1974 |  Flu | AUTO-QIVC-CSC   | 19/10/2026| administrator    | Community Pharmacy    |
  # | 9     | 9450127077 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre     | yes  | today| yes     | yes  | today-30   | LUDMILLA MCKSN-PDS-ALPHA-SENSITIVE   | 2/5/1974 |  COVID-19 | AUTO-QIV-HD-OM  | 19/10/2026| lead administrator| Community Pharmacy |
  # | 10    | 9450127077 | Aire Valley Surgery (Rawdon)  |Outreach event   | yes  | today| yes     | yes  | today-10   | LUDMILLA MCKSN-PDS-ALPHA-SENSITIVE   | 2/5/1974 |  Flu | AUTO-QIVC-OM    | 19/10/2026| administrator    | Branch Surgery    |

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
      | index | nhs_number | site                         | vaccination_location | eligibility | assess_date | consent | vaccination | vaccination_date | name               | dob       | address                                                   | chosen_vaccine | batch_number | batch_expiry_date | user_role          | care_model     |
      | 0     | 9430023373 | Aire Valley Surgery (Rawdon) | Outreach event       | yes         | today       | yes     | yes         | today-9          | CORETTA AMBROSETTI | 22/6/1959 | 2 BARTLE HALL COTTAGE, LEA LANE, BARTLE, PRESTON, PR4 0HA | COVID-19       | AUTO-SUP-C-1 | 19/10/2026        | lead administrator | Branch Surgery |


  # | 8     | 9430026046   | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre      | yes  | today| yes     | yes  | today-20   | KEMP FLEETHAM | 26/5/2016  | 170 WEELSBY ROAD, GRIMSBY, S HUMBERSIDE, DN32 8QQ | Flu | AUTO-SUP-N-F     | 19/10/2026 | recorder    | Community Pharmacy |


  # | 1     | 3508118053   | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Outreach event    | yes  | today| yes     | yes  | today-9    | CORETTA AMBROSETTI  | 22/6/1959  | 2 BARTLE HALL COTTAGE, LEA LANE, BARTLE, PRESTON, PR4 0HA  | COVID-19 | AUTO-SUPER-C-1   | 19/10/2026 | administrator      | Community Pharmacy |
  # | 2     | 9430026046   | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre      | yes  | today| yes     | yes  | today-30   | KEMP FLEETHAM | 26/5/2016  | 170 WEELSBY ROAD, GRIMSBY, S HUMBERSIDE, DN32 8QQ | Flu | AUTO-SUP-N-F     | 19/10/2026 | recorder    | Community Pharmacy |
  # | 3     | 9430023373   | Leeds Pharmacy      |Vaccination Centre      | yes  | today| yes     | yes  | today-9    | CORETTA AMBROSETTI  | 22/6/1959  | 2 BARTLE HALL COTTAGE, LEA LANE, BARTLE, PRESTON, PR4 0HA  | COVID-19 | AUTO-SUP-C-1     | 19/10/2026 | lead administrator | Community Pharmacy |
  # | 4     | 3508118053   | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre      | yes  | today| yes     | yes  | today-30   | CORETTA AMBROSETTI  | 22/6/1959  | 2 BARTLE HALL COTTAGE, LEA LANE, BARTLE, PRESTON, PR4 0HA  | COVID-19 | AUTO-SUPER-C-1   | 19/10/2026 | administrator      | Community Pharmacy |
  # | 5     | 9430026046   | Aire Valley Surgery (Rawdon)    |Outreach event    | yes  | today| yes     | yes  | today-60   | KEMP FLEETHAM | 26/5/2016  | 170 WEELSBY ROAD, GRIMSBY, S HUMBERSIDE, DN32 8QQ | Flu | AUTO-SUP-N-F     | 19/10/2026 | recorder    | Branch Surgery    |
  # | 6     | 9430023373   | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre      | yes  | today| yes     | yes  | today-14   | CORETTA AMBROSETTI  | 22/6/1959  | 2 BARTLE HALL COTTAGE, LEA LANE, BARTLE, PRESTON, PR4 0HA  | COVID-19 | AUTO-SUP-C-1     | 19/10/2026 | lead administrator | Community Pharmacy    |
  # | 7     | 3508118053   | Leeds Pharmacy      |Outreach event    | yes  | today| yes     | yes  | today-30   | CORETTA AMBROSETTI  | 22/6/1959  | 2 BARTLE HALL COTTAGE, LEA LANE, BARTLE, PRESTON, PR4 0HA  | COVID-19 | AUTO-SUPER-C-1   | 19/10/2026 | administrator      | Community Pharmacy |


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
      | index | nhs_number | site                                                                              | vaccination_location | eligibility | assess_date | consent | vaccination | vaccination_date | name          | chosen_vaccine | batch_number | batch_expiry_date | care_model         | user_role     |
      # | 0     | 9430026054  | Aire Valley Surgery (Rawdon)| Vaccination Centre    | yes  | today| yes     | yes  | today-8   | KEMP FLEETHAM | Flu | AUTO-SUP-O-F      | 19/10/2026 | Branch Surgery    | lead administrator |
      | 1     | 9430026054 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre   | yes         | today       | yes     | yes         | today-14         | KEMP FLEETHAM | COVID-19       | AUTO-SUP-O-C | 19/10/2026        | Community Pharmacy | administrator |
  # | 2     | 3508118053  | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre    | yes  | today| yes     | yes  | today-60   | CORETTA AMBROSETTI  | Flu | AUTO-SUP-O-F      | 19/10/2026 | Community Pharmacy | recorder    |
  # | 3     | 3508118053  | Leeds Pharmacy      |Vaccination Centre    | yes  | today| yes     | yes  | today-10   | CORETTA AMBROSETTI  | COVID-19 | AUTO-SUP-O-C      | 19/10/2026 | Community Pharmacy | lead administrator |
  # | 4     | 9430026054  | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre    | yes  | today| yes     | yes  | today-9    | KEMP FLEETHAM | Flu | AUTO-SUP-O-F      | 19/10/2026 | Community Pharmacy | administrator      |
  # | 5     | 9430026054  | Leeds Pharmacy      |Vaccination Centre    | yes  | today| yes     | yes  | today-60   | KEMP FLEETHAM | COVID-19 | AUTO-SUP-O-C      | 19/10/2026 | Community Pharmacy | lead administrator |
  # | 6     | 3508118053  | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre    | yes  | today| yes     | yes  | today-30   | CORETTA AMBROSETTI  | Flu | AUTO-SUP-O-F      | 19/10/2026 | Community Pharmacy | recorder    |
  # | 7     | 3508118053  | Aire Valley Surgery (Rawdon)| Vaccination Centre    | yes  | today| yes     | yes  | today-5    | CORETTA AMBROSETTI  | COVID-19 | AUTO-SUP-O-C      | 19/10/2026 | Branch Surgery    | administrator      |

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
      | index | nhs_number | site                         | vaccination_location | eligibility | assess_date | consent | vaccination | vaccination_date | name       | dob        | address                                                            | chosen_vaccine | batch_number | batch_expiry_date | user_role          | care_model     |
      | 0     | 9465492302 | Aire Valley Surgery (Rawdon) | Outreach event       | yes         | today       | yes     | yes         | today-9          | MYRA ALLEN | 06/05/1973 | SOUTH LODGE, TOLL ROAD, BLEADON, WESTON-SUPER-MARE, AVON, BS23 4TZ | COVID-19       | AUTO-DEC-SJ1 | 19/10/2026        | lead administrator | Branch Surgery |


  # | 1     | 9465492302  | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre   | yes  | today | yes     | yes  | today-15  | MYRA ALLEN | 06/05/1973 | SOUTH LODGE, TOLL ROAD, BLEADON, WESTON-SUPER-MARE, AVON, BS23 4TZ | Flu | AUTO-DEC-F-SJ1   | 19/10/2026 | administrator      | Community Pharmacy |


  # | 2     | 9465492302  | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre   | yes  | today| yes     | yes  | today-25  | MYRA ALLEN | 06/05/1973 | SOUTH LODGE, TOLL ROAD, BLEADON, WESTON-SUPER-MARE, AVON, BS23 4TZ | COVID-19 | AUTO-DEC-SJ1     | 19/10/2026 | recorder    | Community Pharmacy |
  # | 3     | 9465492302  | Leeds Pharmacy | Vaccination Centre   | yes  | today| yes     | yes  | today-10  | MYRA ALLEN | 06/05/1973 | SOUTH LODGE, TOLL ROAD, BLEADON, WESTON-SUPER-MARE, AVON, BS23 4TZ | Flu | AUTO-DEC-F-SJ1   | 19/10/2026 | lead administrator | Community Pharmacy |
  # | 4     | 9465492302  | Aspire Pharmacy | Outreach event   | yes  | today| yes     | yes  | today-30  | MYRA ALLEN | 06/05/1973 | SOUTH LODGE, TOLL ROAD, BLEADON, WESTON-SUPER-MARE, AVON, BS23 4TZ | COVID-19 | AUTO-DEC-SJ1     | 19/10/2026 | administrator      | Community Pharmacy |

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
      | index | site                         | vaccination_location | eligibility | assess_date | consent | vaccination | vaccination_date | chosen_vaccine | batch_number | batch_expiry_date | user_role          | care_model     |
      | 0     | Aire Valley Surgery (Rawdon) | Outreach event       | yes         | today       | yes     | yes         | today-6          | COVID-19       | AUTO-LOCAL-C | 19/10/2026        | lead administrator | Branch Surgery |


  # | 1     | Aire Valley Surgery (Rawdon)    | Vaccination Centre | yes  | today| yes     | yes  | today-30   | Flu | AUTO-LOCAL-F     | 19/10/2026 | administrator      | Branch Surgery    |


  # | 2     | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre | yes  | today| yes     | yes  | today-60   | COVID-19 | AUTO-LOCAL-C     | 19/10/2026 | recorder    | Community Pharmacy |
  # | 3     | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre | yes  | today| yes     | yes  | today-10   | Flu | AUTO-LOCAL-F     | 19/10/2026 | lead administrator | Community Pharmacy |
  # | 4     | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre | yes  | today| yes     | yes  | today-90   | COVID-19 | AUTO-LOCAL-C     | 19/10/2026 | administrator      | Community Pharmacy |
  # | 5     | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre | yes  | today| yes     | yes  | today-5    | Flu | AUTO-LOCAL-F     | 19/10/2026 | recorder    | Community Pharmacy |
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
      | index | nhs_number | site                         | vaccination_location | eligibility | due_date | assess_date | consent | vaccination | vaccination_date | name           | dob        | address                                                                     | chosen_vaccine                    | batch_number   | batch_expiry_date | user_role          | care_model         |
      | 4     | 5990374534 | Aire Valley Surgery (Rawdon) | Outreach event       | yes         | today+50 | today-4     | yes     | yes         | today-3          | GABI FOSTER    | 6/6/2004   | CAMPUS CITY NEW CAMPUS 41 BERKELEY ROAD, WESTBURY PARK, Manchester, M16 0RA | Respiratory syncytial virus (RSV) | AUTOMATION-ABR | 1/2/2026          | lead administrator | Branch Surgery     |
      | 0     | 5990376766 | Leeds Pharmacy               | Vaccination Centre   | yes         | today    | today       | yes     | yes         | today            | KAYABI KERRABI | 20/11/2004 | 01, Moore, Bishop, Essex, N8 7RE                                            | Pertussis                         | AUTOMATION-AVS | 19/10/2027        | administrator      | Community Pharmacy |
  # | 1     | 9469998626  | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre  |yes  | today+100  | today-1     | yes     | yes  | today-1   | JONNY CONOPO| 05/03/2015 | 1 DAISY BANK, LANCASTER, LA1 3JW |Pertussis| AUTOMATION-BIS | 19/10/2028 | recorder    | Community Pharmacy |
  # | 2     | 5990379013  | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Hospital hub for staff and patients| yes  | today+290  | today-1     | yes     | yes  | today| LAURIE RAMSAY| 6/12/1953 | 01, Moore, Bishop, Essex, N8 7RE| Pertussis| AUTO-RVS | 19/02/2029 | lead administrator | Community Pharmacy |
  # | 3     | 9472710255  | Aspire Pharmacy |Housebound patient's home  | yes  | today+5    | today-3     | yes     | yes  | today-2   | DELICE PINKER      | 10/11/1926 | HARDCRAGG HOUSE, HARDCRAGG WAY, GRANGE-OVER-SANDS, CUMBRIA, LA11 6BH | Respiratory syncytial virus (RSV)   | AUTOMATION-ARX | 19/10/2026 | administrator      | Community Pharmacy |
  # | 5     | 5990374534  | Leeds Pharmacy |Vaccination Centre  |yes  | today+10   | today-2     | yes     | yes  | today-5   | GABI FOSTER      | 6/6/2004  | CAMPUS CITY NEW CAMPUS 41 BERKELEY ROAD, WESTBURY PARK, Manchester, M16 0RA    | Pertussis| AUTOMATION-XYZ | 19/10/2026 | recorder    | Community Pharmacy |
  # | 6     | 5990376766  | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre  |yes  | today+70   | today-1     | yes     | yes  | today-1   | KAYABI KERRABI   | 20/11/2004 | 01, Moore, Bishop, Essex, N8 7RE| Respiratory syncytial virus (RSV)   |AUTOMATION-XYZ | 19/10/2026 | lead administrator | Community Pharmacy |
  # | 7     | 9469998626  | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Housebound patient's home  | yes  | today+120  | today-2     | yes     | yes  | today-4   | JONNY CONOPO| 05/03/2015 | 1 DAISY BANK, LANCASTER, LA1 3JW |Respiratory syncytial virus (RSV)| AUTOMATION-XYZ | 19/10/2026 | administrator      | Community Pharmacy |
  #   # | 4 | 5990374534 | Watling Street Surgery | Outreach event | yes | today+50 | today-4 | yes | yes | today-3  | GABI FOSTER |  6/6/2004 | CAMPUS CITY NEW CAMPUS 41 BERKELEY ROAD, WESTBURY PARK, Manchester, M16 0RA | Respiratory syncytial virus (RSV) |  AREX2-15A | 19/10/2026 |   - # This test is no longer needed as Arexvy has been decommissioned on 29th Nov 2024

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
    And I should see a record saved dialogue

    Examples:
      | index | nhs_number | site                                                                              | vaccination_location | eligibility | assess_date | consent | vaccination | vaccination_date | name           | dob        | address                             | chosen_vaccine | batch_number  | batch_expiry_date | gender | care_model         | user_role          |
      | 4     | 5990377282 | Aire Valley Surgery (Rawdon)                                                      | Outreach event       | no          | today       | yes     | no          | today            | GABI JERRY     | 27/03/1957 | 32 HOLLAND ROAD, MANCHESTER, M8 4NP | Flu            | AUTO-NO-F-SJ1 | 19/10/2026        | female | Branch Surgery     | administrator      |
      | 0     | 5990378017 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Vaccination Centre   | yes         | today       | no      | yes         | today            | WHITNEY CLARKE | 30/01/2016 | 10 BROOK STREET, LANCASTER, LA1 1SL | COVID-19       | AUTO-NO-C-SJ1 | 19/10/2026        | male   | Community Pharmacy | lead administrator |


  # | 4     | 5990377282  | Leeds Pharmacy   | Outreach event | no   | today| yes     | no  | today| GABI JERRY | 27/03/1957 | 32 HOLLAND ROAD, MANCHESTER, M8 4NP    | Flu | AUTO-NO-F-SJ1     | 19/10/2026| female | Community Pharmacy   | administrator    |


  # | 0     | 5990378017  | Leeds Pharmacy   | Vaccination Centre   | yes  | today| yes     | yes | today| WHITNEY CLARKE  | 30/01/2016 | 10 BROOK STREET, LANCASTER, LA1 1SL    | COVID-19 | AUTO-NO-C-SJ1     | 19/10/2026| male   | Community Pharmacy   | lead administrator|
  # | 4     | 5990377282  | Aspire Pharmacy   | Outreach event | yes  | today| no      | no  | today| GABI JERRY | 27/03/1957 | 32 HOLLAND ROAD, MANCHESTER, M8 4NP    | Flu | AUTO-NO-F-SJ1     | 19/10/2026| female | Community Pharmacy | administrator    |
  # | 0     | 5990378017  | Aspire Pharmacy   | Vaccination Centre   | yes  | today| yes     | yes | today| WHITNEY CLARKE  | 30/01/2016 | 10 BROOK STREET, LANCASTER, LA1 1SL    | COVID-19 | AUTO-NO-C-SJ1     | 19/10/2026| male   | Community Pharmacy| lead administrator|
  # | 4     | 5990377282  | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Outreach event | yes  | today| yes     | no  | today| GABI JERRY | 27/03/1957 | 32 HOLLAND ROAD, MANCHESTER, M8 4NP    | Flu | AUTO-NO-F-SJ1     | 19/10/2026| female | Community Pharmacy| administrator    |
  # | 0     | 5990378017  | Aire Valley Surgery (Rawdon) | Vaccination Centre   | yes  | today| yes     | yes | today| WHITNEY CLARKE  | 30/01/2016 | 10 BROOK STREET, LANCASTER, LA1 1SL    | COVID-19 | AUTO-NO-C-SJ1     | 19/10/2026| male   | Branch Surgery   | lead administrator|
  # | 4     | 5990377282  | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service   | Outreach event | yes  | today| no      | no  | today| GABI JERRY | 27/03/1957 | 32 HOLLAND ROAD, MANCHESTER, M8 4NP    | Flu | AUTO-NO-F-SJ1     | 19/10/2026| female | Community Pharmacy | recorder   |
  # | 0     | 5990378017  | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Outreach event | yes  | today| yes     | yes | today| WHITNEY CLARKE  | 30/01/2016 | 10 BROOK STREET, LANCASTER, LA1 1SL    | COVID-19 | AUTO-NO-C-SJ1     | 19/10/2026| male   | Community Pharmacy | recorder   |

  @bsarecordvaccine
  Scenario Outline: NO MATERNITY - Record a maternity vaccine and choose no vaccination decision on the last screen in a GP clinic
    Given I set vaccinator details with <site> and set vaccinator details with <site> and <vaccination_location> as GP clinic and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the pregnant patient's <eligibility> with the details of due date as <due_date> and assessment date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Save and return button
    And I should see a record saved dialogue

    Examples:
      | index | nhs_number | site                                                                              | vaccination_location                | eligibility | due_date  | assess_date | consent | vaccination | vaccination_date | name          | dob       | address                                                                     | chosen_vaccine                    | batch_number | batch_expiry_date | care_model         | user_role     |
      | 1     | 5990374534 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Outreach event                      | no          | today+50  | today-4     | yes     | no          | today-3          | GABI FOSTER   | 6/6/2004  | CAMPUS CITY NEW CAMPUS 41 BERKELEY ROAD, WESTBURY PARK, Manchester, M16 0RA | Respiratory syncytial virus (RSV) | AUTO-ABR     | 1/2/2026          | Community Pharmacy | recorder      |
      | 2     | 5990379013 | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service | Hospital hub for staff and patients | yes         | today+290 | today-1     | no      | no          | today            | LAURIE RAMSAY | 6/12/1953 | 01, Moore, Bishop, Essex, N8 7RE                                            | Pertussis                         | AUTO-RVS     | 19/2/2029         | Community Pharmacy | administrator |
      | 4     | 5990374534 | Aire Valley Surgery (Rawdon)                                                      | Outreach event                      | yes         | today+50  | today-4     | yes     | no          | today-3          | GABI FOSTER   | 6/6/2004  | CAMPUS CITY NEW CAMPUS 41 BERKELEY ROAD, WESTBURY PARK, Manchester, M16 0RA | Respiratory syncytial virus (RSV) | AUTO-ABR     | 1/2/2026          | Branch Surgery     | administrator |
# | 2 | 5990379013 | Aire Valley Surgery (Rawdon) | Hospital hub for staff and patients | yes | today+290 | today-1 | yes | no | today  | LAURIE RAMSAY  | 6/12/1953 | 01, Moore, Bishop, Essex, N8 7RE | Pertussis | AUTO-RVS | 19/2/2029 | Branch Surgery   | administrator    |
