Feature: Logout Feature

@logout
  Scenario: NHS sign in page should be visible
    Given I am logged into the RAVS app
    When I click the logout button
    Then the user should be logged out successfully