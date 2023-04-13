import pytube
import os
import requests
import re
import pyfiglet
import time
import webbrowser

logo = pyfiglet.figlet_format("Download Videos By Ghalwash")
print(logo)
print("")


choice = input("What do you want to do?\n1) Open developer accounts\n2) Run script\n")


if choice == "1":
        webbrowser.open("http://t.me/mrfa0gh")
        webbrowser.open("https://www.instagram.com/mrfa0gh")
        webbrowser.open('https://twitter.com/mrfa0gh')
 
elif choice == "2":
        print("Script is running...")
else:
        print("Invalid choice.")

# Ask the user for the playlist link
playlist_link = input("Please enter the link to the YouTube playlist: ")

# Create a YouTube playlist object using the link
playlist = pytube.Playlist(playlist_link)

# Loop through each video in the playlist and download the audio
for video in playlist.videos:
    # Get the audio stream of the video
    audio_stream = video.streams.filter(only_audio=True).first()
    
    # Download the audio stream
    print(f"Downloading audio from {video.title}...")
    audio_file = audio_stream.download()
    
    # Convert the audio file to an mp3 file using ffmpeg
    print("Converting audio file to mp3 format...")
    os.system(f"ffmpeg -i {audio_file} -vn -ar 44100 -ac 2 -b:a 192k -f mp3 {video.title}.mp3")
    
    # Get the path of the directory containing the converted audio file
    audio_dir = os.path.dirname(os.path.abspath(audio_file))
    
    # Print the path of the converted audio file
    print(f"Audio file saved at {audio_dir}/{video.title}.mp3")

print("All audio files downloaded and converted successfully!")
