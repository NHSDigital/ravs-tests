Feature: Reports

  @reports
  Scenario: Reports page is displayed
    Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>
    When I click the reports navigation link
    Then the reports page should be displayed

    Examples:
      | care_model         | user_role          | site                         |
      | Trust site         | lead administrator | Weaverham Surgery            |
      | Community pharmacy | administrator      | Aspire Pharmacy              |
      | Branch surgery     | administrator      | Aire Valley Surgery (Rawdon) |

  Scenario: Choose dates page is displayed
    Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>
    When I click the reports navigation link
    And I click the create report button
    Then the choose dates page should be displayed

    Examples:
      | care_model         | user_role          | site                         |
      | Trust site         | lead administrator | Weaverham Surgery            |
      | Community pharmacy | administrator      | Aspire Pharmacy              |
      | Branch surgery     | administrator      | Aire Valley Surgery (Rawdon) |

  Scenario Outline: "Choose vaccines" page is displayed
    Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>
    When I click the reports navigation link
    And I click the create report button
    And I click the <day> radio button and click Continue
    Then the choose vaccines page should be displayed

    Examples:
      | day                           | care_model         | user_role          | site                         |
      | Yesterday                     | Trust site         | lead administrator | Weaverham Surgery            |
      | Today                         | Trust site         | lead administrator | Weaverham Surgery            |
      | Last 7 days (includes today)  | Community pharmacy | administrator      | Aspire Pharmacy              |
      | Last 14 days (includes today) | Community pharmacy | administrator      | Aspire Pharmacy              |
      | Last 31 days (includes today) | Branch surgery     | administrator      | Aire Valley Surgery (Rawdon) |
  # skipped due to bug in report dates validation
  #| Select a custom date range up to 31 days | Branch surgery      | administrator      | Aire Valley Surgery (Rawdon)  |

  Scenario: User should not be able to proceed if no date range is selected
    Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>
    When I click the reports navigation link
    And I click the create report button
    And I select no date range and click Continue
    Then the user should not be able to proceed to choose a vaccine

    Examples:
      | care_model         | user_role          | site                         |
      | Trust site         | lead administrator | Weaverham Surgery            |
      | Community pharmacy | administrator      | Aspire Pharmacy              |
      | Branch surgery     | administrator      | Aire Valley Surgery (Rawdon) |

  Scenario Outline: Choose sites page is displayed
    Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>
    When I click the reports navigation link
    And I click the create report button
    And I click the today date range button and click continue
    And I select the vaccine type <vaccineType> and click continue
    Then the choose sites page should be displayed

    Examples:
      | vaccineType                       | care_model         | user_role          | site                         |
      | COVID-19                          | Trust site         | lead administrator | Weaverham Surgery            |
      | Flu                               | Trust site         | lead administrator | Weaverham Surgery            |
      | Pertussis                         | Community pharmacy | administrator      | Aspire Pharmacy              |
      | Respiratory syncytial virus (RSV) | Community pharmacy | administrator      | Aspire Pharmacy              |
      | COVID-19                          | Branch surgery     | administrator      | Aire Valley Surgery (Rawdon) |
      | Flu                               | Branch surgery     | administrator      | Aire Valley Surgery (Rawdon) |

  Scenario Outline: Check and confirm page should be displayed
    Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>
    When I click the reports navigation link
    And I click the create report button
    And I click the today date range button and click continue
    And I select the vaccine type <vaccineType> and click continue
    And I select the site <site> and click continue
    And I click continue on the data page
    Then the check and confirm page should be displayed

    Examples:
      | vaccineType                       | care_model         | user_role          | site                         |
      | COVID-19                          | Trust site         | lead administrator | Weaverham Surgery            |
      | Flu                               | Trust site         | lead administrator | Weaverham Surgery            |
      | Pertussis                         | Community pharmacy | administrator      | Aspire Pharmacy              |
      | Respiratory syncytial virus (RSV) | Community pharmacy | administrator      | Aspire Pharmacy              |
      | COVID-19                          | Branch surgery     | administrator      | Aire Valley Surgery (Rawdon) |
      | Flu                               | Branch surgery     | administrator      | Aire Valley Surgery (Rawdon) |


  Scenario Outline: Report is ready page should be displayed
    Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>
    When I click the reports navigation link
    And I click the create report button
    And I click the today date range button and click continue
    And I select the vaccine type <vaccineType> and click continue
    And I select the site <site> and click continue
    And I click continue on the data page
    And I click Confirm and create report button in the check and confirm page
    Then Creating your page element should be displayed and Download Report button should be visible

    Examples:
      | vaccineType                       | care_model         | user_role          | site                                                                              |
      | COVID-19                          | Trust site         | lead administrator | Weaverham Surgery                                                                 |
      | Flu                               | Trust site         | lead administrator | Weaverham Surgery                                                                 |
      | Pertussis                         | Community pharmacy | administrator      | Aspire Pharmacy                                                                   |
      | Respiratory syncytial virus (RSV) | Community pharmacy | administrator      | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service |
      | COVID-19                          | Branch surgery     | administrator      | Aire Valley Surgery (Rawdon)                                                      |
      | Flu                               | Branch surgery     | administrator      | Aire Valley Surgery (Rawdon)                                                      |

  Scenario Outline: User can download the report
    Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>
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
      | vaccineType                       | day                           | care_model         | user_role          | site                                                                              |
      | COVID-19                          | Last 31 days (includes today) | Trust site         | lead administrator | Weaverham Surgery                                                                 |
      | Flu                               | Last 31 days (includes today) | Trust site         | lead administrator | Weaverham Surgery                                                                 |
      | Pertussis                         | Last 7 days (includes today)  | Community pharmacy | administrator      | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service |
      | Respiratory syncytial virus (RSV) | Last 14 days (includes today) | Community pharmacy | administrator      | Aspire Pharmacy                                                                   |
  # skipped due to bug in report dates validation
  #| COVID-19                           | Select a custom date range up to 31 days  | Branch surgery      | administrator      | Aire Valley Surgery (Rawdon)  |

  Scenario: Reports navigation link should not be visible when logged in as recorder
    Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>
    Then reports navigation link should not be visible

    Examples:
      | care_model         | user_role | site                         |
      | Trust site         | recorder  | Weaverham Surgery            |
      | Community pharmacy | recorder  | Aspire Pharmacy              |
      | Branch surgery     | recorder  | Aire Valley Surgery (Rawdon) |

  Scenario: Reports navigation link should be visible when logged in as an administrator
    Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>
    Then reports navigation link should be visible

    Examples:
      | care_model         | user_role     | site                                                                              |
      | Trust site         | administrator | Weaverham Surgery                                                                 |
      | Community pharmacy | administrator | Aspire Pharmacy (The Concourse Shopping Centre) - Covid Local Vaccination Service |
      | Branch surgery     | administrator | Aire Valley Surgery (Rawdon)                                                      |

  Scenario: Create reports page should be visible when logged in as an administrator
    Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>
    When I click the reports navigation link
    Then the reports page should be displayed

    Examples:
      | care_model         | user_role     | site                         |
      | Trust site         | administrator | Weaverham Surgery            |
      | Community pharmacy | administrator | Aspire Pharmacy              |
      | Branch surgery     | administrator | Aire Valley Surgery (Rawdon) |

  Scenario Outline: Create report for an organization with no location sites
    Given I am logged into the RAVS app with the username <username>
    When I click the reports navigation link
    Then the `No vaccination data to report on` message should be displayed
    And the Create report button should be disabled

    Examples:
      | username                                      |
      | neelima.guntupalli1+no_location_sites@nhs.net |
