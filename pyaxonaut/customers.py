import requests

from constants import AXONAUT_API_CUSTOMERS_LIST, AXONAUT_API_BASE_URL
from models import customer as customer_model

CUSTOMERS_URL = f"{AXONAUT_API_BASE_URL}/{AXONAUT_API_CUSTOMERS_LIST}"


class Customers:

    def __init__(self, api_key):
        self.api_key = api_key

    def get_customers(self):
        customers = []
        resp = requests.post(CUSTOMERS_URL, data={
            "accountApiKey": self.api_key
        })

        print(resp.__dict__)

        for axonaut_customer in resp.json().get('arrayCompanies'):
            customer = customer_model.Customer
            customer.company_id = axonaut_customer.get('companyId')
            customers.append(customer)
        return customers
