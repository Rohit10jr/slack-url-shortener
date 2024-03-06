# Slack URL Shortener
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

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
git clone https://github.com/Rohit10jr/Ecommerce-site.git
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

1. First create and Sign in to your Slack account and create a new workspace.

![Screenshot (623)](https://github.com/Rohit10jr/slack-url-shortener/assets/130643902/3e2d16ff-a9d2-43e8-a1af-1b2cff3e119f)


2. Now open another browser tab and head to slack API site, click on the create your own app button.

![Screenshot (624)](https://github.com/Rohit10jr/slack-url-shortener/assets/130643902/53f885ed-c6b7-4ef8-ad90-353bf04bb860)

3. After that choose the option to create an app from scratch, and select the workspace you want.

![Screenshot (627)](https://github.com/Rohit10jr/slack-url-shortener/assets/130643902/2470e87f-28f8-440a-9d24-dd5e683570c9)

4. now go to basic information, fetch your signing secret, and paste it into your dot env(.env) file.

![Screenshot (628)](https://github.com/Rohit10jr/slack-url-shortener/assets/130643902/0516a4c7-6ff9-4be5-aee8-1166defb60fb)

5. navigate to the OAuth & Permissions feature, copy your slack token, and paste it into your dot env(.env) file.

![Screenshot (630)](https://github.com/Rohit10jr/slack-url-shortener/assets/130643902/da2dbd57-2743-436f-92d9-f46188d4fb34)

6. Then at OAuth & Permissions scroll down to Bot Token Scopes. Add all these scopes to your Slack app.

![Screenshot (628)](https://github.com/Rohit10jr/slack-url-shortener/assets/130643902/a60d1e80-2628-43a7-ac1e-4573dd603be9)

7. Now navigate to event subscriptions, and add the link you want the post request to be sent whenever an event occurs.



8. Go to the Slash Commands feature. Click on the Create New Command button.



9. After completing these installations and configurations, now update your project file with the necessary tokens and routes.

## Usage
wrtewrgq wewqefwefqwef

## Contributions

Contributions to the Awesome Slack URL Shortener are highly encouraged. To contribute, please follow these guidelines:
1. Fork the repository and create a new branch for your feature or bug fix.
2. Submit a pull request with a detailed description of your changes.
3. Happy Coding.

## Acknowledgments

This project was developed with Python and Flask and relies on various open-source libraries. Thanks to the Python and Flask community and contributors behind these tools.
