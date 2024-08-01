Feature: Find a patient

@findpatient
  Scenario: Find a patient page should launch
    Given I am logged into the RAVS app
    When I click the find a patient navigation link
    Then the find a patient page should be displayed

@findpatient
  Scenario: Search without entering nhs number
    Given I am on the find a patient by nhs number page
    When I click the search button
    Then the alert message should appear for nhs number

@findpatient
  Scenario: Search without entering patient details
    Given I am on the find a patient by pds details page
    When I click the search button
    Then the alert messages should appear for Forename, Surname, Date Of Birth, Gender and Postcode

  @findpatient
  Scenario Outline: Search by NHS number
      Given I am on the find a patient by nhs number page
      When I enter a valid <nhsNumber>
      And I click the search button
      Then I should be directed to the patient's information page and show <name>, <nhsNumber>, <dateofbirth> and <address> details

      Examples:
      | nhsNumber   | name                 | dateofbirth | address   |
      | 9693632109  | Bill GARTON          | 23/6/1946   | 	1 MOUNT AVENUE, BARTON-UPON-HUMBER, S HUMBERSIDE, DN18 5DW  |
      # | 9449304424  | COMFORT26th Jones | 9/3/2018    | 	Ifyoucan113, 26TH, KT17 1NA  |
      | 9732743476  | Mike HEESOM         | 24/10/1992  | 	2 CHAPEL YARD, BRIGG, S HUMBERSIDE, DN20 8JY  |
      | 9650594000  | Archie STRAIN       | 30/7/2014   | 	1 CONINGSBY DRIVE, GRIMSBY, S HUMBERSIDE, DN34 5HQ  |
      | 9732596996  | Lisa WORTHY         | 30/6/2024   | 	10 NORTON PARK VIEW, SHEFFIELD, S8 8GS  |
      # | 9449305552  | Milton Jacob        | 4/7/2024    | 	12, OATLANDS ROAD, EN3 5LJ   |
      | 9449306621  | Not found           | 20110509    | KT21 1LJ  |
      # | 9449306613  | Briar Anderton    | 20/5/1990   | 	27 Ryde Vale Road, LONDON, SW12 9JQ  |
      | 9449306605  | Srinivasarao Patel  | 03/03/2020  | 	4 Calicut Lane2, Line 2, Line 3, SLOUGH, Berkshire, KT21 1EJ  |
      | 9449306494  | Reynolds Ryan       | 27/3/2001   | 	40 Queen Street London, EC4R 1DD  |
      | 9469997956  | SOLOMON DAZLEY      | 20160130    | 	10 BROOK STREET, LANCASTER, LA1 1SL   |
      | 9469998626  | JONNY CONOPO        | 20150305    | 	1 DAISY BANK, LANCASTER, LA1 3JW   |
      | 9470004272  | JOJO LANE           | 20150706    | 	10 RAKESMOOR LANE, BARROW-IN-FURNESS, LA14 4LG  |
      | 9470006143  | TABBY FERN          | 20150222    | 	CLEAR BECK HOUSE, TATHAM, LANCASTER, LA2 8PJ   |
      | 9470006739  | JANNETTE ARD        | 20151209    | 	1 ST. MARTINS COURT, CONISTON, CUMBRIA, LA21 8HZ  |
      | 9470011902  | KATEE TUZZIO        | 20150527    | 	BRIDGE END HOUSE, PARK ROAD, MILNTHORPE, CUMBRIA, LA7 7AN  |
      | 9470032640  | SYBIL PELLING        | 20151217    | 	50 ST. GEORGES QUAY, LANCASTER, LA1 1SA   |
