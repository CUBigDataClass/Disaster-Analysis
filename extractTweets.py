import tweepy
import sys

# user application credentials
consumer_key = "5uzIc3mu5bdqKfgPM2Mysnc0V"
consumer_secret = "cDrkl7CIZlzLfN6688xjJDmN5l2EDX8brTcfZCZUPjoDOdYfh8"

access_token = "4904583673-vMkTnb7l9pnR1X6wPhI8ceDR4BCwqexZzYvOWEl"
access_token_secret = "GiCJGDGW5m61Ew8NRl3Y6zbLuz8Ndlar7hD9CprwsSqxi"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

    def on_status(self, status):
        print status.text , "\n"

    # handle errors without closing stream:
    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True 

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True 

sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))
sapi.filter(track=['disaster'])
