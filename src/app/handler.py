from app.geocoders.here import HereGeocoder
from http.server import BaseHTTPRequestHandler
import urllib, json

# For responses, it's important to call response methods in the correct order
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if(self.path[:9] == "/geocode?"):
            query = urllib.parse.parse_qs(self.path[9:])
            geocoder = HereGeocoder()
            latlng = geocoder.geocode(query["address"][0])
            # 1. Response Code
            self.send_response(200)
            # 2. Headers
            self.send_header("Content-Type", "text/json")
            self.end_headers()
            # 3. Body
            self.wfile.write(json.dumps(latlng).encode('utf-8'))
        else:
            # 1. Response Code
            self.send_response(404)
            # 2. Headers
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            # 3. Body
            self.wfile.write(b"<!DOCTYPE html><html><body>not found</body></html>")
        return
