import httplib2

'''
	This class represents the GoogleAPIController.
	The main functionality of this class is to manage all the requests & responses,
	to & from the Google Analytics API
'''
class GoogleAPIController(object):
	def __init__(self, credentials):
		self.name = "GoogleAPIController"
		self.credentials = credentials
		self.httpObj = httplib2.Http()

	'''
		Authorizes the specified credentials and returns the user's username
	'''
	def getUserName(self):
		self.httpObj = self.credentials.authorize(httpObj)
		service = build('analytics', 'v3', http=httpObj)

		accounts = service.management().accounts().list().execute()
		return accounts['username']