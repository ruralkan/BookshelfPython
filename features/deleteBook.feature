Feature: Delete a book from the collection
    In order to delete any book from collection
    As an API User
    I should be able to delete a Book in the collection

Scenario: Delete a particular book for ID
    Given an user watn to delete a book from the collection
    When I select its ID
    And request Delete
    Then I can Delete the book
