import pymongo
import datetime

from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client['disaster']
Tweets = db['Tweets']


dateFromMarch = datetime.datetime(2016, 3, 24, 0, 0 , 0)
currentDate = datetime.datetime.utcnow()
TweetsGatheredPerDay = Tweets.find({"created_at" : { '$gt' : dateFromMarch , '$lt': currentDate }}).count()
print TweetsGatheredPerDay  
        #print content
        #for issue in count.keys():
        #    if issue in content['text']:
        #        #print "Happening: " , issue
        #        count[issue] += 1

    #print count
    #break
    #monthly  = db['monthly']

    #result = db.monthly.insert_one({"date": dateFromMarch , "count": count})
    #dateFromMarch += differenceOf24Hours 


#print "Before Collapse:" , count

#for content in afterCollapseTweets:
#    for issue in count.keys():
#        if issue in content['text']:
#            count[issue] += 1

#print "After Collapse:" , count 
#result = db.overView.insert_one({"date": dateNow , "count": count} )
#print "Output: " , result
#print count    
    #print content['text']

