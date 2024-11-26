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

Scenario Outline: Check and confirm page is displayed
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
