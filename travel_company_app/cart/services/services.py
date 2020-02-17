from django.shortcuts import get_object_or_404
from db.models import Tour, Route


def get_tour(id_tour):
    return get_object_or_404(Tour, id_tour=id_tour)


def get_route(id_tour):
    return get_object_or_404(Route, name_toure=id_tour)


def add_to_cart(form, cart, tour, route):
    cd = form.cleaned_data

    cart.add(tour=tour,
             hotelroom=cd['hotelroom'],
             typeofpayment=cd['typeofpayment'],
             route=route,
             quantity=cd['quantity'],
             update_quantity=cd['update'])