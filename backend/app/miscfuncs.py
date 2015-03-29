import sys, os
import twitter, pymongo
from secrets import *

def deleteTweet(tweetid):

	# prepare twitter api
	api = twitter.Api(consumer_key=CONSUMER_KEY,
		consumer_secret=CONSUMER_SECRET,
		access_token_key=ACCESS_TOKEN,
		access_token_secret=ACCESS_SECRET)

	# make tweet
	status = api.DestroyStatus(id=tweetid)

def getTweet(tweetid):

	# prepare twitter api
	api = twitter.Api(consumer_key=CONSUMER_KEY,
		consumer_secret=CONSUMER_SECRET,
		access_token_key=ACCESS_TOKEN,
		access_token_secret=ACCESS_SECRET)

	try:
		status = api.GetStatus(id=tweetid)
		if status.user.screen_name == 'kinectsentrygun':
			print 'found one of my tweets!'
			return status.id
		else:
			return False
	except twitter.error.TwitterError, e:
		# tweet does not exist
		return False

def findTransaction(transactionid):
	print 'result for transactionid: %s' % transactionid
	return getDatabase().transactions.find_one({'transactionid': transactionid})

def findTweet(tweetid):
	return getDatabase().transactions.find({'tweetid': tweetid})

def putTransaction(transactionid):
	getDatabase().transactions.insert({'transactionid':transactionid,
		'paid': 'False'})
	
def getDatabase():
	client = pymongo.MongoClient(os.environ.get('MONGODB_URL'))
	return client.transactionlist