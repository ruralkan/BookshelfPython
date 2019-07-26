Feature: Update feature books
    In order to modify the information about any book from collection
    As an API User
    I should be able to updata all or only one Book attribute

Scenario: Update all information about a book by ID
    Given an user wants to update all book's features
    When  He makes a request to a particular books ID
    Then He obtain information of the specific book
    And He can modify all features
    And Save all features in the database

Scenario: Update some features from a book by ID
    Given an user wants to update some book's features
    When  He makes a request to book's ID
    Then He obtain all features of the specific book
    And He can modify any feature
    And Save changes in the database

