
import os
#import youtube_dl

with open("url.txt", "r") as f:
    urls = f.read().splitlines()

print(urls)

out_directory = os.path.join("home", "tcsmilpitascoderschool", "PycharmProjects"
, "elizabeth")



ydl_opts = {
    'format':
    'bestaudio/best',
    'outtmpl':
    os.path.join(out_directory, '%(title)s.%(ext)s'),
    'rejecttitle': 'True',
    'postprocessors':
    [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}]
    'extractaudio':
    'True,'
    'audioformat':
    'mp3',
    'nooverwrites':
    'True',
    'noplaylist':
    'True',
    'nocheckercertificate':
    'True'
        }

with youtube_dl.Youtube(ydl_opts) as ydl:
    for url in urls:
        ydl.download([url])

