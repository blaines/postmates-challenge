import json
import urllib
import logging
import app.config

class OSMGeocoder:
    def __init__(self):
        self.service_url = "https://nominatim.openstreetmap.org/search/{0}?format=json&limit=1"
    def geocode(self, address = "default"):
        query = urllib.parse.quote(address)
        req = urllib.request.Request(self.service_url.format(query))
        response = urllib.request.urlopen(req)
        if response.status == 200:
            logging.info(f"OSM Geocoder Response {response.status}")
            json_data = json.loads(response.read().decode('utf-8'))
            try:
                latlng = json_data[0]
                return {"status": 20011, "service": "osm", "lat": float(latlng["lat"]), "lng": float(latlng["lon"])}
            except KeyError:
                # Most likely in this case an API error was returned
                logging.warn(f"OSM Geocoder Response Body Missing Data")
                return {"status": 50011, "service": "osm", "error": "KeyError"}
            except IndexError:
                # Most likely in this case there was no result
                logging.warn(f"OSM Geocoder Response Body Missing Data")
                return {"status": 50012, "service": "osm", "error": "IndexError"}
        else:
            # The server returned non-successfully
            logging.warn(f"OSM Geocoder Response {response.status}")
            return {"status": 50013, "service": "osm"}
        
