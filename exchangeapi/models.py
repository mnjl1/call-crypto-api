from turtle import mode
from django.db import models

# Create your models here.

class Currency(models.Model):
    pair = models.CharField(blank=True, max_length=20)
    binance_price = models.FloatField()
    kraken_price = models.FloatField()

    def __str__(self):
        return f'{self.pair}, {self.binance_price}, {self.kraken_price}'