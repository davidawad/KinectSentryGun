import sys, os
import twitter
from secrets import *

def main(argv):

	# check args
	if len(argv) is not 2:
		print "Invalid number of arguments."
		return

	# make sure photo exists 
	if not os.path.exists('pictures/%s' % argv[1]):
		print "File not found."
		return

	# prepare twitter api
	api = twitter.Api(consumer_key=CONSUMER_KEY,
		consumer_secret=CONSUMER_SECRET,
		access_token_key=ACCESS_TOKEN,
		access_token_secret=ACCESS_SECRET)

	# make tweet
	status = api.PostMedia(status='Tango down.', 
		media='pictures/%s' % argv[1])
	print status.text

if __name__ == '__main__':
	main(sys.argv)