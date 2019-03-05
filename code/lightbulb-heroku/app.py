# demo app for webhooks and python
# this app demonstrates a simple stateful web app 
# that can be controlled via webhooks
#
# this should be deployed at https://csci4849-demo.herokuapp.com
#
# it uses the following libraries:
# flask for parsing web requests: http://flask.pocoo.org
# redis for simple object storage: https://pypi.org/project/redis/
#
# this can be deployed for free using heroku. see example here:
# https://github.com/datademofun/heroku-basic-flask
#
# we use a simple redis database because heroku apps can't reliably
# retain their state. this uses the free heroku redis store
# from https://elements.heroku.com/addons/heroku-redis
#
# about this app: this app tracks the status of three lights in a house
# (kitchen, livingroom, bedroom). each can be turned on and off
# and the status can be read. in the current version, this just updates
# the database, but you should be able to connect this to real stuff
# without much work
#
# a good tutorial for the overall process is here:
# https://www.pragnakalp.com/dialogflow-fulfillment-webhook-tutorial/

from flask import Flask, request, jsonify
app = Flask(__name__)

import os
import redis
import json

# available light settings
LIGHTS = ['kitchen', 'livingroom', 'bedroom']

# use local settings for connecting to the database
# example from https://stackoverflow.com/questions/9383450/how-can-i-detect-herokus-environment
USE_LOCAL = not 'ON_HEROKU' in os.environ

# database functions go here

# connect to the database and return the db handle
def connectToDatabase():
	db = None
	if USE_LOCAL:
		db = redis.Redis(host='localhost', port=6379, db=0)
	else:
		db = redis.from_url(os.environ.get("REDIS_URL"))

	# initialize if we need to
	for light in LIGHTS:
		if not db.exists(light):
			db.set(light, 'off')		
	
	return db

# intitialize the database. we only need to do this once
# we set all the lights to off		
# 
# note here that we are just using the light name as database variable names
# in a real app we would probably want to use some namespace prefix to keep
# everything from getting jammed up

def initialize(db):
	for light in LIGHTS:
		db.set(light, 'off')

# set the value of a light. we'll use strings to represent on and off
def setLight(db, light, value):
	if not light in LIGHTS:
		raise Error("Invalid light")
	db.set(light, value)

# get the value of a light. as noted above, we'll use strings to represent on and off
def getLight(db, light):
	if not light in LIGHTS:
		raise Error("Invalid light")
	return db.get(light)
	
# get the status of all the lights in a dict
def getStatus(db):
	status = {}
	for light in LIGHTS:
		status[light] = getLight(db, light)
	return status

# web code goes down here
# this provides a simple web interface to our database

@app.route("/")
def root():
	return """
	<h1>Commands:</h1>
	<ul>
		<li>/status - report the status of each light</li>
		<li>/get/{light} - return the light status</li>
		<li>/set/{light} - set the light status to on or off</li>
		<li>/reset - reset the database</li>
		<li>/lastRequest - see JSON of the last webhook request (for debugging)</li>
	</ul>
	"""

@app.route("/get/<light>")
def webGetLight(light):
	db = connectToDatabase()
	value = getLight(db, light)
	return "The " + light + " light is " + value

@app.route("/set/<light>/<value>")
def webSetLight(light, value):
	db = connectToDatabase()
	setLight(db, light, value)
	return "The " + light + " light is now " + value


# for readability's sake, here we represent the status as HTML
# below in the webhook section we represent it as a string
# to improve understandability of the text
# if textOnly is true, strip out the html

@app.route("/status")
def webStatus(textOnly=False):
	db = connectToDatabase()
	status = getStatus(db)
	
	# return status as a string (to work with dialogflow)
	statusString = ""
	for light in LIGHTS:
		if textOnly:
			statusString += "The " + light + " light is " + status[light] + ". "
			
		else:
			statusString += "The <strong>" + light + "</strong> light is <em>" + status[light] + "</em>.<br/>"
			
	return statusString

@app.route("/reset")
def webReset():
	db = connectToDatabase()
	initialize(db)
	return "ok"

# this is for debugging the webhook code
# it just prints out the json of the last webhook request
@app.route("/lastRequest")
def lastRequest():
	db = connectToDatabase()
	req = db.get("lastRequest")
	return req

# webhook code goes here
# this is set to receive a webhook request from DialogFlow
# see https://dialogflow.com/docs/fulfillment/how-it-works for details
# 
# basically, the url /dialog will expect a JSON object as described above
# and will parse the attached JSON object, then do stuff

@app.route("/dialog", methods=["POST"])
def handleDialog():
	data = request.get_json()
	
	# save this request for debugging
	db = connectToDatabase()
	db.set("lastRequest", json.dumps(data))
	
	# debug
	# print data
	
	# now, do stuff based on the JSON data
	# in particular we want to look at the queryResult.intent.displayName to
	# see which intent is triggered, and queryResult.parameters to see params
	
	if data['queryResult']['intent']['displayName'] == "getOverallStatus":
		response = webStatus(True)
		print response
		return jsonify({'fulfillmentText': response})
	elif data['queryResult']['intent']['displayName'] == "getLightStatus":
		lightName = data['queryResult']['parameters']['light-name']
		response = webGetLight(lightName)
		print response
		return jsonify({'fulfillmentText': response})
	elif data['queryResult']['intent']['displayName'] == "setLightStatus":
		lightName = data['queryResult']['parameters']['light-name']
		lightStatus = data['queryResult']['parameters']['light-status']
		# set the light and get the response
		response = webSetLight(lightName, lightStatus)
		print response
		return jsonify({'fulfillmentText': response})
	