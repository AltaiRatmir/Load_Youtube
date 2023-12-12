import os
import tkinter as tk
from tkinter import Label, Button, messagebox
from tkinter.ttk import Combobox
from pytube import YouTube, Playlist

file_Patch = os.getcwd() + '\\Video'


def download_video(link):
    link_yt = YouTube(link)
    btn['text'] = f'Идет загрузка {link_yt.title}'
    stream = link_yt.streams.get_highest_resolution()
    stream.download(file_Patch)
    messagebox.showinfo('Информация', f'Файл : <{link_yt.title}> загружен')
    btn['text'] = 'Скачать'


def download_playlist(link):
    my_playlist = Playlist(link)
    for video in my_playlist.videos:
        btn['text'] = f'Идет загрузка {video.title}'
        video.streams.get_highest_resolution().download(file_Patch)
    btn['text'] = 'Скачать'
    messagebox.showinfo('Информация', f'Плейлист : <{my_playlist.title}> загружен')


def download():
    try:
        link = entry_01.get()
        content_type = combo.get()
        global file_Patch
        file_Patch = file_Patch.replace(os.sep, '/')
        if content_type == 'одно видео':
            download_video(link)
        else:
            download_playlist(link)
    except:
        messagebox.showinfo('Информация', 'Неверные параметры')
    btn['text'] = 'Скачать'


my_window = tk.Tk()
my_window.title('Загрузка видео с YouTube')
# my_window.iconbitmap('icon.ico')
window_width = 1000
window_height = 115
my_window.minsize(width=window_width, height=window_height)
my_window.maxsize(width=window_width, height=window_height)

# Выравнивание программы по центру экрана
# Получение размеров экрана
screen_width = my_window.winfo_screenwidth()
screen_height = my_window.winfo_screenheight()
# Расчет координат для центрирования окна
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
# Установка координат для окна
my_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

my_lbl_01 = Label(my_window, text='Введите ссылку на видео : ')
my_lbl_01.place(x=5, y=10)
my_lbl_02 = Label(my_window, text='Куда будет сохранено видео : ')
my_lbl_02.place(x=5, y=40)
entry_01 = tk.Entry(my_window, width=130)
entry_01.place(x=180, y=10)
entry_02 = tk.Entry(my_window, width=130)
entry_02.insert(0, file_Patch)
entry_02.place(x=180, y=40)
my_lbl_03 = Label(my_window, text='Загружать : ')
my_lbl_03.place(x=5, y=75)
combo = Combobox(my_window, state='readonly', width=15)
combo['values'] = ('одно видео', 'весь плейлист')
combo.current(0)
combo.place(x=80, y=75)
btn = Button(my_window, text='Скачать', width=80, height=2, command=download)
btn.place(x=270, y=65)

my_window.mainloop()
