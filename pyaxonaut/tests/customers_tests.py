import unittest

from config import PyAxonautConfig
from customers import Customers


class TestCustomer(unittest.TestCase):

    def setUp(self):
        config = PyAxonautConfig()
        self.api_key = config.get_api_key()

    def test_dummy(self):
        customers = Customers(self.api_key)
        self.assertTrue(len(customers.get_customers()) > 0)


