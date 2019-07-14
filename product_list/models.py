from django.db import models

class ProductType(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(blank = True, null = True)
    price = models.FloatField()
    url = models.URLField(blank = True, null = True)
    shop = models.CharField(max_length = 100)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    priority = models.IntegerField(default = 1)

    def __str__(self):
        return self.name


class ProductList(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    description = models.TextField(blank = True, null = True)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
