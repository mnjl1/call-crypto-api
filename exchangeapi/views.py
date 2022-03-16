from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Currency
from .serializers import CurrencySerializer
from . import utils
from exchangeapi import serializers


@api_view(['GET'])
def get_all_prices(request):
    prices = utils.get_all_prices()
    return Response(prices)


