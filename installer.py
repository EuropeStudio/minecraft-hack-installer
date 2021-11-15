from tkinter import *
import wget
from requests import get
import getpass

x, y = 42 , 401


def download():
    url = 'https://pastebin.com/raw/uXh1cDZa'
    response = get(url)
    wget.download(response.text[:500], "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/mods/ZeroTwo_0.0.7.jar")

tk = Tk()

tk.geometry("500x500")
tk.title("zerotwo")


install_button = PhotoImage(file=r'hi.png')
background_image = PhotoImage(file=r'kykymber.png')

background_label = Label(tk, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

button = Button(tk, image=install_button, command=download)
button.place(x=x, y=y)


tk.resizable(width=False, height=False)

tk.mainloop()
