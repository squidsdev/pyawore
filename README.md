# pyawore | Библиотека для приема платежей Awore 
Эта библеотека позволит вам с легкостью производить транзакции и принимать платежи Awore.
## Установка
```bash
pip install git+https://github.com/squidsdev/pyawore
```
## Использование
### Получение баланса токенов

```python
from pyawore import *

awore_token = "ВАШ ТОКЕН"  # https://awore.ru/settings
awore = Pyawore(awore_token)

print(awore.get_all_balance())
```
### Отправка средств с токенов

```python
from pyawore import *

awore_token = "ВАШ ТОКЕН"  # https://awore.ru/settings
awore = Pyawore(awore_token)

awore.send_transaction(token="BTC", address_to="0x563baA79711AEb43e8f35917c427A54cA66Bb2cB", amount=10,
    includeFee=False)
```
### Создание счета

```python
from pyawore import *

awore_token = "ВАШ ТОКЕН"  # https://awore.ru/settings
awore = Pyawore(awore_token)

payment = awore.create_invoice(amount=100, comment='Покупка котенка', return_url='https://awore.ru',
    callback_url='https://awore.ru/id?=4234235', token_code='BTC', currency_code='USD')
print(payment["url"])
```
### Получение инфорации о счете

```python
from pyawore import *

awore_token = "ВАШ ТОКЕН"  # https://awore.ru/settings
awore = Pyawore(awore_token)

print(awore.invoice_info(id=143564))
```
### Получение всех счетов

```python
from pyawore import *

awore_token = "ВАШ ТОКЕН"  # https://awore.ru/settings
awore = Pyawore(awore_token)

print(awore.invoice_all())
```
