import datetime
import pymongo
import pytz
import time
from pymongo import MongoClient
import datetime
from collections import Counter
import json
import requests
import wikipedia
from pygoogle import pygoogle
import duckduckgo
from googlesearch import GoogleSearch

client = MongoClient('localhost',27017)
utc=pytz.UTC
db = client['disaster']
threeHourlyAlert = db['threeHourlyAlert']
Tweets = db['Tweets']

incrementBy2Hour= datetime.timedelta(hours=2)

allDisasters = list(threeHourlyAlert.find())
disasterList = []
for disaster in allDisasters:
    for nameOfDisaster in disaster['count']:
        disasterList.append( (disaster['date'] , nameOfDisaster) )

markers = []
infoWindowContent = []
for date,disasterKeyWord in disasterList:
    date = date.replace(tzinfo=utc)
    dateFinal = date +  incrementBy2Hour
    dateFinal = dateFinal.replace(tzinfo=utc)
    disasterTweets = Tweets.find({"created_at" : { '$gt' : date , '$lt': dateFinal } , '$text': {'$search': disasterKeyWord}})#.count()
    d = Counter()
    for content in disasterTweets:
        for countContent in content['text'].split():
            d[countContent] += 1
    useToGetLocation = ""
    for k,v in d.most_common(100):
        useToGetLocation += k + " "
    payload = {'text':useToGetLocation,'demonyms': 'false'}
    r = requests.post("http://cliff.mediameter.org/process", data=payload)
    if (json.loads(r.text)['results']['places']['focus'] != {}):
        if (json.loads(r.text)['results']['places']['focus']['cities'] != []):
            location = json.loads(r.text)['results']['places']['focus']['cities']
        elif (json.loads(r.text)['results']['places']['focus']['states'] != []):
            location = json.loads(r.text)['results']['places']['focus']['states']
        elif (json.loads(r.text)['results']['places']['focus']['countries'] != []):
            location = json.loads(r.text)['results']['places']['focus']['countries']
        else:
            continue
    else:
        continue
    name=location[0]['name']
    lat=location[0]['lat']
    lon=location[0]['lon']
    searchText= disasterKeyWord + " " + name + " " + date.strftime("%d %B %Y")
    #print searchText
    search=GoogleSearch(searchText);
    time.sleep(300)
    wikiTitle = search.top_results()[0]['title']
    wikiURL = search.top_results()[0]['url']
    wikiContent = search.top_results()[0]['content']
    #wikiSearchList = wikipedia.search(searchText);
    #print wikiSearchList
    # for wikiSearch in wikiSearchList:
    #     if "2016" in wikiSearch :
    #         wikiSearchWord = wikiSearch
    #         break
    #     else:
    #         wikiSearchWord = wikiSearchList[0]
    # if ( wikiSearchWord != "" ):
    #     wikiContent = wikipedia.page(wikiSearch)
    #     wikiTitle = date.strftime("%d %B %Y") + " " + wikiContent.title 
    #     wikiPostConent = wikiContent.content.split('.')[0]
    #     wikiURL = wikiContent.url
    # else:
    #     #googleSearch = googlesearch(searchText)
    #     wikiTitle = date.strftime("%d %B %Y") + " " + disasterKeyWord + " at " + name  
    #     #wikiURL = googleSearch.get_urls()[0]
    #     #wikiPostConent = ""
    # wikiTitle = date.strftime("%d %B %Y") + " at " + name + " " + " Incident: " ;
    markers.append([ wikiTitle.encode('utf8') + " " + disasterKeyWord.encode('utf8') ,  lat , lon ])
    infoWindowContent.append([ '<div class="info_content">' + '<h3>' + wikiTitle.encode('utf8') +'</h3>' + '<br><h4>' + wikiContent.encode('utf8')  + '</h4>'  + '<br><p>' + wikiURL.encode('utf8') + '</p>' +'</div>' ])
    print markers
    print infoWindowContent
print markers
print infoWindowContent 
