# customer/loader.py

import json


def load_customer():

    with open("customer/customer.json", "r", encoding="utf-8") as file:

        customer = json.load(file)

    return customer