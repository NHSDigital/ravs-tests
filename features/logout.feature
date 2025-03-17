Feature: Logout Feature

  Background:
  Given I am logged into the RAVS app as <user_role> into care model <care_model> with <site>

@logout
  Scenario: NHS sign in page should be visible
    When I click the logout button
    Then the user should be logged out successfully

    Examples:
    | care_model          |  user_role          | site                          |
    | Trust site          |  lead administrator | Weaverham Surgery             |
    | Community pharmacy  |       administrator | Aspire Pharmacy               |
    | Branch surgery      |       administrator | Aire Valley Surgery (rawdon)  |
