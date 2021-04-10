Feature: Request token
    Scenario: Call the leaf api and request a token
        Given I have user authentication credentials 
        When I make an http post call to https://api.withleaf.io/api/authenticate
        Then I must get a response with status code 200 and a json object with token
