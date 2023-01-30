import requests
from tkinter import messagebox, Tk, Canvas, Frame, Entry, Button
from tkinter import *


def translator():
    api_url = 'https://developers.lingvolive.com/api/v1/Minicard'

    get_a_new_bearer_token = requests.post('https://developers.lingvolive.com/api/v1.1/authenticate',
                                           headers={'Authorization': 'Basic YTAxMmQ4ZDMtMWFmMS00NzAxLW'
                                                                     'E2NTUtNGJjNTg5ZTdhODRmOmY4YmJhM2Z'
                                                                     'jYzY4MTQzMWRiZGU0MmJhYTNhYWEyNmE4'})

    param = {
        'text': wordInput.get(),
        'srcLang': 1049,
        'dstLang': 1033,
    }

    header = {
        'Authorization': 'Bearer ' + get_a_new_bearer_token.text
    }

    res = requests.get(api_url, params=param, headers=header)
    info['text'] = res.json()['Translation']['Translation']


root = Tk()

root['bg'] = 'white'
root.title('Translator')
root.wm_attributes('-alpha', 0.9)
root.geometry('300x250')
root.resizable(width=False, height=False)


frame_top = Frame(root, bg='orange')
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='orange')
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

wordInput = Entry(frame_top, bg='white')
wordInput.pack()

btn = Button(frame_top, text='Перевод', bg='white', command=translator)
btn.pack()

info = Label(frame_bottom, text='Перевод')
info.pack()

root.mainloop()
