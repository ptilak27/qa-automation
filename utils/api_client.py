# utils/api_client.py
import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def create_user(self, user_payload):
        url = f"{self.base_url}/users/add"
        resp = requests.post(url, json=user_payload, timeout=15)
        return resp
