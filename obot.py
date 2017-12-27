import praw

username = ""
password = ""
ua = "searches for images in subreddits by /u/hipereeon" 
app_id = ""
app_secret = ""

def login():
    r = praw.Reddit(client_id = app_id,
                    client_secret = app_secret,
                    user_agent=ua,
                    username = username,
                    password = password)
    return r