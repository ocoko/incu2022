from flask import Flask, request
import requests
import json

############## Bot details ##############

bot_name = 'Joke_Bot@webex.bot'
#roomId = 'Y2lzY29zcGFyazovL3VzL1JPT00vMWM4ZWRjMjQtMzBmYi0zZTFjLTk3OTgtODU5ZGVlMTYyNThl'
token = 'NGUxZTk0MzgtMDNmZi00YzIwLWFhODEtNzM5OWQxNmE5YWJiZGJkMDIxYjItOTIy_P0A1_17ec3022-497d-4eb1-a4df-d430c60c5a4d'
header = {"content-type": "application/json; charset=utf-8",
          "authorization": "Bearer " + token}

############## Flask Application ##############
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def sendMessage():
	webhook = request.json
	url = 'https://webexapis.com/v1/messages'
	msg = {"roomId": webhook["data"]["roomId"]}
	sender = webhook["data"]["personEmail"]
	message = getMessage()
	if (sender != bot_name):
		if (message == "help"):
			msg["markdown"] = " The **Joke_Bot** welcomes you to a small joke center!  \n List of available commands: " \
							  "\n- help " \
							  "\n- Hello" \
							  "\n- Give me a joke!" \
							  "\n- IT joke" \
							  "\n- I need a Mood Booster!"
		elif (message == "Hello"):
			msg["markdown"] = "Knock Knock"
		elif (message == "Who's there?"):
			msg["markdown"] = "Ya!"
		elif (message == "Ya who?"):
			msg["markdown"] = "No thanks, I prefer Google!"
		elif (message == "Not that funny"):
			msg["markdown"] = "Bill Gates says it is!"

		elif (message == "Give me a joke!"):
			msg["markdown"] = "How many programmers does it take to change a light bulb? \n None. It’s a hardware problem. "

		elif (message == "I need a Mood Booster!"):
			msg["markdown"] = "I'd send you a gif of a cute puppy, but my programmer doesn't know how to program it"

		elif (message == "IT joke"):
			msg["markdown"] = "There are 10 types of people in the world: those who understand binary, and those who don’t."
		else:
			msg["markdown"] = "Type **help** to see the list of available commands."
		requests.post(url,data=json.dumps(msg), headers=header, verify=True)

def getMessage():
	webhook = request.json
	url = 'https://webexapis.com/v1/messages/' + webhook["data"]["id"]
	get_msgs = requests.get(url, headers=header, verify=True)
	message = get_msgs.json()['text']
	return message

app.run(debug = True)
