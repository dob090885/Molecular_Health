
Feature: Fetching first 10 trails for different search inputs
  # Enter feature description here

  Scenario: Validating Blank Search
    Given User is on Home Page
    When User does not enter any key and click Search
    Then User navigates to results page displaying all results

  Scenario: Validating Search button
    Given User is on Home Page
    When User enters key and click Search
    Then User navigates to results page and fetch trails

