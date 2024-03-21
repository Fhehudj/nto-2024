import requests

url = 'http://192.168.12.12:5000/api'


session = requests.Session()


def get_pin():
    return session.get(url + '/EncryptedPin').json()


def encrypt_pin(pin):
    return session.post(url + '/EncryptPin', json={'pin': pin}).json()


def get_time():
    return session.get(url + '/Time').json()


def check_pin(pin):
    return session.post(url + '/CheckPin', json={'pin': pin}).content


for i in range(10000):
    res = check_pin(i)
    if not res.startswith(b'<!doctype html>\n<html lang=en>\n<title>500 Inte'):
        print(res)
    else:
        if i % 1000 == 0:
            print(i)
