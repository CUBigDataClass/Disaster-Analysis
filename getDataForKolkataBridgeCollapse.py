import pymongo
import datetime

from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client['disaster']
Tweets = db['Tweets']

count = {'ablaze':0,'accident':0,'aftershock':0,'airplane accident':0,'ambulance':0,'annihilated':0,'annihilation':0,'apocalypse':0,'armageddon':0,'army':0,'arson':0,'arsonist':0,'attack':0,'attacked':0,'avalanche':0,'battle':0,'bioterror':0,'bioterrorism':0,'blaze':0,'blazing':0,'bleeding':0,'blew up':0,'blight':0,'blizzard':0,'blood':0,'bloody':0,'blown up':0,'body bag':0,'body bagging':0,'body bags':0,'bomb':0,'bombed':0,'bombing':0,'bridge collapse':0,'buildings burning':0,'buildings on fire':0,'burned':0,'burning':0,'burning buildings':0,'bush fires':0,'casualties':0,'casualty':0,'catastrophe':0,'catastrophic':0,'chemical emergency':0,'cliff fall':0,'collapse':0,'collapsed':0,'collide':0,'collided':0,'collision':0,'crash':0,'crashed':0,'crush':0,'crushed':0,'curfew':0,'cyclone':0,'damage':0,'danger':0,'dead':0,'death':0,'deaths':0,'debris':0,'deluge':0,'deluged':0,'demolish':0,'demolished':0,'demolition':0,'derail':0,'derailed':0,'derailment':0,'desolate':0,'desolation':0,'destroy':0,'destroyed':0,'destruction':0,'detonate':0,'detonation':0,'devastated':0,'devastation':0,'disaster':0,'displaced':0,'drought':0,'drown':0,'drowned':0,'drowning':0,'dust storm':0,'earthquake':0,'electrocute':0,'electrocuted':0,'emergency':0,'emergency plan':0,'emergency services':0,'engulfed':0,'epicentre':0,'evacuate':0,'evacuated':0,'evacuation':0,'explode':0,'exploded':0,'explosion':0,'eyewitness':0,'famine':0,'fatal':0,'fatalities':0,'fatality':0,'fear':0,'fire':0,'fire truck':0,'first responders':0,'flames':0,'flattened':0,'flood':0,'flooding':0,'floods':0,'forest fire':0,'forest fires':0,'hail':0,'hailstorm':0,'harm':0,'hazard':0,'hazardous':0,'heat wave':0,'hellfire':0,'hijack':0,'hijacker':0,'hijacking':0,'hostage':0,'hostages':0,'hurricane':0,'injured':0,'injuries':0,'injury':0,'inundated':0,'inundation':0,'keyword':0,'landslide':0,'lava':0,'lightning':0,'loud bang':0,'mass murder':0,'mass murderer':0,'massacre':0,'mayhem':0,'meltdown':0,'military':0,'mudslide':0,'natural disaster':0,'nuclear disaster':0,'nuclear reactor':0,'obliterate':0,'obliterated':0,'obliteration':0,'oil spill':0,'outbreak':0,'pandemonium':0,'panic':0,'panicking':0,'police':0,'quarantine':0,'quarantined':0,'radiation emergency':0,'rainstorm':0,'razed':0,'refugees':0,'rescue':0,'rescued':0,'rescuers':0,'riot':0,'rioting':0,'rubble':0,'ruin':0,'sandstorm':0,'screamed':0,'screaming':0,'screams':0,'seismic':0,'sinkhole':0,'sinking':0,'siren':0,'sirens':0,'smoke':0,'snowstorm':0,'storm':0,'stretcher':0,'structural failure':0,'suicide bomb':0,'suicide bomber':0,'suicide bombing':0,'sunk':0,'survive':0,'survived':0,'survivors':0,'terrorism':0,'terrorist':0,'threat':0,'thunder':0,'thunderstorm':0,'tornado':0,'tragedy':0,'trapped':0,'trauma':0,'traumatised':0,'trouble':0,'tsunami':0,'twister':0,'typhoon':0,'upheaval':0,'violent storm':0,'volcano':0,'war zone':0,'weapon':0,'weapons':0,'whirlwind':0,'wild fires':0,'wildfire':0,'windstorm':0,'wounded':0,'wounds':0,'wreck':0,'wreckage':0,'wrecked':0}

dateKolkataCollapse = datetime.datetime(2016, 3, 31, 7, 2 , 0)

#print datetime.datetime.utcnow()
#print datetime.timedelta(minutes=10)
differenceOf24Hours = datetime.timedelta(hours=24)
#print datetime.datetime.utcnow() - datedifferenceOf10Minutes 
#print Tweets.count()

neededValueLast24HoursBeforeCollapse = dateKolkataCollapse - differenceOf24Hours
neededValue24HoursSinceCollapse = dateKolkataCollapse + differenceOf24Hours

print neededValueLast24HoursBeforeCollapse
print neededValue24HoursSinceCollapse
beforeCollapseTweets=Tweets.find({"created_at" : { '$gt' : neededValueLast24HoursBeforeCollapse , '$lt': dateKolkataCollapse } })
afterCollapseTweets=Tweets.find({"created_at" : { '$gt' : dateKolkataCollapse , '$lt': neededValue24HoursSinceCollapse }})

for content in beforeCollapseTweets:
    for issue in count.keys():
        if issue in content['text']:
            count[issue] += 1

#overView = db['Overview']
print "Before Collapse:" , count

for content in afterCollapseTweets:
    for issue in count.keys():
        if issue in content['text']:
            count[issue] += 1

print "After Collapse:" , count 
#result = db.overView.insert_one({"date": dateNow , "count": count} )
#print "Output: " , result
#print count    
    #print content['text']

