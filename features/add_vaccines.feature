Feature: Add vaccine to site

  Background:
  Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>

  @addvaccine
  Scenario: Add vaccines page should launch
    When I am on the vaccines page
    And I click add vaccine button
    Then the choose site page should be launched

    Examples:
    | care_model          |  user_role          | site                          |
    | Trust site          |  lead administrator | Weaverham Surgery             |
    | Community pharmacy  |       administrator | Aspire Pharmacy               |
    | Branch surgery      |       administrator | Aire Valley Surgery (Rawdon)  |

  @addvaccine
  Scenario: Vaccines navigation link should not be visible when logged in as recorder
    Then vaccines navigation link should not be visible

    Examples:
    | care_model          |  user_role | site                      |
    | Trust site          |  recorder  | Weaverham Surgery             |
    | Community pharmacy  |  recorder  | Aspire Pharmacy               |
    | Branch surgery      |  recorder  | Aire Valley Surgery (Rawdon)  |

  @addvaccine
  Scenario: Vaccines navigation link should be visible when logged in as an administrator
    Then vaccines navigation link should be visible

  @addvaccine
  Scenario: Add vaccines page should be visible when logged in as an administrator
    When I click the vaccines navigation link
    Then the vaccines page should be visible

    Examples:
    | care_model          |  user_role      | site                      |
    | Trust site          |  administrator  | Weaverham Surgery             |
    | Community pharmacy  |  administrator  | Aspire Pharmacy               |
    | Branch surgery      |  administrator  | Aire Valley Surgery (Rawdon)  |
