import json
import os
import unittest

from models.quote import Quote


class TestQuoteModel(unittest.TestCase):

    def setUp(self):
        with open(f"{os.path.dirname(os.path.realpath(__file__))}/fixtures/quote.json",
                  mode="r") as json_quote_fixture:
            self.quote_fixture = json.load(json_quote_fixture)

    def test_get_customer_from_json(self):
        quote_line = Quote(self.quote_fixture)
        self.assertEqual(12345, quote_line.quote_id)
        self.assertEqual("123456789", quote_line.number)
        self.assertEqual("123456789 Devis ACME", quote_line.title)
        self.assertEqual("2018-09-27", quote_line.date)
        self.assertEqual(None, quote_line.send_date)
        self.assertEqual(1234, quote_line.agent_id)
        self.assertEqual(123456, quote_line.company_id)
        self.assertEqual("ACME", quote_line.company_name)
        self.assertEqual(None, quote_line.global_discount_amount)
        self.assertEqual(None, quote_line.global_discount_amount_with_tax)
        self.assertEqual(None, quote_line.global_discount_unit_is_percent)
        self.assertEqual(None, quote_line.global_discount_comments)
        self.assertEqual(1200, quote_line.pre_tax_amount)
        self.assertEqual(240, quote_line.tax_amount)
        self.assertEqual(1440, quote_line.total_amount)
        self.assertEqual(1, quote_line.customer_answer)
        self.assertEqual(None, quote_line.electronic_signature_date)
        self.assertEqual(1, len(quote_line.quotation_lines))
        self.assertEqual(123456, quote_line.quotation_lines[0].product_id)

