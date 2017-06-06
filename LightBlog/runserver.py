"""
This script runs the LightBlog application using a development server.
"""

from os import environ
from LightBlog import create_app

app=create_app('development')

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)