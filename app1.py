import os
import re
import json
import slack
import string
import random
# import datetime
from datetime import datetime
import requests  
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, jsonify, redirect, abort, render_template
from slackeventsapi import SlackEventAdapter
import pyshorteners
from flask_sqlalchemy import SQLAlchemy
# workspace = slack url shortener, App = short urls, channel = test

app = Flask(__name__)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# database
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# slack 
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events/', app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']

# model
class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(3), unique=True)
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"{self.id}:{self.short_url}"
    
with app.app_context():
    db.create_all()


# functions
def short_link(length=6):
    characters = string.ascii_letters + string.digits
    while True:
        shorturl = ''.join(random.choice(characters) for i in range(6))
        url = Link.query.filter_by(short_url=shorturl).first()
        if not url:
            return shorturl

def original_link(url):
    if url.startswith("<") and url.endswith(">"):
        return url[1:-1]
    else:
        return url
    
def valid_url(text):
    url_pattern = re.compile(
        r'^(https?|ftp)://'  # Scheme (http, https, or ftp)
        r'([A-Za-z0-9.-]+)'  # Domain
        r'(:\d+)?'           # Port (optional)
    )
    match_result = re.match(url_pattern, text)

    if match_result:
        return text
    return False

def check_url(text):
    if valid_url(text):
        return original_link(text)
    return None

@slack_event_adapter.on('message')
def message(payload):
    # print(payload)
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    print(text)
    original_url = original_link(text)
    print(original_url)

    if user_id != BOT_ID and original_url:
        short_url = short_link()
        print(short_url)
        oldurl = Link.query.filter_by(original_url=original_url).first()
        print(oldurl.short_url)
        if not oldurl:
            link = Link(original_url=original_url, short_url=short_url)
            db.session.add(link)
            db.session.commit()
            text = f"https://3c4a-106-222-220-55.ngrok-free.app/{short_url}" 
            client.chat_postMessage(
                    channel=channel_id, text=text)
        else:
            short_url = oldurl.short_url
            print(short_url)
            text = f"https://3c4a-106-222-220-55.ngrok-free.app/{short_url}" 
            client.chat_postMessage(
                    channel=channel_id, text=text)


@app.route("/<short_url>")
def redirect_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first()
    if link:
        original_url = link.original_url
        print(original_url)
        return redirect(original_url)
    else:
        return abort(404) 


@app.route("/slack/command/", methods=["POST"])
def command():
    data = request.form

    if data["command"] == "/shorturl":
        message = "hi i am url shortener bot!"
    else:
        message = f"Invalid command: {data['command']}"

    # Return response to Slack
    return ({"text": message})


# html 
@app.route("/model")
def model():
    model = Link.query.all()
    return render_template('list.html', model = model)

@app.route("/")
def main():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)