from django.contrib import admin
from .models import Shop, Goods, Basket
admin.site.register(Basket)
admin.site.register(Shop)
admin.site.register(Goods)
# Register your models here.
