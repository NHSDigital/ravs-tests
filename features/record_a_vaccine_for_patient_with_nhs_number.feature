Feature: Record vaccine

@recordvaccine
Scenario Outline: Record a vaccine with nhs number
    Given I login to RAVS and get patient details for <nhs_number>
    And set the vaccinator details
    And I search for a patient with the NHS number in the find a patient screen
    And I open the patient record and click choose vaccine button
    When I choose the vaccine and vaccine type and click continue
    And I assess the patient's <eligibility> with the details and click continue to record consent screen button
    And I record <consent> with the details and click continue to vaccinate button
    And I enter <vaccination> details and click Continue to Check and confirm screen
    Then I need to be able to see the patient <name>, <dob>, <address> and vaccination details on the check and confirm screen
    And when I click confirm and save button, the immunisation history of the patient should be updated in the patient details page

Examples:
    | nhs_number   | eligibility | consent | vaccination | name | dob | address |
    | 9693632109   |  yes        | yes     | yes         | Bill GARTON | 	23/6/1946 | 	1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW |
    | 9470040228   |  yes        | yes     | yes         | HERBERT HAAG | 14/12/1922 | 10 COASTAL ROAD, HEST BANK, LANCASTER, LA2 6HN |
    | 9470057589   |  yes        | yes     | yes         | ROGER SEABORNE | 13/12/1922 | 10 ANN STREET, DALTON-IN-FURNESS, CUMBRIA, LA15 8BG |
    | 9472710255   |  yes        | yes     | yes         | DELICE PINKER | 	10/11/1926 | HARDCRAGG HOUSE, HARDCRAGG WAY, GRANGE-OVER-SANDS, CUMBRIA, LA11 6BH |
