from bookshelf import get_model
from flask import Flask, Blueprint, redirect, jsonify, request, Response
import json

crud = Blueprint('crud', __name__)

# [START list]
#GET /books
@crud.route("/", methods=['GET'])
def list():
    
    books = get_model().list()
    #If dont limit number of items
    #books, next_page_token = get_model().list()
    return jsonify({'books': books})
# [END list]

# [START read]
#GET /books/user_id
@crud.route("/<book_id>", methods=['GET'])
def read (book_id):
    return_value = get_model().read(book_id)
    return jsonify(return_value)
# [END read]

def validBookObject(bookObject):
    if ('title' in bookObject):
        print('entro a validBook')
        return True
    else:
        return False


# [START add]
#POST /books
@crud.route("/", methods=['POST'])
def add():
    request_data = request.get_json()
    if (validBookObject(request_data)):
        data = request.form.to_dict(flat=True)
        print("requested data")
        print(request_data)
        book = get_model().create(request_data)
        print('book id')
        print( json(book['_id']))
        # First parameter is a response body, second parameter is the status code, third is the content type header that will be sent
        response = Response('',201, mimetype='application/json')
        # response.headers['Location'] = '/books/' + str(book['_id'])
        return response
    else:
        invalidBookObjectErrorMsg = {
            'error': 'Invalid book object passed in request',
            'helpString': "Data passed in similiar to this {'author': 'Tarantino','title': 'Pulp Fiction','genre': 'Drama', 'read': true}"
        }
        # invalidBookObjectErrorMsg is a dictionary and  we need conver to json
        response = Response(json.dumps(invalidBookObjectErrorMsg),status=400, mimetype='application/json')
        return response
# [END add]


def valid_patch_request_data(request_data):
    if ('name' or 'price' in request_data):
        return True
    else:
        return False

#PATCH
@crud.route('/<book_id>', methods=['PATCH'])
def edit(book_id):
    request_data = request.get_json()
    if(not valid_patch_request_data(request_data)):
        invalidBookObjectErrorMsg = {
            'error': 'Book with the ISBN number that was provided was not found',        }
        ## invalidBookObjectErrorMsg is a dictionary and  we need conver to json
        response = Response(json.dumps(invalidBookObjectErrorMsg),status=400, mimetype='application/json')
        return response

    book = get_model().update(request_data, book_id)
    response = Response('', status=204)
    ## response.headers['Location'] = '/books/' + str(book['_id'])
    return response

#DELETE
@crud.route("/<book_id>", methods=['DELETE'])
def delete_book(book_id):
    if(get_model().delete(book_id)):
        response = Response('', status=204)
        response.headers['Location'] = '/books'
        return response

    invalidBookObjectErrorMsg = {
        'error': 'Book with the book_id number that was provided was not found, so therefore unable to delete',
    }
    ## invalidBookObjectErrorMsg is a dictionary and  we need conver to json
    response = Response(json.dumps(invalidBookObjectErrorMsg),status=404, mimetype='application/json')
    return response

