# Slack URL Shortener App
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)

This is a Slack URL Shortener app. This app automatically detects long URLs posted in your Slack channels and instantly generates concise short URLs, Now, easily share links without cluttering your messages and enjoy quick access to important resources. Simplify your communication with the Slack URL Shortener app and say goodbye to lengthy URLs.

## Demo 

slack URL shortener app demonstration gif.

![slackurl](https://github.com/Rohit10jr/slack-url-shortener/assets/130643902/ecdaf253-5f47-4334-b810-7d5beeafcc0f)

## Table of Contents

1. [Features](#features)
2. [Getting Started](#getting-started)
   - [Installation](#installation)
   - [Configuration](#configuration)
3. [Usage](#usage)
4. [Contributions](#contributions)
5. [Acknowledgments](#acknowledgments)

## Features

- **Automatic Detection:** The app identifies long URLs shared in channels.
- **Instant Shortening:** Generates short URLs in real-time.
- **Cleaner Messages:** Share links with a cleaner look and feel.
- **Effortless Access::** Short URLs redirect to the original links.
- **Seamless Integration:** Enhance your Slack experience with this lightweight and user-friendly app.

## Getting Started

Follow these steps to get your Slack URL Shortener up and running:

### Installation

1. Clone the repository:
```
https://github.com/Rohit10jr/slack-url-shortener.git
```  
2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate
```

3. Install the project dependencies:
```
pip install -r requirements.txt
```

4. Apply database migrations

## Configuration

1. Begin by creating a Slack account on the Slack website, then Sign in to your Slack account and create a new workspace.

![Screenshot (624)](https://github.com/Rohit10jr/slack-url-shortener/assets/130643902/53f885ed-c6b7-4ef8-ad90-353bf04bb860)

2. Now Open a new browser tab and navigate to the Slack API site, click on the "Create your own app" button.

![Screenshot (627)](https://github.com/Rohit10jr/slack-url-shortener/assets/130643902/2470e87f-28f8-440a-9d24-dd5e683570c9)

3. After that Select the option to create an app from scratch, and choose the desired workspace you want.

![Screenshot (628)](https://github.com/Rohit10jr/slack-url-shortener/assets/130643902/0516a4c7-6ff9-4be5-aee8-1166defb60fb)

4. Now go to "Basic information", fetch your signing secret, and securely store it in your dotenv(.env) file.

![Screenshot (618)](https://github.com/Rohit10jr/slack-url-shortener/assets/130643902/571ba5b4-5f7d-42fd-8e96-ce8cc4999dd0)

5. Navigate to the "OAuth & Permissions" feature, copy your slack token, and paste it into your .env file.

![Screenshot (619)](https://github.com/Rohit10jr/slack-url-shortener/assets/130643902/077d7120-1e40-446b-b181-0fc0b3718464)

6. Then at "OAuth & Permissions" scroll down to Bot Token Scopes, and add these required scopes for your Slack app.

![Screenshot (620)](https://github.com/Rohit10jr/slack-url-shortener/assets/130643902/a2b65e0b-bc4e-463b-b81a-6dba161ea2a9)

7. In the "Event Subscriptions", add the desired link to receive POST requests for events.

![Screenshot (621)](https://github.com/Rohit10jr/slack-url-shortener/assets/130643902/63c05ad9-a809-4e6f-90c1-54cd807b62a6)

8. Navigate to the "Slash Commands" feature and create a new command, Configure the command settings as per your wish.

![Screenshot (630)](https://github.com/Rohit10jr/slack-url-shortener/assets/130643902/da2dbd57-2743-436f-92d9-f46188d4fb34)

9. After completing these installations and configurations update all necessary tokens and routes. Now, your Slack URL Shortener app is configured and ready for use!

## Usage

This app automatically detects long URLs posted in your Slack channels and instantly generates concise short URLs, this app helps for sharing cleaner and more manageable URLs within your Slack workspace. Simplify your communication with the Slack URL Shortener app.

## Contributions

Contributions to the Awesome Slack URL Shortener are highly encouraged. To contribute, please follow these guidelines:
1. Fork the repository and create a new branch for your feature or bug fix.
2. Submit a pull request with a detailed description of your changes.
3. Happy Coding.

## Acknowledgments

This project was developed with Python and Flask and relies on various open-source libraries. Thanks to the Python and Flask community and contributors behind these tools.
