Feature: Find a patient

  @findpatient
  Scenario Outline: NHS Number: Searching with invalid NHS number shows an error
    Given I am on the find a patient by nhs number page
    And I enter <nhsNumber> as the nhs number
    Given I click the search button
    Then I can see an nhs number error message <errorMessage>

    Examples:
      | nhsNumber  | errorMessage                       |
      |  123456789 | Minimum number of characters is 10 |
      | 9753108642 | Invalid NHS number                 |

  @findpatient
  Scenario: NHS Number: Searching for a patient without a record returns no results
    Given I am on the find a patient by nhs number page
    And I enter 9449306621 as the nhs number
    Given I click the search button
    Then I can see a message that no results are found for the NHS number 9449306621
    And I can see an option to create a new patient

  @findpatient
  Scenario Outline: NHS Number: Existing patients can be found using their NHS number
    Given I am on the find a patient by nhs number page
    And I enter <nhsNumber> as the nhs number
    Given I click the search button
    Then I can see the patient's information in the search results, showing their name: <name>, nhs number: <nhsNumber>, dob: <dateofbirth> and address: <address>

    Examples:
      | nhsNumber  | name               | dateofbirth | address                                                             |
      | 9693632109 | Bill GARTON        |   23/6/1946 |          1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW |

  @findpatient
  Scenario Outline: Demographics: Existing patients can be found using their mandatory demographic details
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details <firstName>, <lastName>, and <dob>
    Given I click the search button
    Then I can see the patient's information in the search results, showing their name: <firstName> <lastName>, nhs number: <nhsNumber>, dob: <dob> and address: <address>

    Examples:
      | nhsNumber  | firstName | lastName       | dob        | address                                                       |
      | 9449303762 | Pryderi   | Warnford-Davis | 14/04/2001 |                     1 CRANLEIGH ROAD, ESHER, SURREY, KT10 8DF |

  @findpatient
  Scenario Outline: Demographics: Existing patients can be found using their optional demographic details
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details <firstName>, <lastName>, and <dob>
    And I enter the postcode <postcode>
    And I select the gender <gender>
    Given I click the search button
    Then I can see the patient's information in the search results, showing their name: <firstName> <lastName>, nhs number: <nhsNumber>, dob: <dob> and address: <address>

    Examples:
      | nhsNumber  | firstName | lastName | dob        | address                                                         | postcode | gender |
      | 9693632109 | Bill      | Garton   |  23/6/1946 |      1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | DN18 5DW | Male   |
      | 9470006739 | JANNETTE  | ARD      | 09/12/2015 |                1 ST. MARTINS COURT, CONISTON, CUMBRIA, LA21 8HZ | LA21 8HZ | Other  |

  @findpatient
  Scenario Outline: Demographics: Search does not find existing patients if any of their details are wrong
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details <firstName>, <lastName>, and <dob>
    Given I enter postcode <postcode>
    And I select the gender <gender>
    Given I click the search button
    Then I can see a message that no results are found for the patient
    And I can see an option to create a new patient

    Examples:
      | scenario    | firstName | lastName | dob        | postcode | gender  |
      | first name  | Bob       | Garton   |  23/6/1946 | DN18 5DW | Male    |
      | last name   | Bill      | Gartoni  |  23/6/1946 | DN18 5DW | Male    |
      | dob - day   | Bill      | Garton   |   3/6/1946 | DN18 5DW | Male    |
      | dob - month | Bill      | Garton   | 23/12/1946 | DN18 5DW | Male    |
      | dob - year  | Bill      | Garton   |  23/6/1991 | DN18 5DW | Male    |
      | postcode    | Bill      | Garton   |  23/6/1946 | M6 3AA   | Male    |
      | gender      | Bill      | Garton   |  23/6/1946 | DN18 5DW | Female  |
      | gender      | Bill      | Garton   |  23/6/1946 | DN18 5DW | Other   |
      | gender      | Bill      | Garton   |  23/6/1946 | DN18 5DW | Unknown |

  @findpatient
  Scenario: Demographics: Search without entering patient details shows errors on the mandatory fields
    Given I am on the find a patient by demographics page
    Given I click the search button
    Then I can see a first name error message Enter the first name
    And I can see a last name error message Enter the last name
    And I can see a dob error message Enter the date of birth

  @findpatient
  Scenario: Demographics: Search with an invalid postcode shows an error message
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details Bill, Garton, and 23/6/1946
    When I enter the postcode INVALID
    Given I click the search button
    Then I can see a postcode error message Enter the full postcode in the correct format

  @findpatient
  Scenario: Demographics: Multiple demographic matches shows an error that more than one result is found
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details AIDAN, SMITH, and 23/02/2020
    Given I click the search button
    Then I can see a message that more than one result was found

  @findpatient
  Scenario: Demographics: Can search for a patient by their old name, after a name change
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details Joan, Robertson, and 19/09/1972
    Given I click the search button
    Then I can see the patient's information in the search results, showing their name: Poppy Roberts, nhs number: 9449310076, dob: 19/09/1972 and address: 1 Canada Road, COBHAM, Surrey, LS15 4LJ

  @findpatient
  Scenario: Demographics: Searching for a patient without a record returns no results
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details Cecile, Elston, and 18/01/1965
    Given I click the search button
    Then I can see a message that no results are found for the patient
    And I can see an option to create a new patient