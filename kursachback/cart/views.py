from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from db.models import Tour, Route
from .forms import CartAddTourForm
from cart.cart import Cart
from db.models import  Putevka, Hotelroom, Contract, Groupp
from .forms import OrderCreateForm
from django.db.models import Max
from db.math import get_id_hotel_room
import datetime


@require_POST
def cart_add(request, id_tour):
    cart = Cart(request)
    tour = get_object_or_404(Tour, id_tour=id_tour)
    route = get_object_or_404(Route, name_toure=id_tour)
    form = CartAddTourForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(tour=tour,
                 hotelroom=cd['hotelroom'],
                 typeofpayment=cd['typeofpayment'],
                 route=route,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, id_tour):
    cart = Cart(request)
    tour = get_object_or_404(Tour, id_tour=id_tour)
    cart.remove(tour)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                contract = Contract.objects.all().aggregate(Max('field_contract'))
                id_contract = 0
                if contract['field_contract__max'] is not None:
                    id_contract = contract['field_contract__max']
                id_contract = id_contract + 1
                date_today = datetime.datetime.today()
                date = date_today.date()
                Contract.objects.create(field_contract=id_contract,
                                        dateofconclusion=date,
                                        typeofpayment=item['typeofpayment'],)
                id_hotel_room = Hotelroom.objects.filter(idhotelroom=str(item['hotelroom']))
                id_room = get_id_hotel_room(id_hotel_room)
                id_group = Groupp.objects.filter(field_route__name_toure__id_tour=item['tour'].id_tour)
                field_putevka = Putevka.objects.all().aggregate(Max('field_pytevki'))
                id_putevka = 0
                if field_putevka['field_pytevki__max'] is not None:
                    id_putevka = field_putevka['field_pytevki__max']
                id_putevka = id_putevka + 1
                for group in id_group:
                   Putevka.objects.create(field_pytevki=id_putevka,
                                           name_toure=item['tour'].id_tour,
                                           cost=item['price'],
                                           idhotelroom=id_room,
                                           email=request.POST['email'],
                                           field_contract=id_contract,
                                           field_groupp=group.field_groupp,
                                           )
            # очистка корзины
            cart.clear()
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})