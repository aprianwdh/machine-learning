import yt_dlp

ydl_opts = {}

url = "https://youtu.be/IFQ5tcFBtdc?si=dO167jOIjnqrFAGZ"

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

