"""
This script runs the GolfCard application using a development server.
"""

from os import environ
from GolfCard.views import socketio, app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    print('start')
    print(PORT)
    print(HOST)
    socketio.run(app, port=PORT, host=HOST)
    print('end')