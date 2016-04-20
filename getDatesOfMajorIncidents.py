import pyspark
import pymongo_spark
import datetime
import pymongo
import pytz
import time
from operator import add

from pymongo import MongoClient

start_time = time.time()
client = MongoClient('localhost',27017)
utc=pytz.UTC
db = client['disaster']
threeHourlyAlert = db['minute']

pymongo_spark.activate()
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName("pyspark test")
sc = SparkContext(conf=conf)
rdd = sc.mongoRDD('mongodb://localhost:27017/disaster.overAll10MinuteAverage').persist()


dayOne=datetime.datetime(2016, 3, 24, 0, 0 , 0).replace(tzinfo=utc)
incrementBy3Hour= datetime.timedelta(hours=2)

for x in range(288):
    dayOneIncrementBy3Hour = dayOne + incrementBy3Hour
    dayOneIncrementBy3Hour = dayOneIncrementBy3Hour.replace(tzinfo=utc)
    output = rdd.filter( lambda x: x['date'] >= dayOne and x['date'] < dayOneIncrementBy3Hour ).flatMap(lambda x: x['average'].items()).filter(lambda (x,y): y > 8 ).map(lambda (x,y): (x,1)).reduceByKey(lambda x,y:x+y).filter(lambda (x,y): y>8).map(lambda(x,y): x).collect()
    if output != []:
        result = db.threeHourlyAlert.insert_one({"date": dayOne , "count":output})
    dayOne = dayOneIncrementBy3Hour.replace(tzinfo=utc)

