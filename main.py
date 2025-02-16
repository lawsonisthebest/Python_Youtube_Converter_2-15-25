import yt_dlp, os
import rumps
import tkinter as tk
from tkinter import simpledialog

class MyApp(rumps.App):
    def __init__(self):
        super(MyApp, self).__init__("Converter", icon="icon.svg")  # Set app name and icon
        self.menu = ["MP3 Convert", "MP4 Convert"]  # Menu items
        
    @rumps.clicked("MP3 Convert")  # Action when clicking menu item
    def convert_mp3(self, _):
        response = rumps.Window(
            title="Youtube Mp3 Converter",
            message="Paste the url down below:",
            default_text="",
            ok="Convert",
            cancel="Cancel"
        ).run()

        # If user submits, show a notification with the entered text
        if response.clicked:
            ydl_opts = {
                'format': 'bestaudio/best',  # Best audio format
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',  # Use FFmpegExtractAudio instead of FFmpegAudioConvertor
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': os.path.join(os.getcwd()+'/downloads', '%(title)s.%(ext)s'),  # Save the file with the video title
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                try:
                    print(f"Downloading {response.text}...")
                    ydl.download([response.text])
                    print("Download complete!")
                except Exception as e:
                    print(f"An error occurred: {e}")
                    
    
    
    
    @rumps.clicked("MP4 Convert")  # Action when clicking menu item
    def convert_mp4(self, _):
        response = rumps.Window(
            title="Youtube Mp4 Converter",
            message="Paste the url down below:",
            default_text="",
            ok="Convert",
            cancel="Cancel"
        ).run()

        # If user submits, show a notification with the entered text
        if response.clicked:
            ydl_opts = {
                'format': 'bestvideo/best',  # Best audio format
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',  # Use FFmpegExtractAudio instead of FFmpegAudioConvertor
                    'preferredcodec': 'mp4',
                    'preferredquality': '192',
                }],
                'outtmpl': os.path.join(os.getcwd()+'/downloads', '%(title)s.%(ext)s'),  # Save the file with the video title
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                try:
                    print(f"Downloading {response.text}...")
                    ydl.download([response.text])
                    print("Download complete!")
                except Exception as e:
                    print(f"An error occurred: {e}")


if __name__ == "__main__":
    MyApp().run()