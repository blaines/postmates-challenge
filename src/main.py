import json
import urllib.request
import os
import app.server

if __name__ == '__main__':
    server = app.server.Server()
    server.start()