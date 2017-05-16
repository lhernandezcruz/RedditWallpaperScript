# imgurWallpaper
Python script that gets an imgur image from top post of day (of a subreddit) and sets it as wallpaper. 

## What is required to run
### Runs on python 2.7.11, pip, and uses PRAW 5.0.0
Python 2.7.11 (comes with pip) can be downloaded here: https://www.python.org/downloads/release/python-2711/
Praw can be installed using the command: `pip install praw`

### Currently only tested on Windows 10

### Requires a reddit account and an "app"
To create a reddit account go to https://www.reddit.com/register/. 

To create an app for the account go to https://www.reddit.com/prefs/apps/.
- Give it a name
- Click `script`
- Give it a redirect uri of http://localhost:8080

# How to run
Once everything has been completed download the files and put in the correct information in obot.py (username, password, user agent, app id and app secret). For the user agent put something descriptive such as `Gets image from top posts from subreddit`. Then run `python -i imgurWallpaper.py` and it should do everything from there. 




