from models.quote_line import QuoteLine


class Quote:
    quote_id = None
    number = ""
    title = ""
    date = ""
    send_date = ""
    company_id = None
    company_name = ""
    agent_id = None
    global_discount_amount = None
    global_discount_amount_with_tax = None
    global_discount_unit_is_percent = None
    global_discount_comments = None
    pre_tax_amount = None
    tax_amount = None
    total_amount = None
    customer_answer = 0
    electronic_signature_date = ""
    quotation_lines = []

    def __init__(self, quote_json):
        self.quote_id = quote_json.get('id')
        self.number = quote_json.get('number')
        self.title = quote_json.get('title')
        self.date = quote_json.get('date')
        self.send_date = quote_json.get('sentDate')
        self.agent_id = quote_json.get('idUser')
        self.company_id = quote_json.get('companyId')
        self.company_name = quote_json.get('companyName')
        self.global_discount_amount = quote_json.get('globalDiscountAmount')
        self.global_discount_amount_with_tax = quote_json.get('globalDiscountAmountWithTax')
        self.global_discount_unit_is_percent = quote_json.get('globalDiscountUnitIsPercent')
        self.global_discount_comments = quote_json.get('globalDiscountComments')
        self.pre_tax_amount = quote_json.get('preTaxAmount')
        self.tax_amount = quote_json.get('taxAmount')
        self.total_amount = quote_json.get('totalAmount')
        self.customer_answer = quote_json.get('customerAnswer')
        self.electronic_signature_date = quote_json.get('electronicSignatureDate')
        self.quotation_lines = list(map(QuoteLine, quote_json.get('quotationLines')))
