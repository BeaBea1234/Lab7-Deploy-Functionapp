import azure.functions as func
import pymongo
import os
import azure.functions as func
from bson.json_util import dumps
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()
    if request:
        try:
            # add your connection string here
            url = os.environ["MyDbConnection"]
            client = pymongo.MongoClient(url)

            # you will need this fill in
            database = client['lab2db'] # Change the MongoDB name (don't choose the name of the CosmosDb)
            collection = database['notes']    # Change the collection name

            # replace the insert_one variable with what you think should be in the bracket
            collection.insert_one({"_id": {"$oid": "5ed439f1a5193402a6bdfgdf"},"title": "this is a new entry done by a post request"})

            # we are returnign the request body so you can take a look at the results
            return func.HttpResponse(req.get_body())

        except ValueError:
            return func.HttpResponse('Database connection error.', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass the correct JSON format in the body of the request object",
            status_code=400
        )