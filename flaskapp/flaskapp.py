from flask import Flask, render_template , jsonify ,request
from flask.ext.bootstrap import Bootstrap
from flask.ext.triangle import Triangle
import json


########## SPARK RELATED ###########

#import pyspark
#import pymongo_spark
#pymongo_spark.activate()
#from pyspark import SparkContext, SparkConf
#conf = SparkConf().setAppName("pyspark test")
#sc = SparkContext(conf=conf)
#rdd = sc.mongoRDD('mongodb://localhost:27017/disaster.Tweets')

####################################

app = Flask(__name__)
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
    	return jsonify(username="Mahesh")
    if request.method == 'POST':
	#print json.loads(request.data.decode())
        count = rdd.count()
        print count
	return jsonify(data=count)
	#return json.loads(request.data.decode())['search']
	#return jsonify(data="hello")	

if __name__ == '__main__':
  app.debug = True
  app.run(debug=True,host=app.config['SERVER_NAME'], port=80)
  #app.run(debug=True)
