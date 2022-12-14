import azure.functions as func
import pymongo
import os
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://lab2cosmosdb:QAUk1MHvjnVfFuC6zqpBE3jU8o2ZUlV5JY5HnDvySTPqL5Qw45iduqeKaDE0n715sKNvFL30AugvjfsgN0OJjQ==@lab2cosmosdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@lab2cosmosdb@" #os.environ["MyDbConnection"] # Change the Variable name, as applicable to you
        client = pymongo.MongoClient(url)
        database = client['lab2db'] # Change the MongoDB name (don't use the name of CosmosDB)
        collection = database['notes']    # Change the collection name

        result = collection.find()
        result = dumps(result)

        #return func.HttpResponse("updated database collection", mimetype="application/json", charset='utf-8')
        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except ConnectionError:
       
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)
