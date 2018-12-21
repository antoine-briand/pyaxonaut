import json
import os
import unittest

from pyaxonaut.models.quote_line import QuoteLine


class TestQuoteLineModel(unittest.TestCase):

    def setUp(self):
        with open(f"{os.path.dirname(os.path.realpath(__file__))}/fixtures/quote_line.json",
                  mode="r") as json_quote_line_fixture:
            self.quote_line_fixture = json.load(json_quote_line_fixture)

    def test_get_customer_from_json(self):
        quote_line = QuoteLine(self.quote_line_fixture)
        self.assertEqual(123456, quote_line.product_id)
        self.assertEqual(None, quote_line.product_internal_id)
        self.assertEqual("ACME Product", quote_line.product_name)
        self.assertEqual(None, quote_line.product_code)
        self.assertEqual("ACME Product", quote_line.title)
        self.assertEqual("<h1></h1>", quote_line.details)
        self.assertEqual("1.00000", quote_line.quantity)
        self.assertEqual("1200.00000", quote_line.unit_price)
        self.assertEqual("20.00", quote_line.tax_rate)
        self.assertEqual("0.00", quote_line.line_discount_amount)
        self.assertEqual("0.00", quote_line.line_discount_amount_with_tax)
        self.assertEqual(True, quote_line.line_discount_unit_is_percent)
        self.assertEqual(240, quote_line.tax_amount)
        self.assertEqual(1200, quote_line.pretax_amount)
        self.assertEqual(1440, quote_line.total_amount)
