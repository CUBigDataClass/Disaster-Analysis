from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import csv
import re
import datetime

import pymongo
from pymongo import MongoClient

from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet

import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.feature_selection import SelectKBest, f_regression, chi2

from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

from sklearn.pipeline import Pipeline
from sklearn.cross_validation import KFold, cross_val_score
from sklearn.metrics import accuracy_score

import sys
reload(sys)
sys.setdefaultencoding('utf8')

client = MongoClient('localhost', 27017)
db = client['disaster']
realTimeCount10Sec = db['second']

count = {'bomb': 0, 'violent storm': 0, 'hijacker': 0, 'bombed': 0, 'sunk': 0, 'avalanche': 0, 'debris': 0, 'body bag': 0, 'battle': 0, 'fear': 0, 'weapons': 0, 'catastrophe': 0, 'forest fire': 0, 'ruin': 0, 'buildings burning': 0, 'blaze': 0, 'fatal': 0, 'airplane accident': 0, 'sinking': 0, 'electrocute': 0, 'rescue': 0, 'hostage': 0, 'massacre': 0, 'traumatised': 0, 'trouble': 0, 'screaming': 0, 'suicide bomb': 0, 'annihilated': 0, 'loud bang': 0, 'floods': 0, 'quarantine': 0, 'obliterate': 0, 'cliff fall': 0, 'body bagging': 0, 'snowstorm': 0, 'whirlwind': 0, 'disaster': 0, 'bleeding': 0, 'razed': 0, 'famine': 0, 'armageddon': 0, 'wreck': 0, 'thunder': 0, 'wrecked': 0, 'crush': 0, 'burned': 0, 'sirens': 0, 'explosion': 0, 'screams': 0, 'rescuers': 0, 'bridge collapse': 0, 'survivors': 0, 'fatality': 0, 'earthquake': 0, 'accident': 0, 'flames': 0, 'detonate': 0, 'mass murderer': 0, 'smoke': 0, 'military': 0, 'stretcher': 0, 'blizzard': 0, 'danger': 0, 'bloody': 0, 'panicking': 0, 'drowned': 0, 'eyewitness': 0, 'devastation': 0, 'bush fires': 0, 'army': 0, 'heat wave': 0, 'emergency plan': 0, 'tragedy': 0, 'collided': 0, 'survive': 0, 'injury': 0, 'riot': 0, 'attacked': 0, 'fire': 0, 'bioterrorism': 0, 'wounds': 0, 'quarantined': 0, 'drown': 0, 'hailstorm': 0, 'casualties': 0, 'mass murder': 0, 'demolish': 0, 'collision': 0, 'pandemonium': 0, 'sandstorm': 0, 'electrocuted': 0, 'landslide': 0, 'flooding': 0, 'mayhem': 0, 'rainstorm': 0, 'demolition': 0, 'blew up': 0, 'hijacking': 0, 'siren': 0, 'terrorist': 0, 'inundated': 0, 'damage': 0, 'lava': 0, 'devastated': 0, 'forest fires': 0, 'outbreak': 0, 'terrorism': 0, 'panic': 0, 'detonation': 0, 'injured': 0, 'deluged': 0, 'windstorm': 0, 'thunderstorm': 0, 'hazard': 0, 'crushed': 0, 'crashed': 0, 'blood': 0, 'buildings on fire': 0, 'destruction': 0, 'deluge': 0, 'weapon': 0, 'sinkhole': 0, 'aftershock': 0, 'ambulance': 0, 'wreckage': 0, 'desolate': 0, 'blown up': 0, 'fatalities': 0, 'injuries': 0, 'bombing': 0, 'structural failure': 0, 'death': 0, 'police': 0, 'destroyed': 0, 'engulfed': 0, 'crash': 0, 'emergency': 0, 'inundation': 0, 'collide': 0, 'blight': 0, 'destroy': 0, 'dust storm': 0, 'mudslide': 0, 'displaced': 0, 'arsonist': 0, 'nuclear reactor': 0, 'blazing': 0, 'lightning': 0, 'explode': 0, 'tsunami': 0, 'burning buildings': 0, 'volcano': 0, 'hijack': 0, 'refugees': 0, 'derailment': 0, 'harm': 0, 'hail': 0, 'bioterror': 0, 'hurricane': 0, 'trauma': 0, 'evacuation': 0, 'cyclone': 0, 'epicentre': 0, 'nuclear disaster': 0, 'hostages': 0, 'obliteration': 0, 'suicide bomber': 0, 'drowning': 0, 'derailed': 0, 'threat': 0, 'apocalypse': 0, 'chemical emergency': 0, 'burning': 0, 'obliterated': 0, 'screamed': 0, 'fire truck': 0, 'seismic': 0, 'wildfire': 0, 'emergency services': 0, 'attack': 0, 'storm': 0, 'catastrophic': 0, 'twister': 0, 'evacuated': 0, 'natural disaster': 0, 'collapse': 0, 'trapped': 0, 'war zone': 0, 'exploded': 0, 'collapsed': 0, 'oil spill': 0, 'evacuate': 0, 'typhoon': 0, 'dead': 0, 'survived': 0, 'first responders': 0, 'keyword': 0, 'radiation emergency': 0, 'annihilation': 0, 'deaths': 0, 'rubble': 0, 'ablaze': 0, 'meltdown': 0, 'casualty': 0, 'body bags': 0, 'upheaval': 0, 'flood': 0, 'demolished': 0, 'rioting': 0, 'hellfire': 0, 'curfew': 0, 'hazardous': 0, 'tornado': 0, 'desolation': 0, 'flattened': 0, 'drought': 0, 'derail': 0, 'arson': 0, 'rescued': 0, 'suicide bombing': 0, 'wild fires': 0, 'wounded': 0}


def update_dict():
    #count = dict.fromkeys(count, 0)
    for issue in count.keys():
        count[issue] = 0

def update_count(content):
    sen = re.sub(r'[^A-Za-z0-9_ ]', "", content)
    for issue in count.keys():
        if issue in sen:#unicode(content).encode('utf-8'):
            count[issue] += 1
    #return count.items()

def addToDb(stime):#keywordCount, countAverage):
    #noOfTimesTheAverage = {x:float(count[x])/countAverage[x] for x in countAverage}
    result = db.realTimeCount10Sec.insert_one({"date": stime , "count": count})
    return result

def get_tag(tag):
    if tag in ['NN', 'NNS', 'NNP', 'NNPS']:
        return wordnet.NOUN
    elif tag in ['RB', 'RBR', 'RBS']:
        return wordnet.ADV
    elif tag in ['JJ', 'JJR', 'JJS']:
        return wordnet.ADJ
    else:
        return wordnet.VERB


def stem_tokens(tokens):
    stemmer = PorterStemmer()
    stems = [stemmer.stem(t) for t in tokens]
    return stems

def tokenize_doc(doc):
    wnl = WordNetLemmatizer()
    tok = word_tokenize(doc)
    #~ pos_list = pos_tag(tok)
    #~ tokens = [wnl.lemmatize(pt[0], get_tag(pt[1])) for pt in pos_list]
    tokens = [wnl.lemmatize(t, wordnet.VERB) for t in tok]
    #~ stems = stem_tokens(tokens)
    #~ return stems
    return tokens


def test_feature(clf, test):
    # return clf.transform(np.asarray(test))
    return clf.fit(np.asarray(test))

def classify_tweet(clf, test_vector):
    return clf.predict(np.asarray(test_vector))

class ClassifyTweet(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        self.starttime = datetime.datetime.now()
        self.train = []
        self.label = []
        self.tweet_count = 0
        self.tweet_list = []

        with open('/home/ec2-user/storm_kafka/wordcount/src/bolts/disaster-tweets-DFE.csv', 'rb') as data:
            has_header = csv.Sniffer().has_header(data.read(1024))
            data.seek(0)
            csvreader = csv.reader(data)
            if has_header:
                next(csvreader)

            for row in csvreader:
                self.train.append(row[10])
                self.label.append(row[5])

        self.clf = Pipeline([
                        ('vect',
                                TfidfVectorizer(
                                        analyzer='word',
                                        ngram_range=(1, 1),
                                        stop_words = 'english',
                                        lowercase=True,
                                        token_pattern=r'\b\w+\b',
                                        tokenizer=tokenize_doc,
                                        min_df = 1)),
                        #('dim_reduction',
                        #        TruncatedSVD(n_components=1000)),
                        ('classification',
                                MultinomialNB())
                                #~ LogisticRegression())
                                #~ SVC(kernel = 'linear'))
                ])

        self.clf.fit(np.asarray(self.train), np.asarray(self.label))


    def process(self, tup):
        word = tup.values[0]
        #self.counts[word] += 1

        #self.tweet_count += 1
        #if (len(self.tweet_list) == 0):
        #    self.tweet_list.append("ghost ********* SSS")
        #else:
        self.tweet_list.append(word)
        
        msg = "TWEET || "
        self.log('%s: %s' % (msg, word))
        
        update_count(word) #self.keywords)
        current = datetime.datetime.now()
        diff = current - self.starttime

        #issue = "emergency"
        #if issue in unicode(word).encode('utf-8'):
        #    sen = re.sub(r'[^A-Za-z0-9_ ]', "", word)
        #    self.tmpc += 1
        #    self.log('%s: %d' % (issue, self.tmpc))

        if diff.seconds > 10:
            res = addToDb(self.starttime) #self.keywords, self.countAverage)
            update_dict()
            self.starttime = datetime.datetime.now()


        if (len(self.tweet_list) >= 200):
            msg = "ghost *************************************%%%%%%%%%%%%%%%%%%%%%%%%$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
            self.log('%s' % (msg))
            #tv = test_feature(self.clf, self.tweet_list)
            c = classify_tweet(self.clf, self.tweet_list)

            #msg = "ghost CCCCCCCCCCCCCCCCC"
            #self.log('%s: %s %d' % (msg, len(c), self.tweet_count))
            for i in range(len(c)):
                if c[i] == "Relevant":
                    #msg = "ghost REL "
                    #self.log('%s | %s' % (msg, self.tweet_list[i]))
                    self.emit([self.tweet_list[i]])

            self.tweet_list = []

        #self.emit([word])
        #if c is 1:
        #pred = 9998765
        #else:
        #    pred = 7777777
        #self.log('%s: %d' % (word, pred))
