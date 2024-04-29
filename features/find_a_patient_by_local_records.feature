# Feature: Local Vaccination Record Search

#   Scenario: Search for a vaccination record in local records
#     Given I am on the local vaccination record search page
#     When I enter the following details:
#       | Field         | Value         |
#       | First Name    | Bill          |
#       | Last Name     | GARTON        |
#       | Gender        | Male          |
#       | Postcode      | DN18 5DW      |
#       | Date of Birth | 23/06/1946    |
#     And I click the search button
#     Then I should see the vaccination record for Bill GARTON displayed

#   Scenario Outline: Search for a vaccination record with incomplete data
#     Given I am on the local vaccination record search page
#     When I enter incomplete details:
#       | Field         | Value         |
#       | First Name    | <First_Name>  |
#       | Last Name     | <Last_Name>   |
#       | Gender        | <Gender>      |
#       | Postcode      | <Postcode>    |
#       | Date of Birth | <DOB>         |
#     And I click the search button
#     Then I should see an error message "<Error_Message>"

#     Examples:
#       | First_Name | Last_Name | Gender | Postcode | DOB         | Error_Message             |
#       | John       |           | Male   | SW1A 1AA | 01/01/1980  | Error: Last name required |
#       |            | Doe       | Male   | SW1A 1AA | 01/01/1980  | Error: First name required|
#       | John       | Doe       | Male   |           | 01/01/1980  | Error: Postcode required  |
#       | John       | Doe       |        | SW1A 1AA | 01/01/1980  | Error: Gender required    |
#       | John       | Doe       | Male   | SW1A 1AA |             | Error: Date of birth required |