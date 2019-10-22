

import sys
arguments = sys.argv[1:]
filename = arguments[0]
import youtube_dl 
stream = yt.streams.first()
stream.download('C:\\Users\')
y= {} 
while True: 
    link= input("Copy & paste the URL of the YouTube video you want to download:-") 
    youtube_dl.YoutubeDL(y).download([link])
    f=input("\nENETR YES(Y) TO CONTINUE DOWNLOADING VIDEOS \nELSE NO(N) TO STOP\n") 
    if f=="N" or f=="n":
        break
