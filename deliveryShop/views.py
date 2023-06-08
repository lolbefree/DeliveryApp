import json
from django.http import JsonResponse
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Goods, Basket, BasketGoods
from .forms import BasketForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import LoginForm


def index(request, store=1):
    basket_items = []
    basket = None

    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        if hasattr(user, 'basket'):
            basket = user.basket
        else:
            basket = Basket.objects.create(user=user)
        basket_items = basket.basket_goods.all()

        basket_goods = basket.basket_goods.all()
        for bg in basket_goods:
            if bg.shop_id != store:
                basket.basket_goods.all().delete()

    shops = Shop.objects.all()
    goods = Goods.objects.filter(shop__pk=store)
    chunk_size = 3
    sliced_goods = [goods[i:i + chunk_size] for i in range(0, len(goods), chunk_size)]

    return render(request, 'DeliveryApp/index.html', {"shop_id": store, "shops": shops, "goods": sliced_goods, "basket_items": basket_items})

@login_required
def clear_basket(request):
    user = request.user
    basket = user.basket
    basket.basket_goods.all().delete()

    return redirect('main')


@login_required
def basket_view(request):
    basket = request.user.basket
    basket_items = basket.basket_goods.all()
    total_amount = 0

    for item in basket_items:
        total_amount += item.quantity * item.goods.price

    context = {
        'basket_items': basket_items,
        'total_amount': total_amount
    }
    return render(request, 'DeliveryApp/basket.html', context)



def add_to_basket(request, store=None):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = User.objects.get(username=request.user.username)
            if hasattr(user, 'basket'):
                basket = user.basket
            else:
                basket = Basket.objects.create(user=user)
            print('im post')
            payload = json.loads(request.body)
            good_id = payload.get('id')
            quantity = payload.get('quantity')
            shop_id = payload.get('shop_id')
            print('ahah', shop_id)
            basket = Basket.objects.get(user=request.user)
            basket_goods = basket.basket_goods.all()
            for bg in basket_goods:
                if bg.shop_id != shop_id:
                    basket.goods.clear()
            print(good_id, quantity)
            goods = Goods.objects.get(id=good_id)
            basket_goods, created = BasketGoods.objects.get_or_create(basket=basket, goods=goods, shop_id=shop_id)
            basket_goods.quantity += quantity
            basket_goods.save()
            return JsonResponse({'message': 'Item added to basket successfully'})
        else:
            return JsonResponse({'error': 'Invalid request method'})
    else:
        return JsonResponse({'message': 'not_authenticated'})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'DeliveryApp/register.html', {'form': form})


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'DeliveryApp/login.html'
