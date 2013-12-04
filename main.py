'''
	Comment the google appengine import statements,
	when running the application purely on Flask.

	If running the app via appengine, then uncomment the 
	appropriate import statements
'''
from google.appengine.ext.webapp.util import run_wsgi_app
from app import app

#app.run(debug=True)

run_wsgi_app(app)