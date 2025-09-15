@api @regression
Feature: Create users via API from Excel
  Scenario: Read Excel and create users
    Given I have an Excel file with users
    When I create users via the API
    Then I print the API responses
