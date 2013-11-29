from AnalyticsUser import AnalyticsUser
from datetime import date, timedelta

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
		self.current_date = date.today()

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
		device_metrics = 'ga:visitors'
		device_dimensions = 'ga:deviceCategory'

		# Execute this query
		result = self.service.data().ga().get(
			ids='ga:' + user_profile_id,
			start_date=date(self.current_date.year, self.current_date.month, 1).isoformat(),
			end_date=self.current_date.isoformat(),
			metrics='ga:visitors',
			dimensions='ga:deviceCategory'
		).execute()

		device_categories = result.get('rows')
		device_dict = dict()

		for elem in device_categories:
			device_dict[elem[0]] = int(elem[1])

		return json.dumps(device_dict, sort_keys=True)

	'''
		Queries the Analytics API for the number of visitors per day.
		The query is run from the first day of the week (Monday) to the current date
	'''
	def query_weekly_visits(self):
		weekly_visits = dict()

		day_count = self.current_date.weekday()
		while day_count >=0:
			start_date = self.current_date - timedelta(days=day_count)
			end_date = start_date + timedelta(days=1)

			result = self.service.data().ga().get(
				ids='ga:' + self.user.get_primary_profile_id(),
				start_date=start_date.isoformat(),
				end_date=end_date.isoformat(),
				metrics='ga:visitors',
			).execute()

			weekly_visits[start_date.isoformat()]=int(result.get('rows')[0][0])
			day_count -= 1

		return json.dumps(weekly_visits, sort_keys=True)

	def query_monthly_visits(self):
		monthly_visits = dict()
		
		start_date = date(self.current_date.year, self.current_date.month, 1)		
		end_date = self.current_date

		result = self.service.data().ga().get(
			ids='ga:' + self.user.get_primary_profile_id(),
			start_date=start_date.isoformat(),
			end_date=end_date.isoformat(),
			metrics='ga:visitors',
			dimensions='ga:nthWeek'
		).execute()
		
		for elem in result.get('rows'):
			week_num = int(elem[0]) + 1
			monthly_visits[week_num] = int(elem[1])

		return json.dumps(monthly_visits, sort_keys=True)