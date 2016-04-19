import pymongo
import datetime

from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client['disaster']
overView = db['overAll10MinuteAverage']

#cursor = list(overView.find())
content = list(overView.find({},{'_id': 0,'date': 1,'average.bomb':1}))
print "Length of content:" , len(content)
content1 = []
for x in content[0:5]:
    print x['date'] , x['average']['bomb']
    content1.append([x['date'] , x['average']['bomb']])
return content1
print content1
#date = []
#accident = []

#listCreation =  [[0 for x in range(6)] for x in range(222)] 
#location = list(countContent.keys())
#print listCreation
#totalCount = 0
#for i in content[0:6]:
#    count = 0
#    for j in i['count']:
#        listCreation[count][totalCount] = i['count'][j]    
#        count += 1
#    totalCount += 1

#print listCreation

