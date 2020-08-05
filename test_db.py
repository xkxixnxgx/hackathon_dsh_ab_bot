from tinydb import TinyDB, Query

db = TinyDB('db_test.json')
db.insert({'int': 1, 'char': 'v'})

User = Query()
print(db.all())