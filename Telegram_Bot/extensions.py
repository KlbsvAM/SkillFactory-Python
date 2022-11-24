import requests
import json
from Config_ValuesMoneyBot import keys_ValuesMoneyBot


class APIException(Exception):
    pass
class CryptoConverter:
    @staticmethod
    def get_price(quote: str,base:str,amount:str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')
        try:
            quote_r = keys_ValuesMoneyBot[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту{quote}')
        try:
            base_r = keys_ValuesMoneyBot[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту{base}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_r}&tsyms={base_r}')
        total_base = json.loads(r.content)[keys_ValuesMoneyBot[base]]
        return total_base