import sys
import tweepy
#~ import configparser
import json

#~ from kafka.client import KafkaClient
from kafka.producer import KafkaProducer


consumer_key = "5uzIc3mu5bdqKfgPM2Mysnc0V"
consumer_secret = "cDrkl7CIZlzLfN6688xjJDmN5l2EDX8brTcfZCZUPjoDOdYfh8"

access_token = "4904583673-vMkTnb7l9pnR1X6wPhI8ceDR4BCwqexZzYvOWEl"
access_token_secret = "GiCJGDGW5m61Ew8NRl3Y6zbLuz8Ndlar7hD9CprwsSqxi"

count = 0


class TweeterStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

        #~ self.db = pymongo.MongoClient().disaster

        #~ client = KafkaClient(hosts='127.0.0.1:9092')
        #~ self.producer = KafkaProducer(bootstrap_servers='localhost:9092')
        #~ self.producer = SimpleProducer(client, async = True,
                          #~ batch_send_every_n = 1000,
                          #~ batch_send_every_t = 10)

    def on_status(self, status):
        print status.text, "\n"

        #~ data ={}
        #~ data['text'] = status.text
        #~ data['created_at'] = status.created_at
        #~ data['geo'] = status.geo
        #~ data['source'] = status.source
        #~ self.db.Tweets.insert(data)

        msg =  status.text.encode('utf-8')

        producer = KafkaProducer(bootstrap_servers='0.0.0.0:9092')
        #~ producer = KafkaProducer(bootstrap_servers=['broker1:1234'])
        #print(msg)
        try:
            producer.send(b'twitterstream', msg)
        except Exception as err:
            print(err)
            return False
        return True

        #~ topic = client.topics[str('tweets')]
        #~ with topic.get_producer(delivery_reports=False) as producer:
    
            #~ # print status.text
            #~ sentence = status.text
            #~ for word in sentence.split(" "):
                #~ if word is None:
                    #~ continue
                #~ try:
                    #~ word = str(word)
                    #~ producer.produce(word)
                #~ except:
                    #~ continue

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream



if __name__ == '__main__':

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    sapi = tweepy.Stream(auth, listener = TweeterStreamListener(api))
    sapi.filter(track=['ablaze','accident','aftershock','airplane accident','ambulance','annihilated','annihilation','apocalypse','armageddon','army','arson','arsonist','attack','attacked','avalanche','battle','bioterror','bioterrorism','blaze','blazing','bleeding','blew up','blight','blizzard','blood','bloody','blown up','body bag','body bagging','body bags','bomb','bombed','bombing','bridge collapse','buildings burning','buildings on fire','burned','burning','burning buildings','bush fires','casualties','casualty','catastrophe','catastrophic','chemical emergency','cliff fall','collapse','collapsed','collide','collided','collision','crash','crashed','crush','crushed','curfew','cyclone','damage','danger','dead','death','deaths','debris','deluge','deluged','demolish','demolished','demolition','derail','derailed','derailment','desolate','desolation','destroy','destroyed','destruction','detonate','detonation','devastated','devastation','disaster','displaced','drought','drown','drowned','drowning','dust storm','earthquake','electrocute','electrocuted','emergency','emergency plan','emergency services','engulfed','epicentre','evacuate','evacuated','evacuation','explode','exploded','explosion','eyewitness','famine','fatal','fatalities','fatality','fear','fire','fire truck','first responders','flames','flattened','flood','flooding','floods','forest fire','forest fires','hail','hailstorm','harm','hazard','hazardous','heat wave','hellfire','hijack','hijacker','hijacking','hostage','hostages','hurricane','injured','injuries','injury','inundated','inundation','keyword','landslide','lava','lightning','loud bang','mass murder','mass murderer','massacre','mayhem','meltdown','military','mudslide','natural disaster','nuclear disaster','nuclear reactor','obliterate','obliterated','obliteration','oil spill','outbreak','pandemonium','panic','panicking','police','quarantine','quarantined','radiation emergency','rainstorm','razed','refugees','rescue','rescued','rescuers','riot','rioting','rubble','ruin','sandstorm','screamed','screaming','screams','seismic','sinkhole','sinking','siren','sirens','smoke','snowstorm','storm','stretcher','structural failure','suicide bomb','suicide bomber','suicide bombing','sunk','survive','survived','survivors','terrorism','terrorist','threat','thunder','thunderstorm','tornado','tragedy','trapped','trauma','traumatised','trouble','tsunami','twister','typhoon','upheaval','violent storm','volcano','war zone','weapon','weapons','whirlwind','wild fires','wildfire','windstorm','wounded','wounds','wreck','wreckage','wrecked'])

    #~ client = KafkaClient("localhost:9092")
    #~ producer = SimpleProducer(client)

