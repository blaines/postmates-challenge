import requests
import json

class TestGeocode():
    local_server = "http://127.0.0.1:8000"
    local_path = "/geocode?address="
    postmates = "201%203rd%20Street%20San%20Francisco,%20CA%2094103"
    ycombinator = "320%20Pioneer%20Way%20Mountain%20View,%20CA%2094041"
    missing = "nil"
    test_postmates = f'{local_server}{local_path}{postmates}'
    test_ycombinator = f'{local_server}{local_path}{ycombinator}'
    test_here = f'{local_server}{local_path}0'
    test_failure = f'{local_server}{local_path}😄'
    test_missing = f'{local_server}/{missing}'

    def get_response(self, test_url):
        response = requests.get(test_url)
        return response

    def test_postmates_response(self):
        test = self.get_response(self.test_postmates)
        assert test.status_code == 200
        json_data = json.loads(test.text)
        assert json_data == {"lat": 37.7850747, "lng": -122.399873392674, "service": "osm", "status": 20011}

    def test_ycombinator_response(self):
        test = self.get_response(self.test_ycombinator)
        assert test.status_code == 200
        json_data = json.loads(test.text)
        assert json_data == {"lat": 37.38669505, "lng": -122.067898345833, "service": "osm", "status": 20011}

    def test_here_response(self):
        test = self.get_response(self.test_here)
        assert test.status_code == 200
        json_data = json.loads(test.text)
        assert json_data == {"lat": 27.96408, "lng": -110.78683, "service": "here", "status": 20001}

    def test_failure_response(self):
        test = self.get_response(self.test_failure)
        assert test.status_code == 500
        json_data = json.loads(test.text)
        assert json_data == {"error": "IndexError", "service": "here", "status": 50002}

    def test_missing_response(self):
        assert self.get_response(self.test_missing).status_code == 404
