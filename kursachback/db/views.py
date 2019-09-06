from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login

from db.forms import LoginForm, UserRegistrationForm

from .models import (Tour, Groupp, Route, Station, Routehotel, Hotel)
from .calculation import load_text, pars, HotelImgParser, \
    TourParser, search_tour_country, load_text_hotel, ImageTour

from cart.forms import CartAddTourForm


def user_login(request):
    """
    Checks whether a user in the database includes,
    if there is, it display the template login.html
    :param request: data user information
    :return: render login.html
    """
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
    """
    The main page view display the display all the tours and all the hotels
    :param request: entered user data in the line search
    :return: issued the requested information or information about all the tours and hotels
    """
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

                image_tour = ImageTour(tours_country_search)
                img_tour = image_tour.get_path_tours_to_image()

                tour_parser = TourParser(tours_country_search)
                route_country = Route.objects.filter(field_route__in=tours_country)
                coast_tour, count = tour_parser.get_coast_tours(tours_country_search, route_country)

                return render_to_response('account/tours/main.html', {'tours_country_search': tours_country_search,
                                                                      'coast_tours': coast_tour,
                                                                      'count': count, 'img_tour': img_tour, })

            tours_country = search_tour_country(route_country)
            tours_country_search = Tour.objects.filter(route__field_route__in=tours_country)

            tour_parser = TourParser(tours_country_search)

            route_country = Route.objects.filter(field_route__in=tours_country)
            coast_tour, count = tour_parser.get_coast_tours(tours_country_search, route_country)

            image_tour = ImageTour(tours_country_search)
            img_tour = image_tour.get_path_tours_to_image()
            return render_to_response('account/tours/main.html', {'tours_country_search': tours_country_search,
                                                                  'coast_tours': coast_tour,
                                                                  'count': count, 'img_tour': img_tour, })

        except:
            return render_to_response('account/tours/main.html', {'empty': 'По вашему запросу ничего не найдено',
                                                                  })

    tours = Tour.objects.all()
    tour_parser = TourParser(tours)
    image_tour = ImageTour(tours)
    img_tour = image_tour.get_path_tours_to_image()
    groupp_supply = Groupp.objects.all()
    route = Route.objects.all()
    coast_tour, count = tour_parser.get_coast_tours(tours, route)
    hotel = Hotel.objects.all()
    instance_img_hotel = HotelImgParser()
    image_hotel, count_hotel = instance_img_hotel.get_number_hotel(hotel)
    star_hotel_main = {}
    number_hotel = 0
    for st in hotel:
            star_hotel_main[number_hotel] = st.typeofhotel
            number_hotel += 1
    return render(request, 'account/tours/main.html', {'section': 'main',
                                                       'tours': tours, 'coast_tours': coast_tour,
                                                       'count': count, 'img_tour': img_tour, 'idhotel': hotel,
                                                       'img_hotel': image_hotel, 'count_hotel': count_hotel,
                                                       'star_hotel_main': star_hotel_main, 'group': groupp_supply})


def tour_detail(request, id_tour, slug):
    """
    A view for description of each tour
    :param request:
    :param id_tour:
    :param slug:
    :return: display the template detail.html with the description of the tour
    """
    tours_detail = get_object_or_404(Tour,
                                     id_tour=id_tour,
                                     slug=slug,)
    detail_img = ImageTour(tours_detail).get_path_tour_to_image()
    file_content = load_text(tours_detail)
    route = get_object_or_404(Route, name_toure=tours_detail.id_tour)
    station = Station.objects.filter(field_route=route.field_route)
    hotelroute = Routehotel.objects.filter(field_route=route.field_route)
    idhotel = pars(hotelroute)
    hotel = Hotel.objects.filter(idhotel__in=idhotel)
    instance_img_hotel = HotelImgParser()
    image_hotel, count_hotel = instance_img_hotel.get_number_hotel(hotel)
    cart_tour_form = CartAddTourForm()
    return render(request,
                  'account/tours/detail.html',
                  {'tours_detail': tours_detail, 'route': route, 'station': station,
                   'file_content': file_content, 'idhotel': hotel, 'detail_img': detail_img, 'img_hotel': image_hotel,
                   'count_hotel': count_hotel,  'cart_product_form': cart_tour_form})


def hotel_detali(request, idhotel, slug_hotel):
    """
    A view for description of each hotel
    :param request:
    :param idhotel:
    :param slug_hotel:
    :return: display the template detail_hotel.html with the description of the tour
    """
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
    """
    Logs the user into the database if all the
    fields are entered correctly display register_done.html, otherwise register.html
    :param request:
    :return:
    """
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

