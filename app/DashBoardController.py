import httplib2

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