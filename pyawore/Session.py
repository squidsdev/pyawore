from __future__ import annotations
from pyawore import AuthError, SendTransactionError, CreateInvoiceError
from requests import get, post
import json

class pyawore(object):
	def __init__(self, key: str) -> LavaAPI:
		self.token = key
		self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		self.url = "https://awore.ru/api/v2"

		self.check_key()

	def check_key(self) -> bool:
		if post(self.url + "/token/getAllBalance", headers=self.headers, data=json.dumps({"tokenApi":self.token})).json().get('statusCode'):
			raise AuthError("Неверный ключ API (Invalid API key)")
		return True

	def get_all_balance(self) -> dict:
		return post(self.url + "/token/getAllBalance", headers=self.headers, data=json.dumps({"tokenApi":self.token})).json()

	def send_transaction(self, token: str, address_to: str, amount: float, includeFee: bool = False) -> dict:
		data = {
			"tokenApi": self.token,
			"token": token,
			"address_to": address_to,
			"amount": amount,
			"includeFee": includeFee
		}
		data = post(self.url + "/token/sendTransaction", headers=self.headers, data=json.dumps(data)).json()

		if data.get('error'):
			raise SendTransactionError(data["message"])

	def create_invoice(self, amount: float, currency_code: str, comment: str = '', return_url: str = None) -> dict:
		data = {
			"tokenApi": self.token,
			"amount": amount,
			"currencyCode": currency_code,
			"comment": comment,
			"return_url": return_url
		}
		data = post(self.url + "/invoice/create", headers=self.headers, data=json.dumps(data)).json()

		if data.get('error'):
			raise CreateInvoiceError(data["message"])
		return data

	def invoice_info(self, id: int) -> dict:
		data = {
			"tokenApi": self.token,
			"id": id,
		}
		return post(self.url + "/invoice/info", headers=self.headers, data=json.dumps(data)).json()

	def invoice_all(self) -> dict:
		data = {
			"tokenApi": self.token
		}
		return post(self.url + "/invoice/all", headers=self.headers, data=json.dumps(data)).json()
