import requests
import json

class TestGeocode():
    local_server = "http://127.0.0.1:8000"
    local_path = "/geocode?address="
    postmates = "201%203rd%20Street%20San%20Francisco,%20CA%2094103"
    ycombinator = "320%20Pioneer%20Way%20Mountain%20View,%20CA%2094041"
    failure = "nil"
    test_postmates = f'{local_server}{local_path}{postmates}'
    test_ycombinator = f'{local_server}{local_path}{ycombinator}'
    test_failure = f'{local_server}/{failure}'

    def get_response(self, test_url):
        response = requests.get(test_url)
        return response

    def test_postmates_response(self):
        test = self.get_response(self.test_postmates)
        assert test.status_code == 200
        json_data = json.loads(test.text)
        assert json_data == {"lat": 37.78473, "lng": -122.40015, "service": "here", "status": 20001}

    def test_ycombinator_response(self):
        test = self.get_response(self.test_ycombinator)
        assert test.status_code == 200
        json_data = json.loads(test.text)
        assert json_data == {"lat": 37.38677, "lng": -122.06749, "service": "here", "status": 20001}

    def test_failure_response(self):
        assert self.get_response(self.test_failure).status_code == 404
