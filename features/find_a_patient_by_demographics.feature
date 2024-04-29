# Feature: Search by demographics

#   Scenario: Search for a patient using demographic information
#     Given I am on the patient search page
#     When I enter the following demographic information:
#       | Field           | Value         |
#       | First name      | <First Name>  |
#       | Last name       | <Last Name>   |
#       | Gender          | <Gender>      |
#       | Full postcode   | <Postcode>    |
#       | Date of birth   | <Date of Birth> |
#     And I submit the search
#     Then I should see the patient details matching the provided demographic information

#     Examples:
#       | First Name | Last Name | Gender | Postcode  | Date of Birth |
#       | Bill       | GARTON    | Male   | DN18 5DW  | 23/06/1946    |
#       | John       | DOE       | Male   | EC1A 1BB  | 15/09/1985    |
#       | Alice      | SMITH     | Female | SE10 9JF  | 05/12/1978    |
