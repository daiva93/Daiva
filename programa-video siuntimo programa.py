import sys
import youtube_dl 
DOWNLOAD_PATH = 'C:\\Users\'

def download_youtube_videos(video_url):
    stream = yt.streams.first()
    stream.download(DOWNLOAD_PATH)
    y = {} 
    while True: 
        link= input("Copy & paste the URL of the YouTube video you want to download:-") 
        youtube_dl.YoutubeDL(y).download([link])
        f=input("\nENETR YES(Y) TO CONTINUE DOWNLOADING VIDEOS \nELSE NO(N) TO STOP\n") 
        if f=="N" or f=="n":
            break

if __name__ == '__main__':
    arguments = sys.argv[1:]
    video_url = arguments[0]
    download_youtube_videos(video)
