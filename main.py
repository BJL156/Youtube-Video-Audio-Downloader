import pytube
import os
from tkinter import filedialog
import tkinter

def make_file_name_suitable(title):
    # Remove characters that can't be in a folder/file name
    invalid_folder_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for chars in invalid_folder_chars:
        title = title.replace(chars, '')
    
    # Remove all non ascii characters
    title = ''.join(char for char in title if ord(char) < 128)

    return title

def main():
    while True:
        url = input("Enter YouTube URL: ")

        try:
            yt = pytube.YouTube(url)
        
            audio = yt.streams.get_audio_only()
            video = yt.streams.filter().get_highest_resolution()

            file_name = make_file_name_suitable(yt.title)
            
            # YouTube video information
            print(file_name)
            print(f"Video URL: {yt.watch_url}")
            print(f"Thumnail URL: {yt.thumbnail_url}")
            print(f"Views: {yt.views}")
            print(f"Length: {yt.length}s")
            print(f"Age restricted: {yt.age_restricted}")
            print(f"Channel URL: {yt.channel_url}")

            # Ask for a directory to download to
            root = tkinter.Tk()
            root.withdraw()
            directory = filedialog.askdirectory()
            print(directory)
            os.chdir(directory)

            # Create folder
            os.mkdir(file_name)
            os.chdir(file_name)
            
            # Download video and audio
            video.download(filename=f"{file_name}.mp4")
            print(f"YouTube video downloaded at file location: {directory + '/' + file_name + '/' + file_name + '.mp4'}")
            audio.download(filename=f"{file_name}.mp3")
            print(f"YouTube video audio downloaded at file location: {directory + '/' + file_name + '/' + file_name + '.mp3'}")
        except:
            print(f"Failed to find YouTube video: {url}")
            input("Press enter to continue...")

if __name__ == '__main__':
    main()
