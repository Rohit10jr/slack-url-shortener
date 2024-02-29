import os
import slack
import requests
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from slackeventsapi import SlackEventAdapter

# workspace = slack url shortener, App = short urls, channel = test

app = Flask(__name__)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events/', app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']

@slack_event_adapter.on('message')
def message(payload):
    print(payload)
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    if user_id != BOT_ID:
    # for i in range(1):
        client.chat_postMessage(
                channel=channel_id, text=text)



@app.route("/slack/command/", methods=["POST"])
def command():
    data = request.form

    if data["command"] == "/shorturl":
        message = "hi i am url shortener bot!"
    else:
        message = f"Invalid command: {data['command']}"

    # Return response to Slack
    return ({"text": message})


if __name__ == "__main__":
    app.run(debug=True)