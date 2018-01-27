import urllib.request
import urllib.parse
import re
import pytube
import os



#############
#  Note: 
#  Disable SSL Certificate 
#  
#############

query_string = urllib.parse.urlencode({"search_query" : input()})

html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
video_url = "http://www.youtube.com/watch?v=" + search_results[0]

yt = pytube.YouTube(video_url)
stream = yt.streams.first()

dest = "."
stream.download(dest)
print(yt.title + "\n has been successfully downloaded")




