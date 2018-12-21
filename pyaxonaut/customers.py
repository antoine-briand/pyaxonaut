import requests

from constants import AXONAUT_API_CUSTOMERS_LIST, AXONAUT_API_BASE_URL
from models.customer import Customer


class Customers:
    CUSTOMERS_URL = f"{AXONAUT_API_BASE_URL}/{AXONAUT_API_CUSTOMERS_LIST}"

    def __init__(self, api_key=None):
        self.api_key = api_key

    def request_customers_json(self):
        resp = requests.post(self.CUSTOMERS_URL, data={
            "accountApiKey": self.api_key
        })
        return resp.json().get('arrayCompanies')

    def get_customers(self):
        return list(map(Customer, self.request_customers_json()))
