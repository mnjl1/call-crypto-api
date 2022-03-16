
import requests

from .url_constants import BINANCE_URL, KRAKEN_URL


def get_all_prices():
    binance_data = call_binance_echange_api(BINANCE_URL)
    kraken_data = None
    prices = []
    for price in binance_data.json()['data']:
        prices.append({price['pair']:{ 'binance': price['rate']}})
    
    return prices


def get_specific_echange_api(exchange_url):
    try:
        response = requests.get(exchange_url)
        if response.ok:
            prices = []
            for price in response.json()['data']:
                prices.append({price['pair']: price['rate']})
            return prices
    except requests.exceptions.RequestException as e:
        print(e)
        return {}


def find_pair(pair, exchange):
    prices = get_specific_echange_api(exchange)
    for t_pair in prices:
        if pair in t_pair:
            return t_pair


def call_binance_echange_api(exchange_url):
    try:
        response = requests.get(exchange_url)
        if response.ok:
            return response
    except requests.exceptions.RequestException as e:
        print(e)
        return {}
