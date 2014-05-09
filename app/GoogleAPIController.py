from AnalyticsUser import AnalyticsUser
from datetime import date, timedelta

import simplejson as json

'''
	This class represents the GoogleAPIController.
	The main functionality of this class is to manage all the requests & responses,
	to & from the Google Analytics API
'''
class GoogleAPIController(object):

	custom_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	
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
		device_dict = dict()

		# Execute this query
		result = self.service.data().ga().get(
			ids='ga:' + user_profile_id,
			start_date=date(self.current_date.year, self.current_date.month, 1).isoformat(),
			end_date=self.current_date.isoformat(),
			metrics='ga:visitors',
			dimensions='ga:deviceCategory'
		).execute()

		device_categories = result.get('rows')
		if device_categories is not None:
			for elem in device_categories:
				device_dict[elem[0]] = int(elem[1])

		return json.dumps(device_dict, sort_keys=True)

	'''
		Queries the Analytics API for the number of visitors per day.
		The query is run from the first day of the week (Monday) to the current date
	'''
	def query_weekly_visits(self):
		weekly_visits = list()

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

			if result.get('rows') is not None:
				cust_month = self.custom_months[start_date.month-1] + ' ' + str(start_date.day)
				weekly_visits.append([cust_month, int(result.get('rows')[0][0])])
			day_count -= 1

		return json.dumps(weekly_visits, sort_keys=True)

	'''
		Queries the Analytics API for the number of visitors in the current month.
		The month is partitioned into several weeks and the visitors for each week are reported.
	'''
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

	'''
		Queries the Analytics API for the top 5 most popular pages viewed in this month.
	'''	
	def query_popular_articles(self):

		start_date = date(self.current_date.year, self.current_date.month, 1)		
		end_date = self.current_date

		pop_articles = list()

		result = self.service.data().ga().get(
			ids='ga:' + self.user.get_primary_profile_id(),
			start_date=start_date.isoformat(),
			end_date=end_date.isoformat(),
			metrics='ga:pageviews',
			dimensions='ga:pageTitle',
			sort='ga:pageviews'
		).execute()

		if result.get('rows') is not None:
			res_list = result.get('rows')[-6:-1]
			res_list.reverse()

			for page in res_list:
				pop_articles.append([page[0].replace('|', ''), int(page[1])])

		return pop_articles

	def query_geo_network(self):
		start_date = date(self.current_date.year, self.current_date.month, 1)		
		end_date = self.current_date + timedelta(days=1)
		geo_network = dict()

		result = self.service.data().ga().get(
			ids='ga:' + self.user.get_primary_profile_id(),
			start_date=start_date.isoformat(),
			end_date=end_date.isoformat(),
			metrics='ga:visitors',
			dimensions='ga:country, ga:region',
			sort='ga:country'
		).execute()

		if result.get('rows') is not None:
			res_list = [elem for elem in result.get('rows') if elem[0] == 'United States']

			

			for elem in res_list:
				if elem[1] != '(not set)':
					if elem[1] != 'Hawaii':
						geo_network[elem[1]] = int(elem[2])

		return json.dumps(geo_network, sort_keys=True)
'''
	def query_google_plus_actions(self):
		start_date = date(self.current_date.year, self.current_date.month, 1)		
		end_date = self.current_date

		result = self.service.data().ga().get(
			ids='ga:' + self.user.get_primary_profile_id(),
			start_date=start_date.isoformat(),
			end_date=end_date.isoformat(),
			metrics='ga:socialInteractions'
		).execute()

		return 1 
'''