from AnalyticsUser import AnalyticsUser
from datetime import date

import simplejson as json

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

	'''
		Gets the username of the AnalyticsUser
	'''
	def get_username(self):
		return self.user.get_username()

	'''
		Queries the Analytics API for the number of visitors per device type.
		Device categories include:
		1) Desktop
		2) Mobile
		3) Tablet
	'''
	def query_device_type(self):
		user_profile_id = self.user.get_primary_profile_id()
		current_date = date.today()
		device_metrics = 'ga:visitors'
		device_dimensions = 'ga:deviceCategory'

		# Execute this query
		result = self.service.data().ga().get(
			ids='ga:' + user_profile_id,
			start_date=date(current_date.year, current_date.month, 1).isoformat(),
			end_date=current_date.isoformat(),
			metrics='ga:visitors',
			dimensions='ga:deviceCategory'
		).execute()

		device_categories = result.get('rows')
		device_dict = dict()

		for elem in device_categories:
			device_dict[elem[0]] = int(elem[1])

		return json.dumps(device_dict, sort_keys=True)

	def query_weekly_visits(self):
		current_date = date.today()
		weekly_visits = list()

		day_count = 6

		while day_count >= 0:
			result = self.service.data().ga().get(
				ids='ga:' + self.user.get_primary_profile_id(),
				start_date=date(current_date.year, current_date.month, current_date.day-day_count).isoformat(),
				end_date=current_date.isoformat(),
				metrics='ga:visitors'
			).execute()
			weekly_visits.append(result.get('rows'))
			day_count = day_count - 1

		return weekly_visits