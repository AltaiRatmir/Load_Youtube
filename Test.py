import tkinter as tk


def my_fun():
    text1.configure(state='normal')
    text1.delete('1.0', tk.END)
    text1.insert('1.0', text2.get('1.0', tk.END))
    text1.configure(state='disabled')


my_window = tk.Tk()
my_window.title('Загрузка видео с YouTube')
window_width = 1000
window_height = 500
my_window.minsize(width=window_width, height=window_height)
my_window.maxsize(width=window_width, height=window_height)

text1 = tk.Text(my_window, height=10, width=100, wrap="word", bd=0)
text1.place(x=5, y=5)
text1.configure(state='disabled')
text1['background'] = my_window['background']

text2 = tk.Text(my_window, height=10, width=100, wrap="word")
text2.place(x=5, y=200)

btn_01 = tk.Button(my_window, text='Вставить', width=50, command=my_fun)
btn_01.place(x=25, y=390)

# my_window.wm_attributes("-topmost", True)
# my_window.wm_attributes("-disabled", True)
# my_window.wm_attributes("-transparentcolor", "white")

my_window.mainloop()
