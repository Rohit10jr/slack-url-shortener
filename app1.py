import os
import requests
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from slack_bolt.adapter.flask import SlackRequestHandler
from slack_bolt import App

app = Flask(__name__)

# workspace = slack url shortener, App = short urls, channel = test

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

slack_app = App(
    token=os.environ['SLACK_TOKEN'],
    signing_secret=os.environ['SIGNING_SECRET']
)

@app.route("/slack/command/", methods=["POST"])
def command():
    data = request.form

    if data["command"] == "/shorturl":
        message = "hi i am url shortener bot!"
    else:
        message = f"Invalid command: {data['command']}"

    # Return response to Slack
    return ({"text": message})

# handler = SlackRequestHandler(slack_app)

if __name__ == "__main__":
    app.run(debug=True)