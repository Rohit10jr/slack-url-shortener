import os, re, slack, string, random
import datetime, validators, json
from datetime import datetime
import requests  
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, jsonify, redirect, abort, render_template
from slackeventsapi import SlackEventAdapter
from flask_sqlalchemy import SQLAlchemy

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

slack_description = "Hi i am url shortener bot!\nInstall this app in any Slack channel.\nSimply paste the long URL that you want to shorten.\nThis app will automatically generate short urls for you.\nOnce the short URL is generated, Copy the short URL and share it with others."

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

# ----------------functions----------------
    
# function to generate unique short urls 
def short_link(length=6):
    characters = string.ascii_letters + string.digits
    while True:
        shorturl = ''.join(random.choice(characters) for i in range(6))
        url = Link.query.filter_by(short_url=shorturl).first()
        if not url:
            return shorturl

# function to remove <> from url 
def original_link(url):
    if url is not None and url.startswith("<") and url.endswith(">"):
        return url[1:-1]
    else:
        return url

def is_valid_url(text):
    # return validators.url(text)
    if validators.url(text):
        url = original_link(text)
        return url

# function to find if its url or not
def valid_url(text):
    if text is None:
        print("Text is None.")
        return None
    pattern = re.compile(r'^<?(https?://)[^>]*>?')
    return bool(pattern.match(text))

# funtion to check 
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
    host_url = request.url_root
    if valid_url(text):
        original_url = original_link(text)

        if user_id != BOT_ID and original_url:
            oldurl = Link.query.filter_by(original_url=original_url).first()
            if not oldurl:
                short_url = short_link()
                link = Link(original_url=original_url, short_url=short_url)
                db.session.add(link)
                db.session.commit()
                text = f"{host_url}{short_url}"
                client.chat_postMessage(
                        channel=channel_id, text=text)
            else:
                short_url = oldurl.short_url
                text = f"{host_url}{short_url}" 
                client.chat_postMessage(
                        channel=channel_id, text=text)
                
# route to redierct to original url from the shortened one
@app.route("/<short_url>")
def redirect_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first()
    if link:
        original_url = link.original_url
        # print(original_url)
        return redirect(original_url)
    else:
        return abort(404) 

# slack command handler
@app.route("/slack/command/", methods=["POST"])
def command():
    data = request.form

    if data["command"] == "/shorturl":
        message = slack_description
    else:
        message = f"Invalid command: {data['command']}"

    # Return response to Slack
    return ({"text": message})


# ----------------functions for url shortener site----------------

# route to show every stored links
@app.route("/list")
def model():
    model = Link.query.all()
    return render_template('list.html', model = model)

# home page route
@app.route("/", methods=['GET','POST'])
def main():
    if request.method=='POST':
        url = request.form['user_input']
        host_url = request.url_root
        if valid_url(url):
            original_url = original_link(url)
            oldurl = Link.query.filter_by(original_url=original_url).first()
            if not oldurl:
                short_url = short_link()
                link = Link(original_url=original_url, short_url=short_url)
                db.session.add(link)
                db.session.commit()        
                return render_template('main.html', text=f"{host_url}{short_url}")
            return render_template('main.html', text=f"{host_url}{oldurl.short_url}")
        return render_template("main.html", text="Not a Valid URL!, Please enter a valid URL.")
    return render_template("main.html")

# route to handle 404 
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)