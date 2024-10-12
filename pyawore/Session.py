from __future__ import annotations
import json
from requests import post
from pyawore import AuthError, SendTransactionError, CreateInvoiceError


class Pyawore(object):
    def __init__(self, key: str) -> None:
        self.token = key
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        self.url = "https://awore.ru/api/v2"

        self.check_key()

    def check_key(self) -> bool:
        response = post(self.url + "/token/getAllBalance", headers=self.headers, data=json.dumps({"tokenApi": self.token})).json()
        if response.get('statusCode') != 200:
            raise AuthError("Неверный ключ API (Invalid API key)")
        return True

    def get_all_balance(self) -> dict:
        response = post(self.url + "/token/getAllBalance", headers=self.headers, data=json.dumps({"tokenApi": self.token}))
        return response.json()

    def send_transaction(self, token: str, address_to: str, amount: float, includeFee: bool = False) -> dict:
        data = {
            "tokenApi": self.token,
            "token": token,
            "address_to": address_to,
            "amount": amount,
            "includeFee": includeFee
        }
        response = post(self.url + "/token/sendTransaction", headers=self.headers, data=json.dumps(data)).json()

        if 'error' in response:
            raise SendTransactionError(response["message"])
        return response

    def create_invoice(self, amount: float, token_code: str, currency_code: str, comment: str = '', return_url: str = None, callback_url: str = None) -> dict:
        data = {
            "tokenApi": self.token,
            "amount": amount,
            "comment": comment,
            "returnUrl": return_url,
            "callbackUrl": callback_url,
            "tokenCode": token_code,
            "currencyCode": currency_code
        }
        response = post(self.url + "/invoice/create", headers=self.headers, data=json.dumps(data)).json()

        if 'error' in response:
            raise CreateInvoiceError(response["message"])
        return response

    def invoice_info(self, id: int) -> dict:
        data = {
            "tokenApi": self.token,
            "id": id,
        }
        response = post(self.url + "/invoice/info", headers=self.headers, data=json.dumps(data))
        return response.json()

    def invoice_all(self) -> dict:
        data = {
            "tokenApi": self.token
        }
        response = post(self.url + "/invoice/all", headers=self.headers, data=json.dumps(data))
        return response.json()
