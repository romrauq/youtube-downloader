from pytube import YouTube
from sys import argv	

arg_target_link = argv[1]

yt = YouTube(arg_target_link)

print("Title:", yt.title)
print("Views:", yt.views)


yd = yt.streams.get_by_itag(18)

yd.download("C:\\Users\\Romrauq\\Downloads\\YoutubeDownloader")

