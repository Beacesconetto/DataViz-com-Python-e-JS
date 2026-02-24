from pymongo import MongoClient
import bson

client = MongoClient()
db = client.nobel_prize
coll = db.winners

DB_NOBEL_PRIZE = 'nobel_prize'
COLL_WINNERS = 'winners'

def get_mongo_database(db_name, host='localhost', port=27017, username=None, password=None):
    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s/%s'%\
        (username, password, host, db_name)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)
    return conn[db_name]       
  
db = get_mongo_database(DB_NOBEL_PRIZE)
coll = db[COLL_WINNERS]

nobel_winners = [
{'category': 'Physics',
'name': 'Albert Einstein',
'nationality': 'Swiss',
'gender': 'male',
'year': 1921},
{'category': 'Physics',
'name': 'Paul Dirac',
'nationality': 'British',
'gender': 'male',
'year': 1933},
{'category': 'Chemistry',
'name': 'Marie Curie',
'nationality': 'Polish',
'gender': 'female',
'year': 1911}
]

# coll.drop() -> para "limpar" tudo antes de inserir novos dados
#coll.insert_many(nobel_winners) -> Para colocar os dados nobel_winners no banco
#print(list(coll.find()))
oid = bson.ObjectId() # Mostyrar a data e horário
print(oid.generation_time)

res = coll.find({'category': 'Chemistry'})
#print(list(res))

res2 = coll.find({'year': {'$gt': 1930}}) # $gt = greater than
#print(list(res2))

res3 = coll.find({'$or': [{'year':{'$gt': 1930}}, 
                          {'gender':'female'}]})
#print(list(res3))

def mongo_coll_to_dicts(dbname='test', collname='test', query={}, del_id=True, **kw):
    db = get_mongo_database(dbname, **kw)
    res = list(db[collname].find(query))
    if del_id:
        for r in res:
            r.pop('_id')
    return res
print(mongo_coll_to_dicts(DB_NOBEL_PRIZE, COLL_WINNERS))