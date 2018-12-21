import requests

import pyaxonaut.constants as constants
from pyaxonaut.models.quote import Quote


class Quotes:
    QUOTES_URL = f"{constants.AXONAUT_API_BASE_URL}/{constants.AXONAUT_API_QUOTE_LIST}"

    def __init__(self, api_key=None):
        self.api_key = api_key

    def get_quotes(self):
        return list(map(Quote, self.request_quotes_json()))

    def request_quotes_json(self):
        resp = requests.post(self.QUOTES_URL, data={
            "accountApiKey": self.api_key
        })
        return resp.json().get('quotations')
