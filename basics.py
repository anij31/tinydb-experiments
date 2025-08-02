"""Create a TinyDB database that stores data in db.json

Functionalities:
create db using TinyDB('dbname'.json)
create query using Query()
get db using db.all()
search using db.search(field == value)
insert using db.insert() - takes in python dictionaries
update using db.update(key:value, of field)
remove using db.remove(condition)
truncate or cleanslate the db using db.truncate()
"""
from tinydb import TinyDB, Query

# Create database and a corresponding query
db = TinyDB('db.json')
fruit = Query()

# Insert data
# db.insert({'type': 'Apple', 'count': 7})
# db.insert({'type': 'Peach', 'count': 4})

# Get all the entries
# print(db.all())

# Print items in db.json one by one
# for item in db:
#     print(item)

# Search for item
# print(db.search(fruit.type == 'Peach'))

# Update the count field of the apple
# db.update({'count': 10}, fruit.type == 'Apple')
# print(db.all())

# Remove an entry/document
# db.remove(fruit.count < 5)
# print(db.all())

# Cleanslate the db
# db.truncate()
# print(db.all())

