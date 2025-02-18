import yt_dlp
import os
import sys

def download_mp3(url):
    script_dir = os.path.dirname(sys.executable)  # Get script directory
    parent_dir = os.path.dirname(script_dir)
    
    ydl_opts = {
        'format': 'bestaudio/best',  # Best audio format
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Use FFmpegExtractAudio instead of FFmpegAudioConvertor
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(parent_dir, 'downloads', '%(title)s.%(ext)s'),  # Save the file with the video title
        'ignoreerrors': True,  # Ignore errors and continue
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"Downloading {url}...")
            ydl.download([url])
            print("Download complete!")
        except Exception as e:
            print(f"An error occurred with {url}: {e}")

if __name__ == "__main__":
    while True:
        print("--------------------------------")
        url = input("Enter The URL (or type 'exit' to quit): ")
        print("--------------------------------")
        if url.lower() == 'exit':
            break
        download_mp3(url)
