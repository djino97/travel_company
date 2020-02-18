from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import CartAddTourForm
from cart.cart import Cart
from db.models import Putevka, Hotelroom, Contract, Groupp, Klient
from .forms import OrderCreateForm
from .services import services
from django.db.models import Max
from db.calculation import get_id_hotel_room
import datetime


@require_POST
def cart_add(request, id_tour):
    cart = Cart(request)
    form = CartAddTourForm(request.POST)
    if form.is_valid():
        tour = services.get_tour(id_tour)
        route = services.get_route(id_tour)
        services.add_to_cart(form, cart, tour, route)
    return redirect('cart:cart_detail')


def cart_remove(request, id_tour):
    cart = Cart(request)
    tour = services.get_tour(id_tour)
    cart.remove(tour)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

