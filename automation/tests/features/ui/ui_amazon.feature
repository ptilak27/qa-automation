@ui
Feature: Amazon Product Search
    As a user
    I want to search for mobile phones on Amazon
    So that I can view product details

    Scenario: Search for mobile phones and extract product details
        Given I navigate to Amazon India website
        When I search for "mobile"
        Then I should see search results
        And I extract product details from page 1
        And I print the product information
