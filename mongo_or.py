#########################################################################
#-*- coding:utf-8 -*-
# File Name: test.py
#########################################################################
#!/bin/python
from settings import DB
t = DB.room.find({"$or":[{"room_type":4},{"room_type":3}]})
#t = DB.room.find({"$or":[{"room_type":4},{"room_type":3}], "$or":[{"room_contract_data.number":{'regex': '.*38'}}]})
print t.count()
b = DB.room.find({'$and':[{"$or":[{"room_type":4},{"room_type":3}], "$or":[{"room_contract_data.number":{'$regex': '.*38'}}]}]})
print b.count()
c = DB.room.find({"room_contract_data.number":{'$regex': '.*38'}})
print c.count()
