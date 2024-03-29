import requests
from urllib.parse import urljoin
from api.data import payload_segment, payload_campaign
from api.exceptions import *

class ApiClient:

    def __init__(self):
        self.base_url = 'https://target.my.com'
        self.session = requests.Session()

    def _request(self, method, location, expected_status = 200, headers = None, params = None,
                 data = None, json = None, jsonify = True, fullpath = False):
        if not fullpath:
            url = urljoin(self.base_url, location)
        else:
            url = location
        response = self.session.request(method, url, headers=headers, params=params, data=data, json=json)
        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.reason} for URL "{url}"')
        if jsonify:
            return response.json()
        return response

    @property
    def csrf_token(self):
        token = self.session.cookies.get('csrftoken')
        if token is None:
            raise CSRFTokenNotSetException('No CSRF Token set for this client')
        return token

    def get_csrf_token(self):
        self._request('GET', 'csrf/', jsonify=False)
        return self.session.cookies.get('csrftoken')

    def post_login(self, email, password):
        location = 'https://auth-ac.my.com/auth'
       
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': self.base_url
        }
        data = {
            'email': email,
            'password': password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1',
            'failure': 'https://account.my.com/login/'
        }
        self._request('POST', location, expected_status=200, headers=headers, data=data, jsonify=False, fullpath=True)
        return self.get_csrf_token()

    def create_segment(self, name):
        location = 'api/v2/remarketing/segments.json'
        payload = payload_segment(name)
        headers = {'Content-Type': 'application/json',
                   'X-CSRFToken': self.csrf_token}
        response = self._request('POST', location, headers=headers, json=payload)
        return response['id']
    
    def delete_segment(self, name):
        location = f'api/v2/remarketing/segments/{name}.json'
        headers = {'Content-Type': 'application/json',
                   'X-CSRFToken': self.csrf_token}
        self._request('DELETE', location, expected_status = 204, headers=headers, jsonify = False)

    def create_campaign(self, name_company):

        location = '/api/v2/campaigns.json'

        payload = payload_campaign(name_company)
        headers = {'Content-Type': 'application/json', 'X-CSRFToken': self.csrf_token}
        response = self._request('POST', location, headers=headers, json=payload)
        return response['id']

    def delete_campaign(self, name):
        location = f'/api/v2/campaigns/{name}.json'
        headers = {'Content-Type': 'application/json',
                   'X-CSRFToken': self.csrf_token}
        self._request('DELETE', location, expected_status = 204, headers=headers, jsonify = False)

    def get_all_segments(self, id):
    
        location = "api/v2/remarketing/segments.json?fields=id&limit=100&"
        segments_json = self._request('GET', location)
        for i in segments_json['items']:
            if i['id'] == id:
                return 0
        return 1

    def get_all_campaign(self, id):

        location = 'api/v2/campaigns.json?fields=id&sorting=-id&limit=100&'
        campaign_json = self._request('GET', location)
        for i in campaign_json['items']:
            if i['id'] == id:
                return 0
        return 1
        


