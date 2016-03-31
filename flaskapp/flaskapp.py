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
########## SPARK RELATED #############

#import pyspark
#import pymongo_spark
#pymongo_spark.activate()
#from pyspark import SparkContext, SparkConf
#conf = SparkConf().setAppName("pyspark test")
#sc = SparkContext(conf=conf)
#rdd = sc.mongoRDD('mongodb://localhost:27017/disaster.Tweets')

######################################

app = Flask(__name__)
Triangle(app)
app.config['SERVER_NAME'] = 'ec2-52-36-170-157.us-west-2.compute.amazonaws.com'

bootstrap = Bootstrap(app)

@app.route('/',methods=['GET', 'POST'])
def hello_world():
  #return 'Hello from Flask!'
  return render_template('index.html')


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
        count = rdd.count()
        print count
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
    return render_template('displayGraphs.html', content=listCreation)
if __name__ == '__main__':
  app.debug = True
  app.run(debug=True,host=app.config['SERVER_NAME'], port=80)
  #app.run(debug=True)
