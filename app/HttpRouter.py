import httplib2

import flask
from flask import render_template, redirect, request, session, url_for, make_response, Flask
from app import app
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.client import FlowExchangeError

from DashBoardController import DashBoardController

'''
	The index function renders the welcome page on request
'''
@app.route('/', methods=['GET'])
def index():
	credentials = session.get('credentials')
	if credentials is not None:
		return redirect(url_for('dashboard'))
	
	return render_template("index.html")

'''
	The dashboard function renders the dashboard page on request
	If the user is not logged in, redirect the user back to the home page
'''
@app.route('/dashboard',  methods=['GET'])
def dashboard():
	credentials = session.get('credentials')
	httpObj = httplib2.Http()

	if credentials is not None:
		db_controller = DashBoardController(credentials, httpObj)
		db_controller.fetch_social_activities()
		username = db_controller.display_username()
		return render_template("dashboard_new.html", username=username, controller=db_controller)

	return redirect(url_for('index'))

'''
	The login function redirects the user to the Google Authorization page
'''
@app.route('/login', methods=['GET'])
def login():
	auth_flow = constructFlow() # Get the Flow object
	'''
		Call the Flow object's authorize_url()
		This returns a URL to Google's login page
	'''
	auth_uri = auth_flow.step1_get_authorize_url() 
	return redirect(auth_uri)

'''
	The logout function removes all the user related credentials from the session
	It then redirects the user back to the home page
'''
@app.route('/logout', methods=['GET'])
def logout():
	session.pop('credentials', None)
	#flask.session.regenerate()
	return redirect(url_for('index')) 

'''
	The authorization_redirect function is a callback function.
	It receives the authorization code from Google and requests an access token
'''
@app.route('/oauth2callback')
def authorization_redirect():
	auth_code = request.args.get('code', None)
	auth_credentials = None

	if auth_code:
		auth_flow = constructFlow()
		try:
			auth_credentials = auth_flow.step2_exchange(auth_code)
		except FlowExchangeError:
			print "Could not exchange code for credentials"

		session['credentials'] = auth_credentials

		flask.session.regenerate()

	return redirect(url_for('dashboard'))

'''
	Constructs a Flow object and returns it
'''
def constructFlow():
	flow_obj = OAuth2WebServerFlow(client_id = app.config['CLIENT_ID'], 
		client_secret = app.config['CLIENT_SECRET'],
		scope = app.config['SCOPE'],
		redirect_uri = app.config['REDIRECT_URI'])
	return flow_obj
