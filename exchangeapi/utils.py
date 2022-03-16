from gettext import find
import requests

binance_url = 'https://www.binance.com/bapi/asset/v1/public/asset-service/product/currency'
kraken_url = ''


def get_exchange_data(pair, exchange):
    if pair is None and exchange is None:
        pass
    elif pair is None:
        prices = call_echange_api(exchange)
        return prices.json()
    else:
        pair_price = find_pair(pair, prices)
        return pair_price

def get_all_prices():
    binance_data = call_echange_api(binance_url)
    prices = []
    for price in binance_data.json()['data']:
        prices.append({price['pair']: price['rate']})
    return prices


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
