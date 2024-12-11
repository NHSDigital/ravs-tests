Feature: Reports

@reports
Scenario: Reports page is displayed
  Given I am logged into the RAVS app
  When I click the reports navigation link
  Then the reports page should be displayed

Scenario: Choose dates page is displayed
  Given I am logged into the RAVS app
  When I click the reports navigation link
  And I click the create report button
  Then the choose dates page should be displayed

Scenario Outline: Create report for an organization with no location sites
  Given I am logged into the RAVS app with the <username>
  When I click the reports navigation link
  Then the `No vaccination data to report on` message should be displayed
  And the Create report button should be disabled

Examples:
| username                                      |
| neelima.guntupalli1+no_location_sites@nhs.net |

Scenario Outline: "Choose vaccines" page is displayed
  Given I am logged into the RAVS app
  When I click the reports navigation link
  And I click the create report button
  And I click the <day> radio button and click Continue
  Then the choose vaccines page should be displayed

Examples:
| day        |
| Yesterday  |
| Today      |
| Last 7 days (includes today)   |
| Last 14 days (includes today)  |
| Last 31 days (includes today)  |
| Select a custom date range up to 31 days  |

Scenario: User should not be able to proceed if no date range is selected
  Given I am logged into the RAVS app
  When I click the reports navigation link
  And I click the create report button
  And I select no date range and click Continue
  Then the user should not be able to proceed to choose a vaccine

Scenario Outline: User should not be able to proceed if incorrect date range is selected
  Given I am logged into the RAVS app
  When I click the reports navigation link
  And I click the create report button
  And I select a invalid date range of <from_date> and <to_date> and click Continue
  Then the error message <error_message> should be displayed

Examples:
  | from_date   | to_date   | error_message                                               |
  | today       | today+31  | To date must be in the past                                 |
  | today       | today+1   | To date must be in the past                                 |
  | today+1     | today+1   | To date must be in the past, From date must be in the past  |
  | today+1     | today     | From date must be in the past                               |
  | null        | null      | Enter From date, Enter To date                              |

Scenario Outline: Choose sites page is displayed
  Given I am logged into the RAVS app
  When I click the reports navigation link
  And I click the create report button
  And I click the today date range button and click continue
  And I select the vaccine type <vaccineType> and click continue
  Then the choose sites page should be displayed

  Examples:
  |vaccineType                        |
  | COVID-19                          |
  | Flu                               |
  | Pertussis                         |
  | Respiratory syncytial virus (RSV) |

Scenario Outline: Choose data page is displayed
  Given I am logged into the RAVS app
  When I click the reports navigation link
  And I click the create report button
  And I click the today date range button and click continue
  And I select the vaccine type <vaccineType> and click continue
  And I select the site <site> and click continue
  Then the choose data page should be displayed and all data options should be checked by default

  Examples:
  |vaccineType                        | site          |
  | COVID-19                          | Albert House  |
  | Flu                               | Albert House  |
  | Pertussis                         | Albert House  |
  | Respiratory syncytial virus (RSV) | Albert House  |

Scenario Outline: Check and confirm page should be displayed
  Given I am logged into the RAVS app
  When I click the reports navigation link
  And I click the create report button
  And I click the today date range button and click continue
  And I select the vaccine type <vaccineType> and click continue
  And I select the site <site> and click continue
  And I click continue on the data page
  Then the check and confirm page should be displayed

  Examples:
  |vaccineType                        | site          |
  | COVID-19                          | Albert House  |
  | Flu                               | Albert House  |
  | Pertussis                         | Albert House  |
  | Respiratory syncytial virus (RSV) | Albert House  |
  | COVID-19                          | Albert House  |

Scenario Outline: Report is ready page should be displayed
  Given I am logged into the RAVS app
  When I click the reports navigation link
  And I click the create report button
  And I click the today date range button and click continue
  And I select the vaccine type <vaccineType> and click continue
  And I select the site <site> and click continue
  And I click continue on the data page
  And I click Confirm and create report button in the check and confirm page
  Then Creating your page element should be displayed and Download Report button should be visible

  Examples:
  |vaccineType                        | site          |
  | COVID-19                          | Albert House  |
  | Flu                               | Albert House  |
  | Pertussis                         | Albert House  |
  | Respiratory syncytial virus (RSV) | Albert House  |
  | COVID-19                          | Albert House  |

Scenario Outline: User can download the report
  Given I am logged into the RAVS app
  When I click the reports navigation link
  And I click the create report button
  And I click the <day> radio button and click Continue
  And I select the vaccine type <vaccineType> and click continue
  And I select the site <site> and click continue
  And I click continue on the data page
  And I click Confirm and create report button in the check and confirm page
  And I click download report button
  Then the report is downloaded successfully

  Examples:
  |vaccineType                        | site          | day                                       |
  | COVID-19                          | Albert House  | Last 31 days (includes today)             |
  | Flu                               | Albert House  | Last 31 days (includes today)             |
  | Pertussis                         | Albert House  | Last 7 days (includes today)              |
  | Respiratory syncytial virus (RSV) | Albert House  | Last 14 days (includes today)             |
  | COVID-19                          | Albert House  | Last 31 days (includes today)             |
  | COVID-19                          | Albert House  | Select a custom date range up to 31 days  |

  Scenario Outline: Record a vaccine and generate a report for today
    Given I am logged into the RAVS app
    And I login to RAVS and set vaccinator details with <site> and <care_model> and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
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
    And the immunisation history of the patient should be updated in the patient details page and not be deleted
    When I click the reports navigation link
    And I click the create report button
    And I click the Today radio button and click Continue
    And I select the vaccine type <chosen_vaccine> and click continue
    And I select the site <site> and click continue
    And I click continue on the data page
    And I click Confirm and create report button in the check and confirm page
    And I click download report button
    Then the report is downloaded successfully and contains the vaccine record for <nhs_number>

  Examples:
    | index | nhs_number | site | care_model | eligibility | assess_date | consent | vaccination | vaccination_date | name    | dob        | address                                       | chosen_vaccine | batch_number     | batch_expiry_date |
    | 0  | 9693632109 | Albert House | Vaccination Centre open to the public | yes        | today      | yes     | yes         | today | Bill GARTON | 23/6/1946 | 1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | COVID-19  | AUTOMATION-SJ1   | 19/10/2026   |
    | 0  | 9693632109 | Albert House | Vaccination Centre open to the public | yes        | today      | yes     | yes         | today-32 | Bill GARTON | 23/6/1946 | 1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | COVID-19  | AUTOMATION-SJ1   | 19/10/2026   |

  Scenario Outline: Record a vaccine and generate a report for no vaccination decision on the last screen
    Given I am logged into the RAVS app
    And I login to RAVS and set vaccinator details with <site> and <care_model> and get patient details for <nhs_number> with option <index> and choose to vaccinate with vaccine details as <chosen_vaccine>, <batch_number> with <batch_expiry_date>
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    When I click choose vaccine button and choose the <chosen_vaccine>, <batch_number> with <batch_expiry_date> and click continue
    And I assess the patient's <eligibility> with the details and date as <assess_date> and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I record <vaccination> details and date as <vaccination_date> and click Save and return button
    Then I search for a patient with the NHS number in the find a patient screen
    And I open the patient record by clicking on patient <name>
    And the immunisation history of the patient should be updated in the patient details page and not be deleted
    When I click the reports navigation link
    And I click the create report button
    And I click the Today radio button and click Continue
    And I select the vaccine type <chosen_vaccine> and click continue
    And I select the site <site> and click continue
    And I click continue on the data page
    And I click Confirm and create report button in the check and confirm page
    And I click download report button
    Then the report is downloaded successfully and contains the vaccine record for <nhs_number>

  Examples:
    | index | nhs_number | site | care_model | eligibility | assess_date | consent | vaccination | vaccination_date | name    | dob        | address                                       | chosen_vaccine | batch_number     | batch_expiry_date |
    | 4 | 9437541817 | KINGSTON HOUSE  | Outreach event | yes | today | yes | no | today | FLORINDA DUNNER |  27/3/1957 | 32 HOLLAND ROAD, MANCHESTER, M8 4NP | Flu | AUTOMATION-SJ1 | 19/10/2026 |


  Scenario Outline: User should be able to filter vaccine event data before creating a report
  Given I am logged into the RAVS app
  When I click the reports navigation link
  And I click the create report button
  And I click the <day> radio button and click Continue
  And I select the vaccine type <vaccineType> and click continue
  And I select the site <site> and click continue
  And I select the data <data> to filter and click continue
  And I click Confirm and create report button in the check and confirm page
  And I click download report button
  Then the report is downloaded successfully and it should not contain the data that was selected for filtering

  Examples:
  |vaccineType                        | site          | day                            |   data   |
  | COVID-19                          | Albert House  | Last 31 days (includes today)  | Patients |
  | Flu                               | Albert House  | Last 31 days (includes today)  | Staff    |
  | Pertussis                         | Albert House  | Last 7 days (includes today)   | Site or delivery team |
  | Respiratory syncytial virus (RSV) | Albert House  | Last 14 days (includes today)  | Assessment and consent |
  | COVID-19                          | Albert House  | Last 31 days (includes today)  | Vaccination |

