from yt_dlp import YoutubeDL

URL = ["https://www.youtube.com/watch?v=GtUQB4DCONQ"]
with YoutubeDL() as ydl:
    ydl.download(URL)
