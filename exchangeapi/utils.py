from gettext import find
import requests

binance_url = 'https://www.binance.com/bapi/asset/v1/public/asset-service/product/currency'
kraken_url = ''


def get_price(pair, exchange):
    prices = call_echange_api(exchange)
    pair_price = find_pair(pair, prices)
    return pair_price


def call_echange_api(url):
    try:
        response = requests.get(url)
        if response.ok:
            return response
    except requests.exceptions.RequestException as e:
        print(e)
        return {}


def find_pair(pair, response):
    data = response.json()['data']
    for t_pair in data:
        if pair == t_pair['pair']:
            return (pair, t_pair['rate'])


print(get_price('VES_USD', binance_url))