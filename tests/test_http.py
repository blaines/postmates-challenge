import requests

class TestGeocode():
    local_server = "http://127.0.0.1:8000"
    local_path = "/geocode?address="
    postmates = "201%203rd%20Street%20San%20Francisco,%20CA%2094103"
    ycombinator = "320%20Pioneer%20Way%20Mountain%20View,%20CA%2094041"
    failure = "nil"
    test_postmates = f'{local_server}{local_path}{postmates}'
    test_ycombinator = f'{local_server}{local_path}{ycombinator}'
    test_failure = f'{local_server}{local_path}{failure}'

    def get_response(self, test_url):
        response = requests.get(test_url)
        return response

    def test_postmates_response(self):
        valid = self.get_response(self.test_postmates)
        assert valid.status_code == 200
        assert valid.text == '{"lng": 000.00000000, "lat": 000.00000000, "service": "google", "status": "20001"}'

    def test_ycombinator_response(self):
        valid = self.get_response(self.test_ycombinator)
        assert valid.status_code == 200
        assert valid.text == '{"lng": 000.00000000, "lat": 000.00000000, "service": "google", "status": "20001"}'

    def test_failure_response(self):
        assert self.get_response(self.test_failure).status_code != 200
