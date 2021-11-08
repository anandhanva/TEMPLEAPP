from os import environ
from maass import app

if __name__ == '__main__':
    HOST = '127.0.0.1'
    try:
        PORT = int(environ.get('SERVER_PORT','8003'))

    except ValueError:
        PORT = 8000
app.run(HOST,PORT, debug=True)


