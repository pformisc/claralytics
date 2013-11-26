import httplib2
from GoogleAPIController import GoogleAPIController

'''
	This class represents the DashBoardController.
	Its responsibilities include
'''
class DashBoardController(object):
	def __init__(self, credentials):
		self.gapicontroller = GoogleAPIController(credentials)

	def get_profile_ID(self):
		profile_id = "id"
		return profile_id

'''
	Authorizes the specified credentials and returns the user's username
'''
def getUserName(credentials):
	httpObj = httplib2.Http()
	httpObj = credentials.authorize(httpObj)
	service = build('analytics', 'v3', http=httpObj)

	accounts = service.management().accounts().list().execute()
	return accounts['username']
