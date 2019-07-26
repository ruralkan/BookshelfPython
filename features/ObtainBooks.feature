Feature: Obtain books from the collection
    In order to buy any book from collection
    As an API User
    I should be able to obtain  a list of Book in the collection
    and select each all to watch details

Scenario: Fetch All books
    Given an user wants to check which books are available from our website
    When  He makes a request to books collection
    Then He obtain a list with all books

Scenario: Get a particular book for ID
    Given an particular book with itself ID in the collection
    When I select its ID
    Then I can obtain detail about the book

Scenario: Get a error when there arent book's ID
    Given that a Book ID not exist  or is wrong
    When I query the ID
    Then I obtain an error message

Scenario: Get books for Keywords
    Given I dont remember the book's title
    When I query the books by key words
    Then I can obtain a list with all books with the keyword

