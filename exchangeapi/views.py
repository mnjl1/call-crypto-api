from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import utils
from .url_constants import exchange_dict


@api_view(['GET'])
def display_all_prices(request):
    prices = utils.get_all_prices()
    return Response(prices)


@api_view(['GET'])
def display_specific_exchange_prices(request, exchange):
    try:
        prices = utils.get_specific_echange_api(exchange_dict[exchange])
        return Response(prices)
    except: 
        return Response('Exchange does not exist')


@api_view(['GET'])
def display_exchange_price_pair(request, exchange, pair):
    try:
        price = utils.find_pair(pair, exchange_dict[exchange])
        return Response(price)
    except:
        return Response('Pair does not exist')

