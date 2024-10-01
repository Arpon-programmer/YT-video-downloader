import yt_dlp

url = 'https://www.youtube.com/watch?v=LcazglPE8CU'
download_folder = '/Volumes/PEN_DRIVE/Songs/%(title)s.%(ext)s'  # Define your desired path and file name format

ydl_opts = {
    'format': 'bestaudio/best',  # Get the best available audio
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',  # Download as MP3
        'preferredquality': '192',
    }],
    'outtmpl': download_folder,  # Specify download path with filename format
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])