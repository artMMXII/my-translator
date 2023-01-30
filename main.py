import requests
from tkinter import messagebox, Tk, Canvas, Frame, Entry, Button


def translator():
    api_url = 'https://developers.lingvolive.com/api/v1/Minicard'

    get_a_new_bearer_token = requests.post('https://developers.lingvolive.com/api/v1.1/authenticate',
                                           headers={'Authorization': 'Basic YTAxMmQ4ZDMtMWFmMS00NzAxLW'
                                                                     'E2NTUtNGJjNTg5ZTdhODRmOmY4YmJhM2Z'
                                                                     'jYzY4MTQzMWRiZGU0MmJhYTNhYWEyNmE4'})

    param = {
        'text': 'кот',
        'srcLang': 1049,
        'dstLang': 1033,
    }

    header = {
        'Authorization': 'Bearer ' + get_a_new_bearer_token.text
    }

    res = requests.get(api_url, params=param, headers=header)

    print(res.json()['Translation']['Translation'])

    print()


translator()
