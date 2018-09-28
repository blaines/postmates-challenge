from http.server import BaseHTTPRequestHandler

# For responses, it's important to call response methods in the correct order
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Response Code
        self.send_response(200)
        # 2. Headers
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        # 3. Body
        self.wfile.write(b'<!DOCTYPE html><html><body>hello world</body></html>')
        return
