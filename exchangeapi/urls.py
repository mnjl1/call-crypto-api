from django.urls import path
from . import views

app_name = 'exchangeapi'

urlpatterns = [
    path('all-prices', views.get_all_prices, name='all-prices'),
]