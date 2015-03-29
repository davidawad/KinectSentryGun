from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from flask import Flask, render_template, redirect, request
from forms import MainForm
from miscfuncs import *
app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
def root():
	form = MainForm()
	if form.validate_on_submit():
		return redirect(form.authorizeTransaction())
	return render_template('base.html', title='Kinect Sentry Gun', form=form)

@app.route('/callback/', methods=['GET', 'POST'])
def callback():

	if ('destination_address' in request.args) and ('input_transaction_hash' in request.args):
		print "hello!"
		if request.args['destination_address'] == os.environ['WALLET_ID']:
			print 'placing transaction! %s' % request.args['input_transaction_hash']
			putTransaction(request.args['input_transaction_hash'])
			return '*ok*'
	return ':('

if __name__ == '__main__':
	http_server = HTTPServer(WSGIContainer(app))
	http_server.listen(5000)
	IOLoop.instance().start()