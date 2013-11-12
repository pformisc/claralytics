from flask import Flask 
from simplekv.memory import DictStore
from flaskext.kvsession import KVSessionExtension

app = Flask(__name__)
app.config.from_object('config')

store = DictStore()

KVSessionExtension(store, app) 

'''
	Import the HttpRouter module to take care of basic URL routing
'''
from app import HttpRouter