import urllib, obot, datetime, ctypes, os

#can change subreddit to something else... ex: gonewild...jk lol
sub = "Wallpaper"

# SPI_SETDESKWALLPAPER is used to set as wallpaper in Windows
SPI_SETDESKWALLPAPER = 20 

# get the current day and use it to save the files by day
now = datetime.datetime.now()
day = now.strftime("%m-%d-%Y")
filename =  day + ".jpg"

# path is the path of where the file is
path = os.path.dirname(os.path.abspath(__file__))
    
# log on to reddit
print "Logging into reddit"
r = obot.login()
print "Logged in as " + str(r.user)

""" 
"   downloadImage()
"     input : imageUrl, localFileName
"     function: gets image from imageUrl and saves it to localFileName
"""
def downloadImage(imageUrl, localFileName):
    #if images directory does not in current direcotry make it
    if not (os.path.isdir(os.path.join(path,"images"))):
        print "Creating Images Directory"
        os.makedirs(os.path.join(path,"images"))
        print "Downloading Image. URL: " + imageUrl
        
    # retrieve image from imageUrl
    urllib.urlretrieve(imageUrl, os.path.join("images", localFileName))
    print "Download Succesful"
    
"""
"  setBackground()
"    input: localFileName
"    function: sets the file at localFileName as the wallpaper
"""    
def setBackground(localFileName): 
    print ("Attempting to Set as Wallpaper")
    imgPath = os.path.join(path, localFileName)
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, imgPath  , 3)
    print "Set as Wallpaper"
    
"""
"   getImages()
"     input: none
"     function: get imgur post from wallpapers subreddit and call downloadImage()
"""
def getImages():
    # get wallpapers subreddit
    subreddit = r.get_subreddit(sub)
    
    # check each post
    print "Searching Posts for Imgur image"
    posts = subreddit.get_top_from_day(limit=10)
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
        
        # if it is jpg...downlaod and set as wallpaper and stop searching
        if ".jpg" in url:
            downloadImage(url,filename)
            setBackground(os.path.join("images", filename))
            break 
        else:
            downloadImage(url  + ".jpg",filename)
            setBackground(os.path.join("images", filename))
            break
        
getImages()
    
