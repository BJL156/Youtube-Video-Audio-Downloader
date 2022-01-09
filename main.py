from pytube import YouTube
import os, re
os.chdir('videos')

yt = str()
def set_up():
    global yt
    print('Youtube Video and Audio Downloader\n'
        'BJL156\n')
    url = input('Enter a URL: ')
    # never gonna give you up: https://www.youtube.com/watch?v=dQw4w9WgXcQ

    yt = YouTube(url)
def main():
    set_up()
    video = yt.streams.filter(res=yt.streams.filter().get_highest_resolution().resolution).first()
    audio = yt.streams.filter(only_audio = True).first()


    folder_name = yt.title.replace('[', '')
    folder_name = folder_name.replace(']', '')
    folder_name = re.sub('[\/:*?"<>|「」]', '', folder_name)
    while len(folder_name) > 156:
        folder_name = folder_name[:-1]
    os.mkdir(yt.title)
    
    while len(folder_name) > 68:
        folder_name = folder_name[:-1]
        print(len(folder_name))

    video.download(output_path=folder_name, filename=f'{folder_name}.mp4')
    audio.download(output_path=folder_name, filename=f'{folder_name}.mp3')
if __name__ == '__main__':
    main()