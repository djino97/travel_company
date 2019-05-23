from django.http import HttpResponse
from django.shortcuts import render, render_to_response,get_object_or_404
from django.contrib.auth import authenticate, login
from db.forms import LoginForm, UserRegistrationForm
from .models import (Tour, Putevka, Route, Station, Routehotel,Hotel)
from .math import load_text, coast_tours, pars, img_hotel, img_tours, img_tour_detail, search_tour_country, \
    load_text_hotel
from cart.forms import CartAddTourForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/registration/login.html', {'form': form})


def main(request):
    if request.GET:
        try:
            route_country = 0
            if request.GET['country']:
                route_country = Route.objects.filter(station__nametown__namecountry='%s' % request.GET['country'])
            elif request.GET['season']:
                route_country = Route.objects.filter(season='%s' % request.GET['season'])
            elif request.GET['date']:
                route_country = Route.objects.filter(groupp__departuredate='%s' % request.GET['date'])
            elif request.GET['country'] and request.GET['season'] and request.GET['date']:
                route_country = Route.objects.filter(groupp__departuredate='%s' % request.GET['date']).\
                    filter(season='%s' % request.GET['season']).filter(groupp__departuredate='%s' % request.GET['date'])
                tours_country = search_tour_country(route_country)
                tours_country_search = Tour.objects.filter(route__field_route__in=tours_country)
                route_country = Route.objects.filter(field_route__in=tours_country)
                coast_tour, count = coast_tours(tours_country_search, route_country)
                img_tour = img_tours(tours_country_search)
                return render_to_response('account/tours/main.html', {'tours_country_search': tours_country_search,
                                                                      'coast_tours': coast_tour,
                                                                      'count': count, 'img_tour': img_tour, })
            tours_country = search_tour_country(route_country)
            tours_country_search = Tour.objects.filter(route__field_route__in=tours_country)
            route_country = Route.objects.filter(field_route__in=tours_country)
            coast_tour, count = coast_tours(tours_country_search, route_country)
            img_tour = img_tours(tours_country_search)
            return render_to_response('account/tours/main.html', {'tours_country_search': tours_country_search,
                                                                  'coast_tours': coast_tour,
                                                                  'count': count, 'img_tour': img_tour,})

        except:
            return render_to_response('account/tours/main.html', {'empty': 'По вашему запросу ничего не найдено',
                                                                  })

    tours = Tour.objects.all()
    img_tour = img_tours(tours)
    route = Route.objects.all()
    coast_tour, count = coast_tours(tours, route)
    hotel = Hotel.objects.all()
    image_hotel, count_hotel = img_hotel(hotel)
    fiew_star = [1, 2, 3, 4, 5]
    return render(request, 'account/tours/main.html', {'section': 'main',
                                                       'tours': tours, 'coast_tours': coast_tour,
                                                       'count': count, 'img_tour': img_tour, 'idhotel': hotel,
                                                       'img_hotel': image_hotel, 'count_hotel': count_hotel,
                                                       'fiew_star': fiew_star})


def tour_detali(request, id_tour, slug):
    tours_detail = get_object_or_404(Tour,
                                     id_tour=id_tour,
                                     slug=slug,)
    detail_img = img_tour_detail(tours_detail)
    file_content = load_text(tours_detail)
    route = get_object_or_404(Route, name_toure=tours_detail.id_tour)
    station = Station.objects.filter(field_route=route.field_route)
    hotelroute = Routehotel.objects.filter(field_route=route.field_route)
    idhotel = pars(hotelroute)
    hotel = Hotel.objects.filter(idhotel__in=idhotel)
    image_hotel, count_hotel = img_hotel(hotel)
    cart_tour_form = CartAddTourForm()
    return render(request,
                  'account/tours/detail.html',
                  {'tours_detail': tours_detail, 'route': route, 'station': station,
                   'file_content': file_content, 'idhotel': hotel, 'detail_img': detail_img, 'img_hotel': image_hotel,
                   'count_hotel': count_hotel,  'cart_product_form': cart_tour_form})


def hotel_detali(request, idhotel, slug_hotel):
    hotel_detail = get_object_or_404(Hotel,
                                     idhotel=idhotel,
                                     slug_hotel=slug_hotel,)
    file_content = load_text_hotel(hotel_detail)
    star_hotel = []
    for st in hotel_detail.typeofhotel:
        star_hotel.append(st)
    return render(request,
                  'account/tours/detail_hotel.html', {'hotel_detail': hotel_detail,
                                                      'file_content': file_content, 'star': star_hotel})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

