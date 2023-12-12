import os
import urllib.request
import customtkinter
import requests
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
# from tkinter import Label, Button, messagebox
# from tkinter.ttk import Combobox
from pytube import YouTube, Playlist
from PIL import Image

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('green')

file_Patch = os.getcwd() + '\\Video'
file_Patch = file_Patch.replace(os.sep, '/')


def my_fun(link):
    urllib.request.urlretrieve(link.thumbnail_url, file_Patch + '/download.jpg')
    image = customtkinter.CTkImage(light_image=Image.open(file_Patch + '/download.jpg'), size=(350, 200))
    image_label = customtkinter.CTkLabel(my_window, image=image, text=' ')
    image_label.place(x=5, y=110)
    text1.configure(state='normal')
    text1.delete('1.0', tk.END)
    text1.insert('1.0', 'Описание видео : ' + link.title)
    text1.configure(state='disabled')
    my_window.minsize(width=window_width, height=320)
    my_window.maxsize(width=window_width, height=320)


def download_video(link):
    link_yt = YouTube(link)
    btn_02['text'] = f'Идет загрузка {link_yt.title}'
    stream = link_yt.streams.get_highest_resolution()
    stream.download(file_Patch)
    messagebox.showinfo('Информация', f'Файл : <{link_yt.title}> загружен')
    my_window.minsize(width=window_width, height=window_height)
    my_window.maxsize(width=window_width, height=window_height)
    btn_02.configure(state='disabled')


def link_check():
    my_check()
    try:
        link = entry_01.get()
        my_fun(YouTube(link))
        btn_02.configure(state='normal')
        progressbar.set(0)
    except:
        messagebox.showinfo('Информация', 'Неверная ссылка')


def download_playlist(link):
    my_playlist = Playlist(link)
    for video in my_playlist.videos:
        my_fun(video)
        my_window.update()
        video.streams.get_highest_resolution().download(file_Patch)
    messagebox.showinfo('Информация', f'Плейлист : <{my_playlist.title}> загружен')
    my_window.minsize(width=window_width, height=window_height)
    my_window.maxsize(width=window_width, height=window_height)
    btn_02.configure(state='disabled')


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


def my_check():
    my_window.minsize(width=window_width, height=window_height)
    my_window.maxsize(width=window_width, height=window_height)
    btn_02.configure(state='disabled')


my_window = ctk.CTk()
my_window.title('Загрузка видео с YouTube')
window_width = 1000
window_height = 110

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

my_lbl_01 = ctk.CTkLabel(my_window, text='Введите ссылку на видео : ')
my_lbl_01.place(x=5, y=10)
my_lbl_02 = ctk.CTkLabel(my_window, text='Куда будет сохранено видео : ')
my_lbl_02.place(x=5, y=40)
entry_01 = ctk.CTkEntry(my_window, width=690)
entry_01.place(x=180, y=10)
btn_01 = ctk.CTkButton(my_window, text='Проверить', width=100, height=20, command=link_check)
btn_01.place(x=875, y=14)
btn_01['bg'] = 'green'
entry_02 = ctk.CTkEntry(my_window, width=790)
entry_02.insert(0, file_Patch)
entry_02.place(x=190, y=40)
my_lbl_03 = ctk.CTkLabel(my_window, text='Загружать : ')
my_lbl_03.place(x=5, y=75)
combo = ctk.CTkComboBox(my_window, state='readonly', width=150, values=['одно видео', 'весь плейлист'])
combo.set('одно видео')
combo.place(x=80, y=75)
btn_02 = ctk.CTkButton(my_window, text='Скачать', width=580, height=20, command=download)
btn_02.place(x=320, y=80)
btn_02['bg'] = 'blue'
btn_02.configure(state='disabled')
my_lbl_05 = ctk.CTkLabel(my_window, text='Процесс загрузки видео : ')
my_lbl_05.place(x=550, y=200)

progressbar = ctk.CTkProgressBar(my_window, orientation="horizontal", width=500)
progressbar.place(x=400, y=230)
progressbar.set(0)
my_lbl_05.configure(text='Процесс загрузки видео : ' + '0%')

image = None
image_label = customtkinter.CTkLabel(my_window, image=image, text=' ')
image_label.place(x=5, y=180)

text1 = tk.Text(my_window, height=5, width=70, wrap="word", bd=0)
text1.place(x=380, y=120)
text1.configure(state='disabled')
text1['background'] = my_window['background']
text1['foreground'] = 'white'

# for i in range(100):
#    progressbar.set(i/100)

# progressbar.set(1)
# progressbar.set(0.1)

# print(progressbar.get())
my_window.mainloop()

'''
https://www.youtube.com/watch?v=DwfHU166bfw
'''
