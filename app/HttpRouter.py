import httplib2

from flask import render_template, redirect, request, session, url_for, make_response
from app import app
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.client import FlowExchangeError
from apiclient.discovery import build

'''
	The index function renders the welcome page on request
'''
@app.route('/', methods=['GET'])
def index():
	if 'credentials' in session:
		return redirect(url_for('dashboard'))
	
	return render_template("index.html")
	
'''
	The dashboard function renders the dashboard page on request
	If the user is not logged in, redirect the user back to the home page
'''
@app.route('/dashboard',  methods=['GET'])
def dashboard():
	if 'credentials' in session:
		username = getUserName(session['credentials'])
		return render_template("dashboard.html", username=username)

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
	del session['credentials']
	return redirect(url_for('index')) 

'''
	The authorization_redirect function is a callback function.
	It receives the authorization code from Google and requests an access token
'''
@app.route('/oauth2callback')
def authorization_redirect():
	auth_code = request.args.get('code', None)

	if auth_code:
		auth_flow = constructFlow()
		try:
			auth_credentials = auth_flow.step2_exchange(auth_code)
		except FlowExchangeError:
			print "Could not exchange code for credentials"

		session['credentials'] = auth_credentials

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

'''
	Authorizes the specified credentials and returns the user's username
'''
def getUserName(credentials):
	httpObj = httplib2.Http()
	httpObj = credentials.authorize(httpObj)
	service = build('analytics', 'v3', http=httpObj)

	accounts = service.management().accounts().list().execute()
	return accounts['username']