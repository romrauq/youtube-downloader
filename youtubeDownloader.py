import os
from pytube import YouTube

current_dir = os.getcwd()
arg_target_link = input("Enter YouTube Link: \n")
yt = YouTube(arg_target_link)

print()
print("Title:", yt.title)
print("Published:", yt.publish_date)
print("Views:", yt.views)

yd = yt.streams.get_by_itag(18)
yd.download(current_dir + "\Downloads")
