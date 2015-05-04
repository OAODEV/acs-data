import os, random
from pymongo import MongoClient

mongo_uri = "mongodb://{}:{}".format(
    os.environ["MONGO_PORT_27017_TCP_ADDR"],
    os.environ["MONGO_PORT_27017_TCP_PORT"]
    )
client = MongoClient(mongo_uri)
db = client[os.environ.get("target_database", "test_db")]
collection = db[os.environ.get("target_collection", "test_collection")]

def new_doc(name, score):
    return {
        "name": name,
        "score": score
        }

default_names = "Alice, Bob, Carol, Delfina"
documents = map(lambda x: new_doc(*x),
                [(name, random.SystemRandom().randint(0, 100))
                 for name
                 in os.environ.get('names', default_names).split(',')
                 ])
print "created {} documents".format(len(documents))
print "total score: {}".format(sum([doc["score"] for doc in documents]))

ids = map(lambda x: collection.insert(x), documents)
print "inserted {} documents: {}".format(len(ids), ids)
