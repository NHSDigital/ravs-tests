Feature: Find a patient

  @findpatient
  Scenario Outline: NHS Number: Searching with invalid NHS number shows an error
    Given I am on the find a patient by nhs number page
    And I enter <nhsNumber> as the nhs number
    When I click the search button
    Then I can see an nhs number error message <errorMessage>

    Examples:
      | nhsNumber  | errorMessage                       |
      |  123456789 | Minimum number of characters is 10 |
      | 9753108642 | Invalid NHS number                 |

  @findpatient
  Scenario Outline: NHS Number: Searching for a patient without a record returns no results
    Given I am on the find a patient by nhs number page
    And I enter <nhsNumber> as the nhs number
    When I click the search button
    Then I can see a message that no results are found for the NHS number <nhsNumber>
    And I can see an option to create a new patient

    Examples:
      | nhsNumber  |
      | 9449306621 |

  @findpatient
  Scenario Outline: NHS Number: Existing patients can be found using their NHS number
    Given I am on the find a patient by nhs number page
    And I enter <nhsNumber> as the nhs number
    When I click the search button
    Then I can see the patient's information in the search results, showing their name: <name>, nhs number: <nhsNumber>, dob: <dateofbirth> and address: <address>

    Examples:
      | nhsNumber  | name        | dateofbirth | address                                                    |
      | 9693632109 | Bill GARTON |   23/6/1946 | 1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW |

  @findpatient
  Scenario Outline: Demographics: Existing patients can be found using their mandatory demographic details
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details <firstName>, <lastName>, and <dob>
    When I click the search button
    Then I can see the patient's information in the search results, showing their name: <firstName> <lastName>, nhs number: <nhsNumber>, dob: <dob> and address: <address>

    Examples:
      | nhsNumber  | firstName | lastName       | dob        | address                                   |
      | 9449303762 | Pryderi   | Warnford-Davis | 14/04/2001 | 1 CRANLEIGH ROAD, ESHER, SURREY, KT10 8DF |

  @findpatient
  Scenario Outline: Demographics: Existing patients can be found using their optional demographic details
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details <firstName>, <lastName>, and <dob>
    And I enter the postcode <postcode>
    And I select the gender <gender>
    When I click the search button
    Then I can see the patient's information in the search results, showing their name: <firstName> <lastName>, nhs number: <nhsNumber>, dob: <dob> and address: <address>

    Examples:
      | nhsNumber  | firstName | lastName | dob        | address                                                    | postcode | gender |
      | 9693632109 | Bill      | Garton   |  23/6/1946 | 1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW | DN18 5DW | Male   |
      | 9470006739 | JANNETTE  | ARD      | 09/12/2015 |           1 ST. MARTINS COURT, CONISTON, CUMBRIA, LA21 8HZ | LA21 8HZ | Other  |

  @findpatient
  Scenario Outline: Demographics: Search does not find existing patients if any of their details are wrong
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details <firstName>, <lastName>, and <dob>
    And I enter the postcode <postcode>
    And I select the gender <gender>
    When I click the search button
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
  Scenario Outline: Demographics: Search without entering patient details shows errors on the mandatory fields
    Given I am on the find a patient by demographics page
    When I click the search button
    Then I can see a first name error message Enter the first name
    And I can see a last name error message Enter the last name
    And I can see a dob error message Enter the date of birth

    Examples:
      |  |

  @findpatient
  Scenario Outline: Demographics: Search with an invalid postcode shows an error message
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details <firstName>, <lastName>, and <dob>
    When I enter the postcode INVALID
    When I click the search button
    Then I can see a postcode error message Enter the full postcode in the correct format

    Examples:
      | firstName | lastName | dob       | postcode |
      | Bill      | Garton   | 23/6/1946 | INVALID  |

  @findpatient
  Scenario Outline: Demographics: Multiple demographic matches shows an error that more than one result is found
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details <firstName>, <lastName>, and <dob>
    When I click the search button
    Then I can see a message that more than one result was found

    Examples:
      | firstName | lastName | dob        |
      | Aidan     | Smith    | 23/02/2020 |

  @findpatient
  Scenario Outline: Demographics: Can search for a patient by their old name, after a name change
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details <firstName>, <lastName>, and <dob>
    When I click the search button
    Then I can see the patient's information in the search results, showing their name: <newName>, nhs number: <nhsNumber>, dob: <dob> and address: <address>

    Examples:
      | firstName | lastName  | dob        | newName       | nhsNumber  | address                                 |
      | Joan      | Robertson | 19/09/1972 | Poppy Roberts | 9449310076 | 1 Canada Road, COBHAM, Surrey, LS15 4LJ |

  @findpatient
  Scenario Outline: Demographics: Searching for a patient without a record returns no results
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details <firstName>, <lastName>, and <dob>
    When I click the search button
    Then I can see a message that no results are found for the patient
    And I can see an option to create a new patient

    Examples:
      | firstName | lastName | dob        |
      | Cecile    | Elston   | 18/01/1965 |

  @findpatient @createpatient
  Scenario Outline: Local: Searching for a patient without a record returns no results
    Given I am on the find a patient by local records page
    And I enter the mandatory patient details <firstName>, <lastName>, and <dob>
    When I click the search button
    Then I can see a message that no results are found for the patient
    And I can see an option to review the search tips
    #And I can see an option to create a new patient

    Examples:
      | firstName | lastName | dob        |
      | John      | Preston  | 14/03/2003 |

  @findpatient @createpatient
  Scenario Outline: Local: Created patient can be found using local search
    Given I am on the find a patient by demographics page
    And I enter the mandatory patient details for a new patient
    When I click the search button
    And I click the create a new patient button
    Then I can see an option to review the search tips
    Examples:
      | firstName | lastName | dob        |
      | John      | Preston  | 14/03/2003 |

  @findpatient @createpatient
  Scenario Outline: Local: Created patient cannot be found using demographic search
    Given I am on the find a patient by local records page
    And I enter the mandatory patient details <firstName>, <lastName>, and <dob>
    When I click the search button
    Then I can see a message that no results are found for the patient
    And I can see an option to review the search tips
    #And I can see an option to create a new patient

    Examples:
      | firstName | lastName | dob        |
      | John      | Preston  | 14/03/2003 |
