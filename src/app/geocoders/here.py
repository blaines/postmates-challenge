import json
import urllib
import logging
import app.config

class HereGeocoder:
    def __init__(self):
        self.service_url = f"https://geocoder.api.here.com/6.2/geocode.json?app_id={app.config.HERE_APP_ID}&app_code={app.config.HERE_APP_CODE}&"
    def geocode(self, address = "default"):
        params = {"searchtext": address}
        query = urllib.parse.urlencode(params)
        req = urllib.request.Request(self.service_url + query)
        try:
            response = urllib.request.urlopen(req)
        except urllib.error.HTTPError:
            # Probably unauthorized
            return {"status": 50004, "service": "here"}
        if response.status == 200:
            logging.info(f"HERE Geocoder Response {response.status}")
            json_data = json.loads(response.read().decode('utf-8'))
            try:
                latlng = json_data["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]
                return {"status": 20001, "service": "here", "lat": latlng["Latitude"], "lng": latlng["Longitude"]}
            except KeyError:
                # Most likely in this case an API error was returned
                logging.warn(f"HERE Geocoder Response Body Missing Data")
                return {"status": 50001, "service": "here", "error": "KeyError"}
            except IndexError:
                # Most likely in this case there was no result
                logging.warn(f"HERE Geocoder Response Body Missing Data")
                return {"status": 50002, "service": "here", "error": "IndexError"}
        else:
            # The server returned non-successfully
            logging.warn(f"HERE Geocoder Response {response.status}")
            return {"status": 50003, "service": "here"}
        
