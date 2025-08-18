Feature: Find a patient

  Background:
    Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>

  @findpatient
  Scenario: Find a patient page should launch
    When I click the find a patient navigation link
    Then the find a patient page should be displayed

    Examples:
      | care_model         | user_role          | site                         |
      | Trust site         | lead administrator | Weaverham Surgery            |
      | Community pharmacy | administrator      | Aspire Pharmacy              |
      | Branch surgery     | recorder           | Aire Valley Surgery (Rawdon) |

  @findpatient
  Scenario: Search without entering nhs number
    Given I am on the find a patient by nhs number page
    When I click the search button
    Then the alert message should appear for nhs number

    Examples:
      | care_model         | user_role          | site                         |
      | Trust site         | lead administrator | Weaverham Surgery            |
      | Community pharmacy | administrator      | Aspire Pharmacy              |
      | Branch surgery     | recorder           | Aire Valley Surgery (Rawdon) |

  @findpatient
  @skip
  # Skipped due to bug: Incorrect error messaging on demographic search
  Scenario: Search without entering patient details
    Given I am on the find a patient by pds details page
    When I click the search button
    Then the alert messages should appear for Forename, Surname, Date Of Birth, Gender and Postcode

    Examples:
      | care_model         | user_role          | site                         |
      | Trust site         | lead administrator | Weaverham Surgery            |
      | Community pharmacy | administrator      | Aspire Pharmacy              |
      | Branch surgery     | recorder           | Aire Valley Surgery (Rawdon) |

  @findpatient
  Scenario Outline: Search by NHS number
    Given I am on the find a patient by nhs number page
    When I enter a valid <nhsNumber>
    And I click the search button
    Then I should be directed to the patient's information page and show <name>, <nhsNumber>, <dateofbirth> and <address> details

    Examples:
      | nhsNumber  | name          | dateofbirth | address                                      | care_model         | user_role          | site                         |
      | 5997998967 | JACKIE WALKER | 6/12/1953   | 9 Islington High Street Verwood, PA, NN6 6NZ | Trust site         | lead administrator | Weaverham Surgery            |
      | 5998005341 | ELVIN MANSELL | 6/12/1953   | Ilfracombe 7 Goodge Street Mo, MO, YO26 5JZ  | Community pharmacy | administrator      | Aspire Pharmacy              |
      | 5998019903 | OAKLEY UDDIN  | 2/6/1953    | 31 Earl'S Court Road Hatfield, MD, YO22 4EG  | Branch surgery     | recorder           | Aire Valley Surgery (Rawdon) |
  # | 5990365624 | DALLAS KING      |   30/6/2024 |  10 NORTON PARK VIEW, SHEFFIELD, S8 8GS                       | Trust site         | lead administrator |Weaverham Surgery             |
  # | 9449306621 | Not found        |    20110509 |  KT21 1LJ                                                     | Community pharmacy | administrator      |Aspire Pharmacy               |
  # | 9449306605 | Srinivasarao Patel |  03/03/2020 |  4 Calicut Lane2, Line 2, Line 3, SLOUGH, Berkshire, KT21 1EJ | Branch surgery   | recorder           |
  # | 9449306494 | Reynolds Ryan    |   27/3/2001 |  Jamie Street, Jaketown, KDDTG5, SW16 6JR                     | Trust site         | lead administrator |Weaverham Surgery             |
  # | 5990378017 | WHITNEY CLARKE   |    20160130 |  10 BROOK STREET, LANCASTER, LA1 1SL                          | Community pharmacy | administrator      |Aspire Pharmacy               |
  # | 9469998626 | JONNY CONOPO     |    20150305 |  1 DAISY BANK, LANCASTER, LA1 3JW                             | Branch surgery     | recorder           |
  # | 5990376766 | KAYABI KERRABI        |    20150706 |  01, Moore, Bishop, Essex, N8 7RE               | Trust site         | lead administrator |Weaverham Surgery             |
  # | 5990365004 | ALANA MRAZ       |    20150222 |  CAMPUS CITY NEW CAMPUS 41 BERKELEY ROAD, WESTBURY PARK, Manchester, M16 0RA                 | Community pharmacy | administrator      |Aspire Pharmacy               |
  # | 5990366043 | AINSLEY INGHAM     |    20151209 |  CAMPUS CITY NEW CAMPUS 41 BERKELEY ROAD, WESTBURY PARK, Manchester, M16 0RA             | Branch surgery     | recorder           |
  # | 9470011902 | KATEE TUZZIO     |    20150527 |  BRIDGE END HOUSE, PARK ROAD, MILNTHORPE, CUMBRIA, LA7 7AN    | Trust site         | lead administrator |Weaverham Surgery             |
  # | 9470032640 | SYBIL PELLING    |    20151217 |  50 ST. GEORGES QUAY, LANCASTER, LA1 1SA                      | Community pharmacy | administrator      |Aspire Pharmacy               |


  @findpatient
  Scenario Outline: NHS Number: Searching with invalid NHS number shows an error
    Given I am on the find a patient by nhs number page
    And I enter <nhsNumber> as the nhs number
    When I click the search button
    Then I can see an nhs number error message <errorMessage>

    Examples:
      | nhsNumber  | errorMessage               | care_model         | user_role          | site                         |
      | 123456789  | Enter 10 digits            | Trust site         | lead administrator | Weaverham Surgery            |
      | 9753108642 | Enter a correct NHS number | Community pharmacy | administrator      | Aspire Pharmacy              |
      | 123456789  | Enter 10 digits            | Branch surgery     | recorder           | Aire Valley Surgery (Rawdon) |


  @findpatient
  Scenario Outline: NHS Number: Searching for a patient without a record returns no results
    Given I am on the find a patient by nhs number page
    And I enter <nhsNumber> as the nhs number
    When I click the search button
    Then I can see a message that no results are found for the NHS number <nhsNumber>
    And I can see an option to create a new patient

    Examples:
      | nhsNumber  | care_model         | user_role          | site                         |
      | 9449306621 | Trust site         | lead administrator | Weaverham Surgery            |
      | 9449306621 | Community pharmacy | administrator      | Aspire Pharmacy              |
      | 9449306621 | Branch surgery     | recorder           | Aire Valley Surgery (Rawdon) |

  ### This test is not needed as it is a duplicate
  # @findpatient
  # Scenario Outline: NHS Number: Existing patients can be found using their NHS number
  #   Given I am on the find a patient by nhs number page
  #   And I enter <nhsNumber> as the nhs number
  #   When I click the search button
  #   Then I can see the patient's information in the search results, showing their name: <name>, nhs number: <nhsNumber>, dob: <dateofbirth> and address: <address>

  #   Examples:
  #     | nhsNumber  | name      | dateofbirth | address                                                    |
  #     | 5997998967 | JACKIE WALKER |   6/12/1953 | 9 Islington High Street Verwood, PA, NN6 6NZ |

  @findpatient
  Scenario Outline: Demographics: Existing patients can be found using their mandatory demographic details
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details <firstName>, <lastName> and <dob>
    When I click the search button
    Then I can see the patient's information in the search results, showing their name: <firstName> <lastName>, nhs number: <nhsNumber>, dob: <dob> and address: <address>

    Examples:
      | nhsNumber  | care_model         | user_role          | firstName | lastName       | dob       | address                                   |
      | 9449303762 | Trust site         | lead administrator | Pryderi   | Warnford-Davis | 14/4/2001 | 1 CRANLEIGH ROAD, ESHER, SURREY, KT10 8DF |
      | 9449303762 | Community pharmacy | administrator      | Pryderi   | Warnford-Davis | 14/4/2001 | 1 CRANLEIGH ROAD, ESHER, SURREY, KT10 8DF |
      | 9449303762 | Branch surgery     | recorder           | Pryderi   | Warnford-Davis | 14/4/2001 | 1 CRANLEIGH ROAD, ESHER, SURREY, KT10 8DF |


  @findpatient
  Scenario Outline: Demographics: Existing patients can be found using their optional demographic details
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details <firstName>, <lastName> and <dob>
    And I enter the postcode <postcode>
    And I select the gender <gender>
    When I click the search button
    Then I can see the patient's information in the search results, showing their name: <firstName> <lastName>, nhs number: <nhsNumber>, dob: <dob> and address: <address>

    Examples:
      | nhsNumber  | care_model         | user_role          | firstName | lastName       | dob       | address                                   | site                         | postcode |
      | 9449303762 | Trust site         | lead administrator | Pryderi   | Warnford-Davis | 14/4/2001 | 1 CRANLEIGH ROAD, ESHER, SURREY, KT10 8DF | Weaverham Surgery            | KT10 8DF |
      | 9449303762 | Community pharmacy | administrator      | Pryderi   | Warnford-Davis | 14/4/2001 | 1 CRANLEIGH ROAD, ESHER, SURREY, KT10 8DF | Aspire Pharmacy              | KT10 8DF |
      | 9449303762 | Branch surgery     | recorder           | Pryderi   | Warnford-Davis | 14/4/2001 | 1 CRANLEIGH ROAD, ESHER, SURREY, KT10 8DF | Aire Valley Surgery (Rawdon) | KT10 8DF |


  @findpatient
  Scenario Outline: Demographics: Search does not find existing patients if any of their details are wrong
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details <firstName>, <lastName> and <dob>
    And I enter the postcode <postcode>
    And I select the gender <gender>
    When I click the search button
    Then I can see a message that no results are found for the patient
    And I can see an option to create a new patient

    Examples:
      | scenario    | nhsNumber  | care_model         | user_role          | firstName | lastName | dob        | postcode | gender | site                         |
      | first name  | 5997998967 | Trust site         | lead administrator | Bob       | Garton   | 23/6/1946  | DN18 5DW | Male   | Weaverham Surgery            |
      | last name   | 5997998967 | Community pharmacy | administrator      | Bill      | Gartoni  | 23/6/1946  | DN18 5DW | Male   | Aspire Pharmacy              |
      | dob - day   | 5997998967 | Branch surgery     | recorder           | Bill      | Garton   | 3/6/1946   | DN18 5DW | Male   | Aire Valley Surgery (Rawdon) |
      | dob - month | 5997998967 | Branch surgery     | recorder           | Bill      | Garton   | 23/12/1946 | DN18 5DW | Male   | Aire Valley Surgery (Rawdon) |
      | dob - year  | 5997998967 | Branch surgery     | recorder           | Bill      | Garton   | 23/6/1991  | DN18 5DW | Male   | Aire Valley Surgery (Rawdon) |
      | postcode    | 5997998967 | Branch surgery     | recorder           | Bill      | Garton   | 23/6/1946  | M6 3AA   | Male   | Aire Valley Surgery (Rawdon) |
      | gender      | 5997998967 | Trust site         | administrator      | Bill      | Garton   | 23/6/1946  | DN18 5DW | Female | Weaverham Surgery            |


  @findpatient
  @skip
  # Skipped due to bug: Incorrect error messaging on demographic search
  Scenario Outline: Demographics: Search without entering patient details shows errors on the mandatory fields
    Given I am on the find a patient by demographics page
    When I click the search button
    Then I can see a first name error message <firstNameError>
    And I can see a last name error message <lastNameError>
    And I can see a dob error message <dobError>

    Examples:
      | firstNameError       | lastNameError       | dobError                | care_model     | user_role | site                         |
      | Enter the first name | Enter the last name | Enter the date of birth | Branch surgery | recorder  | Aire Valley Surgery (Rawdon) |

  @findpatient
  Scenario Outline: Demographics: Search with an invalid postcode shows an error message
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details <firstName>, <lastName> and <dob>
    When I enter the postcode INVALID
    When I click the search button
    Then I can see a postcode error message Enter the full postcode in the correct format

    Examples:
      | firstName | lastName | dob       | postcode | care_model         | user_role          | site                         |
      | Bill      | Garton   | 23/6/1946 | INVALID  | Trust site         | lead administrator | Weaverham Surgery            |
      | Bill      | Garton   | 23/6/1946 | INVALID  | Community pharmacy | administrator      | Aspire Pharmacy              |
      | Bill      | Garton   | 23/6/1946 | INVALID  | Branch surgery     | recorder           | Aire Valley Surgery (Rawdon) |

  @findpatient
  Scenario Outline: Demographics: Multiple demographic matches shows an error that more than one result is found
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details <firstName>, <lastName> and <dob>
    When I click the search button
    Then I can see a message that more than one result was found

    Examples:
      | firstName | lastName | dob        | care_model         | user_role          | site                         |
      | Aidan     | Smith    | 23/02/2020 | Trust site         | lead administrator | Weaverham Surgery            |
      | Aidan     | Smith    | 23/02/2020 | Community pharmacy | administrator      | Aspire Pharmacy              |
      | Aidan     | Smith    | 23/02/2020 | Branch surgery     | recorder           | Aire Valley Surgery (Rawdon) |

  @findpatient
  Scenario Outline: Demographics: Can search for a patient by their old name, after a name change
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details <firstName>, <lastName> and <dob>
    When I click the search button
    Then I can see the patient's information in the search results, showing their name: <newName>, nhs number: <nhsNumber>, dob: <dob> and address: <address>

    Examples:
      | firstName | lastName  | dob        | newName       | nhsNumber  | address                                 | care_model         | user_role     | site            |
      | Joan      | Robertson | 19/09/1972 | Poppy Roberts | 9449310076 | 1 Canada Road, COBHAM, Surrey, LS15 4LJ | Community pharmacy | administrator | Aspire Pharmacy |

  @findpatient
  Scenario Outline: Demographics: Searching for a patient without a record returns no results
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details <firstName>, <lastName> and <dob>
    When I click the search button
    Then I can see a message that no results are found for the patient
    And I can see an option to create a new patient

    Examples:
      | firstName | lastName | dob        | care_model     | user_role | site                         |
      | Cecile    | Elston   | 18/01/1965 | Branch surgery | recorder  | Aire Valley Surgery (Rawdon) |

  @findpatient @createpatient
  Scenario Outline: Local: Searching for a patient without a record returns no results
    Given I am on the find a patient by local records page
    And I enter the mandatory patient details <firstName>, <lastName> and <dob>
    When I click the search button
    Then I can see a message that no results are found for the patient
    #  And I can see an option to create a new patient

    Examples:
      | firstName | lastName | dob        | care_model | user_role          | site              |
      | John      | Preston  | 14/03/2003 | Trust site | lead administrator | Weaverham Surgery |

  @findpatient @createpatient
  Scenario: Local: Created patient can be found using local search
    Given I am on the find a patient by demographics page
    And I generate random data for a new patient
    And I enter the new patient details on find by demographics page
    And I click the search button
    And I click the create a new patient button
    And I enter the new patient details on create a new patient page
    When I click the check and confirm button
    Then I can check and confirm the patient information is correct
    When I click the confirm and save button
    Then I can see the patient added confirmation message
    And I click the find a patient by local records link
    And I enter the new patient details
    When I click the search button
    Then I can see the patient's local record in the search results

  @sflag
  Scenario Outline: Sensitive information should be hidden for S-flag patients
    Given I am on the find a patient by nhs number page
    When I enter a valid <nhsNumber>
    And I click the search button
    And I open the patient record by clicking on patient <name>
    Then the patient's phone-number, address and site information should not be visible

    Examples:
      | nhsNumber  | name                               | dateofbirth | address | care_model         | user_role          | site                         |
      | 9450127077 | LUDMILLA MCKSN-PDS-ALPHA-SENSITIVE | 2/5/1974    |         | Trust site         | lead administrator | Weaverham Surgery            |
      | 5558785314 | ANDRE SANTOS                       | 1/1/1991    |         | Community pharmacy | administrator      | Aspire Pharmacy              |
      | 5558785314 | ANDRE SANTOS                       | 1/1/1991    |         | Branch surgery     | recorder           | Aire Valley Surgery (Rawdon) |
