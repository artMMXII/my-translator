import requests

api_url = 'https://developers.lingvolive.com/api/v1/Minicard'

param = {
    'text': input(),
    'srcLang': 1049,
    'dstLang': 1033,
}

header = {
    'Authorization': ('Bearer ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmxlSEFpT2pFMk56VXhOVFU0T1RNc0lrMXZaR'
                      '1ZzSWpwN0lrTm9ZWEpoWTNSbGNuTlFaWEpFWVhraU9qVXdNREF3TENKVmMyVnlTV1FpT2pjME5qSXNJbFZ1YVhGMVpVbGtJa'
                      'm9pWVRBeE1tUTRaRE10TVdGbU1TMDBOekF4TFdFMk5UVXROR0pqTlRnNVpUZGhPRFJtSW4xOS5mSUxYdVB3YjhCblRRZTR2'
                      'MlhXdW5aZUdjbUI1UmdYT3JnUVhZNE1ZYnk4')
}

res = requests.get(api_url, params=param, headers=header)

print(res.json()['Translation']['Translation'])
