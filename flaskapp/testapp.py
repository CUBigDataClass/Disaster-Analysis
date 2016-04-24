from __future__ import print_function 
import sys
from flask import Flask, render_template , jsonify ,request
from flask.ext.bootstrap import Bootstrap
from flask.ext.triangle import Triangle
from bson import json_util
import json

######### MONGO DB Related ###########
import pymongo
import datetime

from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client['disaster']
overView = db['overView']
overView = db['overAll10MinuteAverage']
Tweets = db['Tweets']
########## SPARK RELATED #############

#import pyspark
#import pymongo_spark
#pymongo_spark.activate()
#from pyspark import SparkContext, SparkConf
#conf = SparkConf().setAppName("pyspark test")
#sc = SparkContext(conf=conf)
#rdd = sc.mongoRDD('mongodb://localhost:27017/disaster.Tweets')

######################################

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

app = Flask(__name__)
Triangle(app)
app.config['SERVER_NAME'] = 'ec2-52-39-134-88.us-west-2.compute.amazonaws.com'

bootstrap = Bootstrap(app)

@app.route('/home',methods=['GET', 'POST'])
def hello_world():
  #return 'Hello from Flask!'
  return render_template('newIndex.html')


@app.route('/', defaults={'KeyWord': None})
@app.route('/<KeyWord>')
def test(KeyWord):
    if( KeyWord == None ): 
        return render_template('newIndex.html')
    #return jsonify(data=KeyWord)
    content = list(overView.find({},{'_id': 0,'date': 1,'average.'+KeyWord:1}))
    content1 = []
    count = Tweets.count()
    {{ count }}
    print (count, file=sys.stderr)
    for x in content[0:5]:
        content1.append([x['date'] , x['average'][KeyWord]])
    #print content
    return render_template('newIndex.html', content=json_util.dumps(content1), data=count)
    #return render_template('test.html')

@app.route('/getJSON/', defaults={'KeyWord': None})
@app.route('/getJSON/<KeyWord>')
def test1(KeyWord):
    content = list(overView.find({},{'_id': 0,'date': 1,'average.'+KeyWord:1}))
    content1 = []
    for x in content:
        content1.append([x['date'] , x['average'][KeyWord]])
    return json_util.dumps(content1)

@app.route('/getCount/',methods=['GET', 'POST'])
def getCount():
#    print request
    if request.method == 'GET':
        #content = json.dumps(,default=json_util.default)
        content = list(overView.find({},{'_id': 0}))[0]['count']
        #return jsonify(data=content)
        #return json.dumps({"auth":"1"})
        return render_template('displayGraphs.html', content=content)
        #print content
        #return jsonify(data="hello")
    	#return jsonify()
    if request.method == 'POST':
	#print json.loads(request.data.decode())
        #count = rdd.count()
        #print count
	count = 1
	return jsonify(data=count)
	#return json.loads(request.data.decode())['search']
	#return jsonify(data="hello")	


@app.route('/getCountHourly/',methods=['GET'])
def getHourlyCount():
    content = list(overView.find({},{'_id': 0}))
    listCreation =  [[0 for x in range(6)] for x in range(222)]
    totalCount = 0
    for i in content[-6:]:
        count = 0
        for j in i['count']:
            listCreation[count][totalCount] = i['count'][j]    
            count += 1
        totalCount += 1 
    return render_template('displayGraphHourly.html', content=listCreation)
if __name__ == '__main__':
  app.debug = True
  app.run(debug=True,host=app.config['SERVER_NAME'], port=80)
  #app.run(debug=True)
