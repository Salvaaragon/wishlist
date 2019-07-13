from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(blank = True, null = True)
    price = models.FloatField()
    url = models.URLField(blank = True, null = True)
    shop = models.CharField(max_length = 100)
    priority = models.IntegerField(default = 1)


def __str__(self):
    return self.name