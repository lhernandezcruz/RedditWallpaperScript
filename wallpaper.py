import urllib.request, obot, datetime, ctypes, os


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
"     input : imageUrl
"     function: gets image from imageUrl and saves it to localFileName
"""
def downloadImage(imageUrl):
    #if images directory does exist not in current direcotry make it
    if not (os.path.isdir(os.path.join(path,"images"))):
        try:
            print("Creating Images Directory")
            os.makedirs(os.path.join(path,"images"))
        except:
            print("Failed to make directory")
            return False
        
        
    # retrieve image from imageUrl
    try:
        print(imageUrl)
        urllib.request.urlretrieve(imageUrl, os.path.join("images", filename))
        print("Download Successful")
        return True
    except:
        print("Couldn't downlaod the image")
        return False
    
"""
"  setBackground()
"    function: sets the file at localFileName as the wallpaper
"""    
def setBackground(): 
    print("Attempting to Set as Wallpaper")
    try:
        imgPath = os.path.join(path, os.path.join("images",filename))
        print(imgPath)
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imgPath , 3)
        print("Set as Wallpaper")
    except:
        print("Failed to set as wallpaper")
    
    
"""
"   getImage()
"     function: get imgur post from subreddit and call downloadImage()
"""
def getImage():
    try:
        # log in to reddit
        print("Logging into reddit")
        r = obot.login()
        print("Logged in as " + str(r.user.me()))
    except:
        # failed to log in
        print("Failed to log in. Please double check user info")
        return
        
    while True :
        # entering a subreddit
        print("Please enter a subreddit. Ex: Art, Wallpaper, Wallpapers, EarthPorn")
        sub = input("subreddit: ")
        # getting subreddit
        subreddit = r.subreddit(sub)  
        
        try:
            r.subreddits.search_by_name(sub, exact=True)
        except:
            print("The subreddit does not exist. Please try again.")
            continue
        
        # gettings posts
        print("Searching Posts in " + subreddit.display_name + " for image")
        posts = subreddit.top(time_filter = 'day')
        
        found = False
        for post in posts:
            url = post.url

            # make sure it is a jpg
            if url.endswith(".jpg"):
                print("Found  Picture. URL: " + url)
                found = downloadImage(url)
                setBackground()
                break 
 
        ## check if we found image
        if found:
            break
        else:
            print("No image found. Try a different subreddit")
            continue
        
getImage()
