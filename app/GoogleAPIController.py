from AnalyticsUser import AnalyticsUser

'''
	This class represents the GoogleAPIController.
	The main functionality of this class is to manage all the requests & responses,
	to & from the Google Analytics API
'''
class GoogleAPIController(object):

	'''
		The constructor for a GoogleAPIController
		Initializes the credentials & the httpObj attributes
	'''
	def __init__(self, service):
		self.name = "GoogleAPIController"
		self.service = service
		self.user = AnalyticsUser(self.service)

	def get_username(self):
		return self.user.get_username()

