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
                klient_object = get_object_or_404(Klient, email=request.POST['email'])
                contract_object = get_object_or_404(Contract, field_contract=id_contract)
                for group in id_group:
                    Putevka.objects.create(field_pytevki=id_putevka,
                                           name_toure=item['tour'],
                                           cost=item['price'],
                                           idhotelroom=id_room,
                                           email=klient_object,
                                           field_contract=contract_object,
                                           field_groupp=group.field_groupp,
                                           )

            cart.clear()
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})