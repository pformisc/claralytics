from GoogleAPIController import GoogleAPIController

'''
	This class represents the DashBoardController.
	Its responsibilities include
'''
class DashBoardController(object):
	def __init__(self):
		self.gapicontroller = GoogleAPIController()
		self.name = "Dashboard"

	def getName(self):
		return "This name: " + self.name + " GAPI Name: " + self.gapicontroller.name
