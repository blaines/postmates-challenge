from app.handler import Handler
from http.server import HTTPServer

def start():
    httpd = HTTPServer(("127.0.0.1", 8000), Handler)
    httpd.serve_forever()