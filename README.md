# bookshelfApi
Build a Book list api (The Bookshelf api) using Flask, Mongo and docker

## The project

Imagine the company you work for called a meeting and invited you to participate. When you arrive, the project manager explains that a major Bookstore hired the company to write an API.

As a proof-of-concept, the retailer requested a book list api ( bookshelf Api) to expose and store books in a collection of book titles. the other purpose is integrate specialized tools, services, or libraries with their own customer and business partners

Your company started the project to write a minimally viable product (MVP) for the bookshelf Api, but the Node developer who was working on it suddenly left the company. The project must be finished, or the customer will take its business elsewhere.

Your role is to finish the JavaScript code started by the previous Node developer and ensure the code meets the functional specs. Are you up to the task?

## User stories

The Bookshelf api MVP consists of 7 user stories. This section contains the stories that you must complete before the MVP can be shown to the customer. Due to the incredibly short timeframe, these stories will act as functional specs for the bookshelf Api MVP.

Each story has a brief description, along with a list of high-level requirements that must be met before the story will be considered accepted.

The stories are implemented in the order given below.

1.	Book collection: return all items in the book collection
	A user needs to be able to obtain and watch all items in the Book collection

2.	Books: Find by ID
	Each book in the database has a unique ID, and a user needs to be able to find a specific book in the database by its ID. Given an ID, the system will return a single book from the database that matches the specified ID.

3.	Books: Add new book to collection
	A user needs to be able to add a new book to collection. The system will provide a way to add new book in the database with the following attributes:
	* Title
	* author
	* genre
	* description
	* read


5.	Books: Update a Book
	A user needs to be able to modify all the book attributes:
	* Title
	* author
	* genre
	* description
	* read

	Given an ID, and values for the updated attributes, the system will provide a way to update the book in the database.

6. Books: Update only a attribute from Book
	A user needs to be able to modify only one attribute from book:
	* Title
	* author
	* genre
	* description
	* read

	Given an ID, and the value for the updated attribute, the system will provide a way to update the book in the database.


7.	Books: Remove item from book collection
	A user needs to be able to remove an item from the collection.
	Given a book ID, the system will provide a way to remove the book from the database.


Together, these 7 stories define the system’s behavior.


## BDD

Behaviour-Driven Development (BDD) is a collaborative approach to software development that bridges the communication gap between business and IT. BDD helps teams communicate requirements with more precision, discover defects early and produce software that remains maintainable over time.

It helps teams create business requirements that can be understood by the whole team. Specifying examples uncovers misunderstanding people might not even be aware of. Teams that practice BDD focus on preventing defects rather than finding them. This leads to less rework and quicker time to market.

Traditional test-driven development (TDD) focuses on only the components, not on larger features or how the components work together. Therefore, it's impossible to know whether two components didn't interact successfully to deliver the intended functional behavior. While the component itself might behave perfectly, the user might still see incorrect behavior.

Alternatively, BDD focuses on the features as they are developed, ensuring that the feature works as intended, going across components.

Some people refer to BDD as "TDD done right." You can also think of BDD as "how we build the right thing" and TDD as "how we build the thing right."

Ideally you test your user stories in two ways:

1. With BDD tests that prove that the stories do what they were meant to

2. With TDD tests that confirm that the components work correctly


## OpenAPI Specification and Swagger

The OpenAPI Specification, formerly known as the Swagger Specification, is the world’s standard for defining RESTful interfaces. The OAS enables developers to design a technology-agnostic API interface that forms the basis of their API development and consumption.

The OpenAPI Specification was donated to the Linux Foundation under the OpenAPI Initiative in 2015. The specification creates a RESTful interface for easily developing and consuming an API by effectively mapping all the resources and operations associated with it.

The Swagger specification defines a set of files required to describe such an API. These files can then be used by the Swagger-UI project to display the API and Swagger-Codegen to generate clients in various languages. Additional utilities can also take advantage of the resulting files, such as testing tools.


