from django.urls import path
from . import views

app_name = 'exchangeapi'

urlpatterns = [
    path('all-prices/', views.display_all_prices),
    path('all-prices/<str:exchange>/', views.display_specific_exchange_prices),
    path('all-prices/<str:exchange>/<str:pair>/', views.display_exchange_price_pair),
]