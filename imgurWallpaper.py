import urllib, obot, datetime, ctypes, os

# SPI_SETDESKWALLPAPER is used to set as wallpaper in Windows
SPI_SETDESKWALLPAPER = 20 

# get the current day and use it to save the files by day
now = datetime.datetime.now()
day = now.strftime("%m-%d-%Y")
filename =  day + ".jpg"

# path is the path of where the file is
path = os.path.dirname(os.path.abspath(__file__))
    
""" 
"   downloadImage()
"     input : imageUrl, localFileName
"     function: gets image from imageUrl and saves it to localFileName
"""
def downloadImage(imageUrl, localFileName):
    #if images directory does exist not in current direcotry make it
    if not (os.path.isdir(os.path.join(path,"images"))):
        try:
            print "Creating Images Directory"
            os.makedirs(os.path.join(path,"images"))
        except:
            print "Failed to make directory"
            return False
        
        
    # retrieve image from imageUrl
    try:
        urllib.urlretrieve(imageUrl, os.path.join("images", localFileName))
        print "Download Successful"
        return True
    except:
        print "Couldn't downlaod the image"
        return False
    
"""
"  setBackground()
"    input: localFileName
"    function: sets the file at localFileName as the wallpaper
"""    
def setBackground(localFileName): 
    print "Attempting to Set as Wallpaper"
    try:
        imgPath = os.path.join(path, localFileName)
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, imgPath , 3)
        print "Set as Wallpaper"
    except:
        print "Failed to set as wallpaper"
    
    
"""
"   getImage()
"     input: none
"     function: get imgur post from subreddit and call downloadImage()
"""
def getImage():
    try:
        # log in to reddit
        print "Logging into reddit"
        r = obot.login()
        print "Logged in as " + str(r.user.me())
    except:
        # failed to log in
        print "Failed to log in. Please double check user info"
        return
        
    while True :
        # entering a subreddit
        print "Please enter a subreddit. Ex: Wallpaper, Wallpapers, EarthPorn"
        sub = raw_input("subreddit: ")
        # getting subreddit
        subreddit = r.subreddit(sub)  
        
        try:
            r.subreddits.search_by_name(sub, exact=True)
        except:
            print "The subreddit does not exist. Please try again."
            continue
        
        
        # gettings posts
        print "Searching Posts in " + subreddit.display_name + " for Imgur image"
        posts = subreddit.top(time_filter = 'day')
        
        found = False
        for post in posts:
            url = post.url
        
            # make sure it is an imgur image only
            # currently doesn't work with albums
            if "imgur.com/" not in url:
                continue
            if "http://imgur.com/a/" in url:
                continue
        
            # if it got here it is imgur... download it
            print "Found Imgur Picture. URL: " + url
            found = True
            # if it is jpg...downlaod and set as wallpaper and stop searching
            if ".jpg" in url:
                found = downloadImage(url,filename)
                setBackground(os.path.join("images", filename))
                break 
        
        ## check if we found image
        if found:
            break
        else:
            print "No imgur image found. Try a different subreddit"
            continue
        
getImage()
