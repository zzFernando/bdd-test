Feature: Request all fields
    Scenario: Call the leaf api and request all fields
        Given I have a valid token 
        When I make an http GET call to https://api.withleaf.io/services/fields/api/fields
        Then I must get a response with status code 200 and a json object with all fields
