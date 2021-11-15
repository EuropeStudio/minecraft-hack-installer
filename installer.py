import tkinter as tk
from tkinter import *
import wget
from requests import get
import getpass

Hacks = [
"PyroClient",
"KonasClient"
] 

app = tk.Tk()

app.geometry('600x600')

variable = tk.StringVar(app)
variable.set(Hacks[0])

opt = tk.OptionMenu(app, variable, *Hacks)
opt.config(width=90, font=('Helvetica', 12))
opt.pack()

PyroClient = tk.Label(text="", font=('Helvetica', 12), fg='red')
PyroClient.pack(side="top")

def PyroClient():
    url = 'https://pastebin.com/raw/url'
    response = get(url)
    wget.download(response.text[:500], "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/mods/example")

KonasClient = tk.Label(text="", font=('Helvetica', 12), fg='red')
KonasClient.pack(side="top")

def KonasClient():
    url = 'https://pastebin.com/raw/url'
    response = get(url)
    wget.download(response.text[:500], "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/mods/example")

app.mainloop()