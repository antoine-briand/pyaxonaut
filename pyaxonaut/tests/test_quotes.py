import json
import os
import unittest
from unittest.mock import Mock, patch

from pyaxonaut.quotes import Quotes


class TestQuotes(unittest.TestCase):

    def setUp(self):
        self._quotes = Quotes()
        with open(f"{os.path.dirname(os.path.realpath(__file__))}/fixtures/quotes.json",
                  mode="r") as json_quotes_fixture:
            self.json_quotes = json.load(json_quotes_fixture)

    def _mock_response(
            self,
            status=200,
            content="CONTENT",
            json_data=None,
            raise_for_status=None):
        mock_resp = Mock()
        # mock raise_for_status call w/optional error
        mock_resp.raise_for_status = Mock()
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status
        # set status code and content
        mock_resp.status_code = status
        mock_resp.content = content
        # add json data if provided
        if json_data:
            mock_resp.json = Mock(
                return_value=json_data
            )
        return mock_resp

    @patch('pyaxonaut.quotes.requests.post')
    def test_get_quotes(self, mock_post):
        mock_resp = self._mock_response(json_data=self.json_quotes)
        mock_post.return_value = mock_resp

        response = self._quotes.get_quotes()
        self.assertTrue(len(response) > 0)
        self.assertEqual(12345, response[0].quote_id)
