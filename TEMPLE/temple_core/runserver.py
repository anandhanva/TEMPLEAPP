from os import environ
from b_core import app

if __name__ == '__main__':
    HOST = '0.0.0.0' #192.168.0.118 

    try:
        PORT = int(environ.get('SERVER_PORT','8002'))

    except ValueError:
        PORT = 8000
app.run(HOST,PORT, debug=True)

