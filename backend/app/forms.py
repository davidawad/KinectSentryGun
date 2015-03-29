from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from miscfuncs import *

class MainForm(Form):
	tweetid = StringField('tweetid', validators=[DataRequired()])
	transactionid = StringField('transactionid', validators=[DataRequired()])

	def validate(self):
		# make sure fields are filled in
		if not Form.validate(self):
			print 'form did not validate'
			return False

		# make sure transaction exists
		transac = findTransaction(self.transactionid.data)
		if transac == None:
			print 'nonexistant transaction'
			self.transactionid.errors.append("error")
			return False

		# make sure transaction hasn't been claimed yet
		if transac['paid'] == 'True':
			print 'transaction claimed'
			self.transactionid.errors.append("error")
			return False

		# # make sure tweet hasn't been claimed yet
		# if findTweet(self.tweetid.data) is not None:
		# 	if findTweet(self.tweetid.data)['paid'] == 'True':
		# 		print 'tweet claimed'
		# 		self.tweetid.errors.append("error")
		# 		return False

		# make sure tweet exists
		print getTweet(self.tweetid.data)
		if getTweet(self.tweetid.data) == None:
			print 'didnt find tweet'
			self.tweetid.errors.append("error")
			return false

		return True

	def authorizeTransaction(self):
		getDatabase().transactions.update(
			{'transactionid': self.transactionid.data},
			{
				'$set':{
						'paid': 'True',
						'tweetid': self.tweetid.data
				}
			})
		deleteTweet(self.tweetid.data)
		return "http://twitter.com/kinectsentrygun"