Feature: Find a patient

  Background:
  Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>

@findpatient
Scenario: Find a patient page should launch
  When I click the find a patient navigation link
  Then the find a patient page should be displayed

    Examples:
    | care_model          |  user_role          | site                          |
    | Trust site          |  lead administrator | Weaverham Surgery             |
    | Community pharmacy  |       administrator | Aspire Pharmacy               |
    | Branch surgery      |       recorder      | Aire Valley Surgery (Rawdon)  |

@findpatient
Scenario: Search without entering nhs number
  Given I am on the find a patient by nhs number page
  When I click the search button
  Then the alert message should appear for nhs number

    Examples:
    | care_model          |  user_role          | site                          |
    | Trust site          |  lead administrator | Weaverham Surgery             |
    | Community pharmacy  |       administrator | Aspire Pharmacy               |
    | Branch surgery      |       recorder      | Aire Valley Surgery (Rawdon)  |

@findpatient
@skip
# Skipped due to bug: Incorrect error messaging on demographic search
Scenario: Search without entering patient details
  Given I am on the find a patient by pds details page
  When I click the search button
  Then the alert messages should appear for Forename, Surname, Date Of Birth, Gender and Postcode

    Examples:
    | care_model          |  user_role          | site                          |
    | Trust site          |  lead administrator | Weaverham Surgery             |
    | Community pharmacy  |       administrator | Aspire Pharmacy               |
    | Branch surgery      |       recorder      | Aire Valley Surgery (Rawdon)  |

@findpatient
Scenario Outline: Search by NHS number
  Given I am on the find a patient by nhs number page
  When I enter a valid <nhsNumber>
  And I click the search button
  Then I should be directed to the patient's information page and show <name>, <nhsNumber>, <dateofbirth> and <address> details

  Examples:
| nhsNumber  | name             | dateofbirth | address                                                       | care_model         | user_role          |site                          |
| 9693632109 | Bill GARTON      |   23/6/1946 |  1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW   | Trust site         | lead administrator |Weaverham Surgery             |
| 9732743476 | Mike HEESOM      |  24/10/1992 |  2 CHAPEL YARD, BRIGG, S HUMBERSIDE, DN20 8JY                 | Community pharmacy | administrator      |Aspire Pharmacy               |
| 9650594000 | Archie STRAIN    |   30/7/2014 |  1 CONINGSBY DRIVE, GRIMSBY, S HUMBERSIDE, DN34 5HQ           | Branch surgery     | recorder           | Aire Valley Surgery (Rawdon)  |
# | 9732596996 | Lisa WORTHY      |   30/6/2024 |  10 NORTON PARK VIEW, SHEFFIELD, S8 8GS                       | Trust site         | lead administrator |Weaverham Surgery             |
# | 9449306621 | Not found        |    20110509 |  KT21 1LJ                                                     | Community pharmacy | administrator      |Aspire Pharmacy               |
# | 9449306605 | Srinivasarao Patel |  03/03/2020 |  4 Calicut Lane2, Line 2, Line 3, SLOUGH, Berkshire, KT21 1EJ | Branch surgery   | recorder           |
# | 9449306494 | Reynolds Ryan    |   27/3/2001 |  Jamie Street, Jaketown, KDDTG5, SW16 6JR                     | Trust site         | lead administrator |Weaverham Surgery             |
# | 9469997956 | SOLOMON DAZLEY   |    20160130 |  10 BROOK STREET, LANCASTER, LA1 1SL                          | Community pharmacy | administrator      |Aspire Pharmacy               |
# | 9469998626 | JONNY CONOPO     |    20150305 |  1 DAISY BANK, LANCASTER, LA1 3JW                             | Branch surgery     | recorder           |
# | 9470004272 | JOJO LANE        |    20150706 |  10 RAKESMOOR LANE, BARROW-IN-FURNESS, LA14 4LG               | Trust site         | lead administrator |Weaverham Surgery             |
# | 9470006143 | TABBY FERN       |    20150222 |  CLEAR BECK HOUSE, TATHAM, LANCASTER, LA2 8PJ                 | Community pharmacy | administrator      |Aspire Pharmacy               |
# | 9470006739 | JANNETTE ARD     |    20151209 |  1 ST. MARTINS COURT, CONISTON, CUMBRIA, LA21 8HZ             | Branch surgery     | recorder           |
# | 9470011902 | KATEE TUZZIO     |    20150527 |  BRIDGE END HOUSE, PARK ROAD, MILNTHORPE, CUMBRIA, LA7 7AN    | Trust site         | lead administrator |Weaverham Surgery             |
# | 9470032640 | SYBIL PELLING    |    20151217 |  50 ST. GEORGES QUAY, LANCASTER, LA1 1SA                      | Community pharmacy | administrator      |Aspire Pharmacy               |


@findpatient
Scenario Outline: NHS Number: Searching with invalid NHS number shows an error
  Given I am on the find a patient by nhs number page
  And I enter <nhsNumber> as the nhs number
  When I click the search button
  Then I can see an nhs number error message <errorMessage>

Examples:
  | nhsNumber  | errorMessage                | care_model         | user_role          | site                          |
  | 123456789  | Enter 10 digits             | Trust site         | lead administrator | Weaverham Surgery             |
  | 9753108642 | Enter a correct NHS number  | Community pharmacy | administrator      | Aspire Pharmacy               |
  | 123456789  | Enter 10 digits             | Branch surgery     | recorder           | Aire Valley Surgery (Rawdon)  |


@findpatient
Scenario Outline: NHS Number: Searching for a patient without a record returns no results
  Given I am on the find a patient by nhs number page
  And I enter <nhsNumber> as the nhs number
  When I click the search button
  Then I can see a message that no results are found for the NHS number <nhsNumber>
  And I can see an option to create a new patient

Examples:
  | nhsNumber   | care_model         | user_role          | site                          |
  | 9449306621  | Trust site         | lead administrator | Weaverham Surgery             |
  | 9449306621  | Community pharmacy | administrator      | Aspire Pharmacy               |
  | 9449306621  | Branch surgery     | recorder           | Aire Valley Surgery (Rawdon)  |

### This test is not needed as it is a duplicate
  # @findpatient
  # Scenario Outline: NHS Number: Existing patients can be found using their NHS number
  #   Given I am on the find a patient by nhs number page
  #   And I enter <nhsNumber> as the nhs number
  #   When I click the search button
  #   Then I can see the patient's information in the search results, showing their name: <name>, nhs number: <nhsNumber>, dob: <dateofbirth> and address: <address>

  #   Examples:
  #     | nhsNumber  | name      | dateofbirth | address                                                    |
  #     | 9693632109 | Bill GARTON |   23/6/1946 | 1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW |

@findpatient
Scenario Outline: Demographics: Existing patients can be found using their mandatory demographic details
  Given I am on the find a patient by demographics page
  And I enter the mandatory patient details <firstName>, <lastName> and <dob>
  When I click the search button
  Then I can see the patient's information in the search results, showing their name: <firstName> <lastName>, nhs number: <nhsNumber>, dob: <dob> and address: <address>

Examples:
  | nhsNumber   | care_model         | user_role          | firstName | lastName        | dob        | address                                  |
  | 9449303762  | Trust site         | lead administrator | Pryderi   | Warnford-Davis  | 14/4/2001 | 1 CRANLEIGH ROAD, ESHER, SURREY, KT10 8DF |
  | 9449303762  | Community pharmacy | administrator      | Pryderi   | Warnford-Davis  | 14/4/2001 | 1 CRANLEIGH ROAD, ESHER, SURREY, KT10 8DF |
  | 9449303762  | Branch surgery     | recorder           | Pryderi   | Warnford-Davis  | 14/4/2001 | 1 CRANLEIGH ROAD, ESHER, SURREY, KT10 8DF |


@findpatient
Scenario Outline: Demographics: Existing patients can be found using their optional demographic details
  Given I am on the find a patient by demographics page
  And I enter the mandatory patient details <firstName>, <lastName> and <dob>
  And I enter the postcode <postcode>
  And I select the gender <gender>
  When I click the search button
  Then I can see the patient's information in the search results, showing their name: <firstName> <lastName>, nhs number: <nhsNumber>, dob: <dob> and address: <address>

Examples:
  | nhsNumber   | care_model         | user_role          | firstName | lastName        | dob        | address                                  | site                          | postcode |
  | 9449303762  | Trust site         | lead administrator | Pryderi   | Warnford-Davis  | 14/4/2001 | 1 CRANLEIGH ROAD, ESHER, SURREY, KT10 8DF | Weaverham Surgery             | KT10 8DF |
  | 9449303762  | Community pharmacy | administrator      | Pryderi   | Warnford-Davis  | 14/4/2001 | 1 CRANLEIGH ROAD, ESHER, SURREY, KT10 8DF | Aspire Pharmacy               | KT10 8DF |
  | 9449303762  | Branch surgery     | recorder           | Pryderi   | Warnford-Davis  | 14/4/2001 | 1 CRANLEIGH ROAD, ESHER, SURREY, KT10 8DF | Aire Valley Surgery (Rawdon)  | KT10 8DF |


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
  | scenario    | nhsNumber   | care_model         | user_role          | firstName | lastName   | dob        | postcode | gender  | site                          |
  | first name  | 9693632109  | Trust site         | lead administrator | Bob       | Garton     | 23/6/1946  | DN18 5DW | Male    | Weaverham Surgery             |
  | last name   | 9693632109  | Community pharmacy | administrator      | Bill      | Gartoni    | 23/6/1946  | DN18 5DW | Male    | Aspire Pharmacy               |
  | dob - day   | 9693632109  | Branch surgery     | recorder           | Bill      | Garton     | 3/6/1946   | DN18 5DW | Male    | Aire Valley Surgery (Rawdon)  |
  | dob - month | 9693632109  | Branch surgery     | recorder           | Bill      | Garton     | 23/12/1946 | DN18 5DW | Male    | Aire Valley Surgery (Rawdon)  |
  | dob - year  | 9693632109  | Branch surgery     | recorder           | Bill      | Garton     | 23/6/1991  | DN18 5DW | Male    | Aire Valley Surgery (Rawdon)  |
  | postcode    | 9693632109  | Branch surgery     | recorder           | Bill      | Garton     | 23/6/1946  | M6 3AA   | Male    | Aire Valley Surgery (Rawdon)  |
  | gender      | 9693632109  | Trust site         | administrator      | Bill      | Garton     | 23/6/1946  | DN18 5DW | Female  | Weaverham Surgery             |


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
  | firstNameError        | lastNameError        | dobError                 | care_model         | user_role          | site                          |
  | Enter the first name  | Enter the last name  | Enter the date of birth  | Branch surgery     | recorder           | Aire Valley Surgery (Rawdon)  |

@findpatient
Scenario Outline: Demographics: Search with an invalid postcode shows an error message
  Given I am on the find a patient by demographics page
  And I enter the mandatory patient details <firstName>, <lastName> and <dob>
  When I enter the postcode INVALID
  When I click the search button
  Then I can see a postcode error message Enter the full postcode in the correct format

Examples:
  | firstName | lastName | dob        | postcode | care_model         | user_role          | site                          |
  | Bill      | Garton   | 23/6/1946  | INVALID  | Trust site         | lead administrator | Weaverham Surgery             |
  | Bill      | Garton   | 23/6/1946  | INVALID  | Community pharmacy | administrator      | Aspire Pharmacy               |
  | Bill      | Garton   | 23/6/1946  | INVALID  | Branch surgery     | recorder           | Aire Valley Surgery (Rawdon)  |

@findpatient
Scenario Outline: Demographics: Multiple demographic matches shows an error that more than one result is found
  Given I am on the find a patient by demographics page
  And I enter the mandatory patient details <firstName>, <lastName> and <dob>
  When I click the search button
  Then I can see a message that more than one result was found

Examples:
  | firstName | lastName | dob        | care_model         | user_role          | site                        |
  | Aidan     | Smith    | 23/02/2020 | Trust site         | lead administrator | Weaverham Surgery           |
  | Aidan     | Smith    | 23/02/2020 | Community pharmacy | administrator      | Aspire Pharmacy             |
  | Aidan     | Smith    | 23/02/2020 | Branch surgery     | recorder           | Aire Valley Surgery (Rawdon)|

@findpatient
Scenario Outline: Demographics: Can search for a patient by their old name, after a name change
  Given I am on the find a patient by demographics page
  And I enter the mandatory patient details <firstName>, <lastName> and <dob>
  When I click the search button
  Then I can see the patient's information in the search results, showing their name: <newName>, nhs number: <nhsNumber>, dob: <dob> and address: <address>

Examples:
  | firstName | lastName  | dob      | newName      | nhsNumber  | address                                   | care_model         | user_role           | site |
  | Joan      | Robertson | 19/09/1972 | Poppy Roberts | 9449310076 | 1 Canada Road, COBHAM, Surrey, LS15 4LJ | Community pharmacy | administrator      | Aspire Pharmacy          |

@findpatient
Scenario Outline: Demographics: Searching for a patient without a record returns no results
  Given I am on the find a patient by demographics page
  And I enter the mandatory patient details <firstName>, <lastName> and <dob>
  When I click the search button
  Then I can see a message that no results are found for the patient
  And I can see an option to create a new patient

Examples:
  | firstName | lastName | dob        | care_model         | user_role          | site |
  | Cecile    | Elston   | 18/01/1965 | Branch surgery     | recorder           | Aire Valley Surgery (Rawdon) |

@findpatient @createpatient
Scenario Outline: Local: Searching for a patient without a record returns no results
  Given I am on the find a patient by local records page
  And I enter the mandatory patient details <firstName>, <lastName> and <dob>
  When I click the search button
  Then I can see a message that no results are found for the patient
    #  And I can see an option to create a new patient

Examples:
  | firstName | lastName | dob        | care_model         | user_role          | site |
  | John      | Preston  | 14/03/2003 | Trust site         | lead administrator | Weaverham Surgery           |

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
  | nhsNumber  | name                                    | dateofbirth | address | care_model         | user_role          | site                        |
  | 9450127077 | LUDMILLA MCKSN-PDS-ALPHA-SENSITIVE      | 2/5/1974    |         | Trust site         | lead administrator | Weaverham Surgery           |
  | 9733907723 | Sandra Ryan                             | 7/4/1994    |         | Community pharmacy | administrator      | Aspire Pharmacy             |
  | 9733907723 | Sandra Ryan                             | 7/4/1994    |         | Branch surgery     | recorder           | Aire Valley Surgery (Rawdon)|
