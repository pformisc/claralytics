import httplib2
import json

from GoogleAPIController import GoogleAPIController
from apiclient.discovery import build

'''
	This class represents the DashBoardController.
	Its responsibilities include
'''
class DashBoardController(object):

	def __init__(self, credentials, httpObj):
		self.credentials = credentials
		self.httpObj = self.credentials.authorize(httpObj)
		self.service = build('analytics', 'v3', http=self.httpObj)
		self.gapicontroller = GoogleAPIController(self.service)

	def display_username(self):
		return self.gapicontroller.get_username()

	def fetch_device_type(self):
		return self.gapicontroller.query_device_type()

	def fetch_weekly_visits(self):
		return self.gapicontroller.query_weekly_visits()

	def fetch_monthly_visits(self):
		return self.gapicontroller.query_monthly_visits()

	def fetch_popular_articles(self):
		return self.gapicontroller.query_popular_articles()

	def fetch_geo_network(self):
		return self.gapicontroller.query_geo_network()

	def fetch_social_activities(self):
		return self.gapicontroller.query_google_plus_actions()