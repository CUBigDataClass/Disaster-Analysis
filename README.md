# Disaster-Analysis
## The objective of the project is to detect disaster around the world and help people communicate for help at the time of disaster.

######Install Mongodb and virtualenv.
Get twitter developement account and application information by visiting: *https://apps.twitter.com ( Create a new app )*

######Steps: Initial Setup ( All of them to be done from home path of the repository. )



  * One time:

`mkdir data` ( To store the database content locally )
`virtualenv -p /usr/bin/python venv` ( To use a seperate python environment for this project )
`source venv/bin/activate` ( To active the virtual enviroment. Needs to be done every time.)
`pip install tweepy`
`pip install pymongo`

  * Everytime you want to get and store information:

`source venv/bin/activate`
`mongod --dbpath data/`

  - For testing the information that we are getting:

`python extractTweets.py` 

    - Modify track to add more keywords for tracking.

  - For storing the data into Mongodb:

`python storeTweetsInMongoDBUsingTweepy.py`