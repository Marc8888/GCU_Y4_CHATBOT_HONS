import os
import json
import threading

from flask import Flask, json, request, send_from_directory
from deeppavlov import configs, build_model, train_model
from deeppavlov.core.common.file import read_json
from utility import Utility
from ml import MLChatBot

# Load the existing model
mlChatBot = MLChatBot()
mlChatBot.LoadModels()

# Get flask instance
web = Flask(__name__, static_url_path='')

# Static Assets
@web.route('/assets/<path:path>')
def send_js(path):
    return send_from_directory('web/assets', path)

# Get the webpage
@web.route('/', methods=['GET'])
def get_home():
	# While debugging, we want to just keep reloading the html file for changes
	return Utility.LoadFileString("web/pages-home.html")

@web.route('/help', methods=['GET'])
def get_help():
	# While debugging, we want to just keep reloading the html file for changes
	return Utility.LoadFileString("web/pages-help.html")

@web.route('/chat', methods=['GET'])
def get_chat():
	# While debugging, we want to just keep reloading the html file for changes
	return Utility.LoadFileString("web/pages-chat.html")

@web.route('/prototype', methods=['GET'])
def get_prototype():
	# While debugging, we want to just keep reloading the html file for changes
	return Utility.LoadFileString("web/prototype.html")

# Generate a chatbot response
@web.route('/chatbot/generate', methods=['post'])
def get_response():
	# Check if we have a message in the form and the message is a string
	if 'message' in request.form:
		# Check if our message is a string
		if type(request.form.get('message')) is str:
			message = request.form.get('message') # Get the message
			chatbotResponse = mlChatBot.GetResponse(message) # Run the chatbox model

			# Create the response
			response = {
				"message":		chatbotResponse[0],
				"probability":	chatbotResponse[1],
			}

			# Return the response
			return response
		else:
			return {
				"error": "Error: Message is not a string"
			}
	else:
		return {
			"error": "Error: No message found in request!"
		}

# Run the webserver (Multi threaded)
def flaskThread():
	web.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
	flaskThread()
	# If the web server is to be non blocking
	# threading.Thread(target=flaskThread).start()