Feature: Accessibility Feature

@accessibility
  Scenario: RAVS login page should be accessible
    Given I access RAVS
    Then the RAVS sign in page should be accessible

@accessibility
  Scenario: RAVS pages should be accessible
    Given I am logged into the RAVS app
    When I access the page <page>
    Then the page <page> should be accessible

    Examples:
    | page      |
    | dashboard |
