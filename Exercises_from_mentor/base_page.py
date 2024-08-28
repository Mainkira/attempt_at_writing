import requests

class MockApi:
    url = 'https://66742d1675872d0e0a95683e.mockapi.io/api/v1/'


    def get(self, endpoint):
        response = requests.get(self.url + endpoint)
        return response.json()

    def post(self, endpoint, data):
        response = requests.post(self.url + endpoint, json=data)
        return response.json()

    def put(self, endpoint, data):
        response = requests.put(self.url + endpoint, json=data)
        return response.json()

    def delete(self, endpoint):
        response = requests.delete(self.url + endpoint)
        return response