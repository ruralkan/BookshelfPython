
from bson import json_util, ObjectId
import json
from flask_pymongo import PyMongo



builtin_list = list


mongo = None


def _id(id):
    if not isinstance(id, ObjectId):
        return ObjectId(id)
    return id

# [START from_mongo]
def from_mongo(data):
    """
    Translates the MongoDB dictionary format into the format that's expected
    by the application.
    """
    if not data:
        return None

    data['id'] = str(data['_id'])
    data['id'] = data['id'][10:34]
    return data
# [END from_mongo]

def init_app(app):
    global mongo

    mongo = PyMongo(app)
    mongo.init_app(app)


# [START list]
def list():
    results = mongo.db.books.find().sort('title')
    #To avoid objectid ("") is not json serializable python
    #Dump loaded BSON to valid JSON string and reload it as dict
    resultsSan = json.loads(json_util.dumps(results))

    books = builtin_list(map(from_mongo, resultsSan))

    return books
# [END list]


# [START read]
def read(id):
    result = mongo.db.books.find_one({'_id': _id(id)})
    resultsSan = json.loads(json_util.dumps(result))
    book = from_mongo(resultsSan)
    return book
# [END read]


# [START create]
def create(data):
    result = mongo.db.books.insert_one(data)
    return read(result.inserted_id)
# [END create]


# [START update]
def update(data, id):
    mongo.db.books.replace_one({'_id': _id(id)}, data)
    return read(id)
# [END update]


def delete(id):
    mongo.db.books.delete_one({'_id': _id(id)})
    return True;