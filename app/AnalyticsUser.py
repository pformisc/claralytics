'''
	This class represents an AnalyticsUser, one who has a Google Analytics Account
'''
class AnalyticsUser(object):

	'''
		The constructor that initializes the accounts, web_properties, and the profiles
	'''
	def __init__(self, service):
		self.service = service
		self.accounts = self.retrieve_account()
		self.web_properties = self.init_web_properties()
		self.profiles = self.init_profiles()

	def retrieve_account(self):
		return self.service.management().accounts().list().execute()

	def init_web_properties(self):
		account_id = self.get_primary_account_id()
		web_properties = self.service.management().webproperties().list(accountId=account_id).execute()
		return web_properties

	def init_profiles(self):
		account_id = self.get_primary_account_id()
		web_properties_id = self.get_primary_web_properties_id()
		profiles = self.service.management().profiles().list(accountId=account_id, webPropertyId=web_properties_id).execute()
		return profiles

	def get_primary_account_id(self):
		return self.accounts.get('items')[0].get('id')

	def get_primary_web_properties_id(self):
		return self.web_properties.get('items')[0].get('id')

	def get_profiles_id(self):
		return self.profiles.get('items')[0].get('id')

	def get_username(self):
		return self.accounts.get('username')