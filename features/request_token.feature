Feature: Request token
    Scenario: Call the leaf api and request a token
        Given I have user authentication credentials 
        When I make an http post call
        Then I must get a reponse with status code 200 and a jSon object with token