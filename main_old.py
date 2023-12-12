import os
from pytube import YouTube, Playlist

file_Patch = os.getcwd() + '\\Video'


def download_video(link):
    link_yt = YouTube(link)
    print("Заголовок : ", link_yt.title)
    stream = link_yt.streams.get_highest_resolution()
    stream.download(file_Patch)
    print('Видео загружено')


def download_playlist(link):
    my_playlist = Playlist(link)
    for video in my_playlist.videos:
        video.streams.get_highest_resolution().download(file_Patch)
        print(f'Видео : <{video.title}> загрузилось')
    print(f'Плейлист : <{my_playlist.title}> загружен')


def download():
    link = input('Введите ссылку: ')
    content_type = input('Если нужно загрузить одно видео введите <1>, если плейлист введите <2> : ')
    global file_Patch
    file_Patch = file_Patch.replace(os.sep, '/')
    if content_type == '1':
        download_video(link)
    elif content_type == '2':
        download_playlist(link)
    else:
        print('Неизвестная опция')


download()
