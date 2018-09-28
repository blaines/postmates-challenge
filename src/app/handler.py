from app.geocoders.here import HereGeocoder
from app.geocoders.openstreet import OSMGeocoder
import app.config
from http.server import BaseHTTPRequestHandler
import urllib, json, logging

GEOCODERS = [OSMGeocoder(), HereGeocoder()]

# For responses, it's important to call response methods in the correct order
class Handler(BaseHTTPRequestHandler):
    def query_geocoding_service(self, query, index = 0):
        service = GEOCODERS[index]
        response = service.geocode(query)
        if response["status"] > 50000:
            logging.warn(f"Service {service} failed")
            if index < len(GEOCODERS) - 1:
                index += 1
                response = self.query_geocoding_service(query, index)
            else:
                logging.warn("All geocoding services have failed")
        return response

    def do_GET(self):
        if(self.path[:9] == "/geocode?"):
            response_status = 200
            query = urllib.parse.parse_qs(self.path[9:])
            latlng = self.query_geocoding_service(query["address"][0])
            if latlng["status"] > 50000:
                response_status = 500
            # 1. Response Code
            self.send_response(response_status)
            # 2. Headers
            self.send_header("Content-Type", "application/json")
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
