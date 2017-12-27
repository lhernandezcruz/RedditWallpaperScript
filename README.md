# imgurWallpaper
Python script that gets an imgur image from top post of day (of a subreddit) and sets it as wallpaper. 

### Currently only tested on Windows 10

## Setup
### Requires Python
Runs on Python 3.3 to 3.6. Python 3.6 (comes with pip) can be downloaded here: https://www.python.org/downloads/.
### Requires Praw
Praw can be installed using the command: `pip install praw`

### Requires a Reddit account and an "app"
To create a Reddit account go to https://www.reddit.com/register/. 

To create an app for the account go to https://www.reddit.com/prefs/apps/.
- Give it a name: Ex: wallpaperGetter
- Click `script`
- Give it a redirect uri of http://localhost:8080

# How to run
Once everything has been completed download the files and put in the correct information in obot.py (username, password, user agent, app id and app secret).

Once information is set in obot.py run `py wallpaper.py` and it should do everything from there.

# Authors
* Luis Hernandez Cruz - lhernandezcruz@g.hmc.edu
