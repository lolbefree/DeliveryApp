from django.db import models
from django.contrib.auth.models import User



class Shop(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=200)
    logo = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField()
    description = models.CharField(max_length=300)
    qty = models.IntegerField()
    price = models.FloatField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='goods')


    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goods = models.ManyToManyField(Goods, related_name='baskets')


class BasketGoods(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='basket_goods')
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ('basket', 'goods')

    def __str__(self):
        return f"{self.goods.name} ({self.quantity})"
