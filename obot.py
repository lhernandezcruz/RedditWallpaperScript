import praw

ua = '' 
app_id = ''
app_secret = ''
app_uri = ''


app_account_code = ''
app_refresh = ''

def login():
    r = praw.Reddit(ua);
    r.set_oauth_app_info(app_id, app_secret, app_uri)
    r.refresh_access_information(app_refresh)
    return r