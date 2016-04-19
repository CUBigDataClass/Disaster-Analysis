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
#datetime.datetime.now().replace(tzinfo=utc)


db = client['disaster']
minute10Analysis = db['minute']

pymongo_spark.activate()
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName("pyspark")
sc = SparkContext(conf=conf)
rdd = sc.mongoRDD('mongodb://localhost:27017/disaster.analysisData')


#Objective 1: Get the number of times the key words(222) are used for 1 particular day , For every minute.
dayOne=datetime.datetime(2016, 3, 26, 17, 50 , 0).replace(tzinfo=utc)
incrementBy10Minute = datetime.timedelta(minutes=10)
incrementBy20Day = datetime.timedelta(days=20)
dayOneEnd = dayOne + incrementBy20Day
dayOneEnd.replace(tzinfo=utc)
contentRdd = rdd.map(lambda x: (x['text'],x['created_at'])).filter(lambda (x,y): y > dayOne and y < dayOneEnd).persist()

#count = {'bomb': 0, 'violent storm': 0, 'hijacker': 0, 'bombed': 0, 'sunk': 0, 'avalanche': 0, 'debris': 0, 'body bag': 0, 'battle': 0, 'fear': 0, 'weapons': 0, 'catastrophe': 0, 'forest fire': 0, 'ruin': 0, 'buildings burning': 0, 'blaze': 0, 'fatal': 0, 'airplane accident': 0, 'sinking': 0, 'electrocute': 0, 'rescue': 0, 'hostage': 0, 'massacre': 0, 'traumatised': 0, 'trouble': 0, 'screaming': 0, 'suicide bomb': 0, 'annihilated': 0, 'loud bang': 0, 'floods': 0, 'quarantine': 0, 'obliterate': 0, 'cliff fall': 0, 'body bagging': 0, 'snowstorm': 0, 'whirlwind': 0, 'disaster': 0, 'bleeding': 0, 'razed': 0, 'famine': 0, 'armageddon': 0, 'wreck': 0, 'thunder': 0, 'wrecked': 0, 'crush': 0, 'burned': 0, 'sirens': 0, 'explosion': 0, 'screams': 0, 'rescuers': 0, 'bridge collapse': 0, 'survivors': 0, 'fatality': 0, 'earthquake': 0, 'accident': 0, 'flames': 0, 'detonate': 0, 'mass murderer': 0, 'smoke': 0, 'military': 0, 'stretcher': 0, 'blizzard': 0, 'danger': 0, 'bloody': 0, 'panicking': 0, 'drowned': 0, 'eyewitness': 0, 'devastation': 0, 'bush fires': 0, 'army': 0, 'heat wave': 0, 'emergency plan': 0, 'tragedy': 0, 'collided': 0, 'survive': 0, 'injury': 0, 'riot': 0, 'attacked': 0, 'fire': 0, 'bioterrorism': 0, 'wounds': 0, 'quarantined': 0, 'drown': 0, 'hailstorm': 0, 'casualties': 0, 'mass murder': 0, 'demolish': 0, 'collision': 0, 'pandemonium': 0, 'sandstorm': 0, 'electrocuted': 0, 'landslide': 0, 'flooding': 0, 'mayhem': 0, 'rainstorm': 0, 'demolition': 0, 'blew up': 0, 'hijacking': 0, 'siren': 0, 'terrorist': 0, 'inundated': 0, 'damage': 0, 'lava': 0, 'devastated': 0, 'forest fires': 0, 'outbreak': 0, 'terrorism': 0, 'panic': 0, 'detonation': 0, 'injured': 0, 'deluged': 0, 'windstorm': 0, 'thunderstorm': 0, 'hazard': 0, 'crushed': 0, 'crashed': 0, 'blood': 0, 'buildings on fire': 0, 'destruction': 0, 'deluge': 0, 'weapon': 0, 'sinkhole': 0, 'aftershock': 0, 'ambulance': 0, 'wreckage': 0, 'desolate': 0, 'blown up': 0, 'fatalities': 0, 'injuries': 0, 'bombing': 0, 'structural failure': 0, 'death': 0, 'police': 0, 'destroyed': 0, 'engulfed': 0, 'crash': 0, 'emergency': 0, 'inundation': 0, 'collide': 0, 'blight': 0, 'destroy': 0, 'dust storm': 0, 'mudslide': 0, 'displaced': 0, 'arsonist': 0, 'nuclear reactor': 0, 'blazing': 0, 'lightning': 0, 'explode': 0, 'tsunami': 0, 'burning buildings': 0, 'volcano': 0, 'hijack': 0, 'refugees': 0, 'derailment': 0, 'harm': 0, 'hail': 0, 'bioterror': 0, 'hurricane': 0, 'trauma': 0, 'evacuation': 0, 'cyclone': 0, 'epicentre': 0, 'nuclear disaster': 0, 'hostages': 0, 'obliteration': 0, 'suicide bomber': 0, 'drowning': 0, 'derailed': 0, 'threat': 0, 'apocalypse': 0, 'chemical emergency': 0, 'burning': 0, 'obliterated': 0, 'screamed': 0, 'fire truck': 0, 'seismic': 0, 'wildfire': 0, 'emergency services': 0, 'attack': 0, 'storm': 0, 'catastrophic': 0, 'twister': 0, 'evacuated': 0, 'natural disaster': 0, 'collapse': 0, 'trapped': 0, 'war zone': 0, 'exploded': 0, 'collapsed': 0, 'oil spill': 0, 'evacuate': 0, 'typhoon': 0, 'dead': 0, 'survived': 0, 'first responders': 0, 'keyword': 0, 'radiation emergency': 0, 'annihilation': 0, 'deaths': 0, 'rubble': 0, 'ablaze': 0, 'meltdown': 0, 'casualty': 0, 'body bags': 0, 'upheaval': 0, 'flood': 0, 'demolished': 0, 'rioting': 0, 'hellfire': 0, 'curfew': 0, 'hazardous': 0, 'tornado': 0, 'desolation': 0, 'flattened': 0, 'drought': 0, 'derail': 0, 'arson': 0, 'rescued': 0, 'suicide bombing': 0, 'wild fires': 0, 'wounded': 0}

# for issue in count.keys():
#     print issue
def getCount(content):
    #print unicode(content).encode('utf-8')
    count = {'bomb': 0, 'violent storm': 0, 'hijacker': 0, 'bombed': 0, 'sunk': 0, 'avalanche': 0, 'debris': 0, 'body bag': 0, 'battle': 0, 'fear': 0, 'weapons': 0, 'catastrophe': 0, 'forest fire': 0, 'ruin': 0, 'buildings burning': 0, 'blaze': 0, 'fatal': 0, 'airplane accident': 0, 'sinking': 0, 'electrocute': 0, 'rescue': 0, 'hostage': 0, 'massacre': 0, 'traumatised': 0, 'trouble': 0, 'screaming': 0, 'suicide bomb': 0, 'annihilated': 0, 'loud bang': 0, 'floods': 0, 'quarantine': 0, 'obliterate': 0, 'cliff fall': 0, 'body bagging': 0, 'snowstorm': 0, 'whirlwind': 0, 'disaster': 0, 'bleeding': 0, 'razed': 0, 'famine': 0, 'armageddon': 0, 'wreck': 0, 'thunder': 0, 'wrecked': 0, 'crush': 0, 'burned': 0, 'sirens': 0, 'explosion': 0, 'screams': 0, 'rescuers': 0, 'bridge collapse': 0, 'survivors': 0, 'fatality': 0, 'earthquake': 0, 'accident': 0, 'flames': 0, 'detonate': 0, 'mass murderer': 0, 'smoke': 0, 'military': 0, 'stretcher': 0, 'blizzard': 0, 'danger': 0, 'bloody': 0, 'panicking': 0, 'drowned': 0, 'eyewitness': 0, 'devastation': 0, 'bush fires': 0, 'army': 0, 'heat wave': 0, 'emergency plan': 0, 'tragedy': 0, 'collided': 0, 'survive': 0, 'injury': 0, 'riot': 0, 'attacked': 0, 'fire': 0, 'bioterrorism': 0, 'wounds': 0, 'quarantined': 0, 'drown': 0, 'hailstorm': 0, 'casualties': 0, 'mass murder': 0, 'demolish': 0, 'collision': 0, 'pandemonium': 0, 'sandstorm': 0, 'electrocuted': 0, 'landslide': 0, 'flooding': 0, 'mayhem': 0, 'rainstorm': 0, 'demolition': 0, 'blew up': 0, 'hijacking': 0, 'siren': 0, 'terrorist': 0, 'inundated': 0, 'damage': 0, 'lava': 0, 'devastated': 0, 'forest fires': 0, 'outbreak': 0, 'terrorism': 0, 'panic': 0, 'detonation': 0, 'injured': 0, 'deluged': 0, 'windstorm': 0, 'thunderstorm': 0, 'hazard': 0, 'crushed': 0, 'crashed': 0, 'blood': 0, 'buildings on fire': 0, 'destruction': 0, 'deluge': 0, 'weapon': 0, 'sinkhole': 0, 'aftershock': 0, 'ambulance': 0, 'wreckage': 0, 'desolate': 0, 'blown up': 0, 'fatalities': 0, 'injuries': 0, 'bombing': 0, 'structural failure': 0, 'death': 0, 'police': 0, 'destroyed': 0, 'engulfed': 0, 'crash': 0, 'emergency': 0, 'inundation': 0, 'collide': 0, 'blight': 0, 'destroy': 0, 'dust storm': 0, 'mudslide': 0, 'displaced': 0, 'arsonist': 0, 'nuclear reactor': 0, 'blazing': 0, 'lightning': 0, 'explode': 0, 'tsunami': 0, 'burning buildings': 0, 'volcano': 0, 'hijack': 0, 'refugees': 0, 'derailment': 0, 'harm': 0, 'hail': 0, 'bioterror': 0, 'hurricane': 0, 'trauma': 0, 'evacuation': 0, 'cyclone': 0, 'epicentre': 0, 'nuclear disaster': 0, 'hostages': 0, 'obliteration': 0, 'suicide bomber': 0, 'drowning': 0, 'derailed': 0, 'threat': 0, 'apocalypse': 0, 'chemical emergency': 0, 'burning': 0, 'obliterated': 0, 'screamed': 0, 'fire truck': 0, 'seismic': 0, 'wildfire': 0, 'emergency services': 0, 'attack': 0, 'storm': 0, 'catastrophic': 0, 'twister': 0, 'evacuated': 0, 'natural disaster': 0, 'collapse': 0, 'trapped': 0, 'war zone': 0, 'exploded': 0, 'collapsed': 0, 'oil spill': 0, 'evacuate': 0, 'typhoon': 0, 'dead': 0, 'survived': 0, 'first responders': 0, 'keyword': 0, 'radiation emergency': 0, 'annihilation': 0, 'deaths': 0, 'rubble': 0, 'ablaze': 0, 'meltdown': 0, 'casualty': 0, 'body bags': 0, 'upheaval': 0, 'flood': 0, 'demolished': 0, 'rioting': 0, 'hellfire': 0, 'curfew': 0, 'hazardous': 0, 'tornado': 0, 'desolation': 0, 'flattened': 0, 'drought': 0, 'derail': 0, 'arson': 0, 'rescued': 0, 'suicide bombing': 0, 'wild fires': 0, 'wounded': 0}
    for issue in count.keys():
        if issue in unicode(content).encode('utf-8'):
            count[issue] += 1
    return count.items()
    # for issue in count.keys():
    #   if issue in content:
    #       count[issue] += 1
    # return count
def printOutput(content):
    print content


#3706885
#2738
for x in range(2560):
    dayOneIncrementBy10Minute = dayOne + incrementBy10Minute
    dayOneIncrementBy10Minute = dayOneIncrementBy10Minute.replace(tzinfo=utc)
    #contentRdd.filter(lambda (x,y): y > dayOne and y < dayOneIncrementByAMinute).map(lambda (x,y): x).foreach(getCount)#.reduceByKey(add).collect()
    #count = contentRdd.filter(lambda (x,y): y > dayOne and y < dayOneIncrementByAMinute and issue in x).count() #.reduceByKey(add).collect()
    #Working readContent = contentRdd.filter(lambda (x,y): y > dayOne and y < dayOneIncrementByAMinute).map(lambda (x,y): x).map(getCount)
    #Working contentRdd.filter(lambda (x,y): y > dayOne and y < dayOneIncrementByAMinute).map(lambda (x,y): x).flatMap(getCount).reduceByKey(add).collect()
    #contentRdd.filter(lambda (x,y): y > dayOne and y < dayOneIncrementByAMinute).map(lambda (x,y): x).flatMap(getCount).reduceByKey(add).collect()
    #contentRdd.filter(lambda (x,y): y > dayOne and y < dayOneIncrementByAMinute).map(lambda (x,y): x).map(getCount).
    #readContent = contentRdd.filter(lambda (x,y): y > dayOne and y < dayOneIncrementByAMinute).map(lambda (x,y): x).reduce(getCount) #.reduceByKey(add).collect()
    output = dict(contentRdd.filter(lambda (x,y): y > dayOne and y < dayOneIncrementBy10Minute).map(lambda (x,y): x).flatMap(getCount).reduceByKey(add).collect())
    result = db.minute10Analysis.insert_one({"date": dayOne , "count":output})

    #result = db.analysisData.insert_one(content)
    #print "Date: ",dayOne , " Count:" , count
    dayOne = dayOneIncrementBy10Minute
    dayOne.replace(tzinfo=utc)

end_time = time.time()

print "Total Time Taken: " , end_time - start_time , " seconds"
