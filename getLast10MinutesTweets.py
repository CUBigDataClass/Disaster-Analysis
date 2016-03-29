import pymongo
import datetime

from pymongo import MongoClient
client = MongoClient()

client = MongoClient('localhost',27017)

db = client['disaster']
Tweets = db['Tweets']

dateNow = datetime.datetime.utcnow()
#print datetime.datetime.utcnow()
#print datetime.timedelta(minutes=10)
differenceOf10Minutes = datetime.timedelta(minutes=10)
#print datetime.datetime.utcnow() - datedifferenceOf10Minutes 
#print Tweets.count()
neededValueLast10Minutes = dateNow - differenceOf10Minutes

print Tweets.find({"created_at" : { '$gte' : neededValueLast10Minutes }}).count()
