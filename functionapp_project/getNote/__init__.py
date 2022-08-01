import azure.functions as func
import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    id = req.params.get('id')
    if id:
        try:
            url = "mongodb://lab2cosmosdb:QAUk1MHvjnVfFuC6zqpBE3jU8o2ZUlV5JY5HnDvySTPqL5Qw45iduqeKaDE0n715sKNvFL30AugvjfsgN0OJjQ==@lab2cosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@lab2cosmosdb@" #os.environ["MyDbConnection"] # Change the Variable name, as applicable to you
            client = pymongo.MongoClient(url)
            database = client['lab2db'] # Change the MongoDB name (don't choose the name of the CosmosDb)
            collection = database['notes']    # Change the collection name

            query = {'_id': ObjectId(id)}
            result = collection.find_one(query)
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except ConnectionError as e:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)
