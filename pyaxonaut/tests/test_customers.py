import unittest
from unittest.mock import Mock, patch

from customers import Customers


class TestCustomers(unittest.TestCase):

    def setUp(self):
        self._customers = Customers()

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

    @patch('customers.requests.post')
    def test_get_customers(self, mock_post):
        data = {
            "arrayCompanies": [
                {'companyId': 1234}
            ]
        }
        mock_resp = self._mock_response(json_data=data)
        mock_post.return_value = mock_resp

        response = self._customers.get_customers()
        self.assertTrue(len(response) > 0)
        self.assertEqual(1234, response[0].company_id)


if __name__ == '__main__':
    unittest.main()
