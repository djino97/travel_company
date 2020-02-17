from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login

from db.forms import LoginForm, UserRegistrationForm
from db.services.services import TourCalculation, AllTour, TourDetail
from .models import Hotel
from .calculation import load_text_hotel


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
    The main page view display all the tours and all the hotels
    :param request: entered user data in the line search
    :return: issued the requested information or information about all the tours and hotels
    """
    if request.GET:

        try:
            TourCalculation.put_get_request(request.GET)
            TourCalculation.find_route_related_request(request.GET)

            tour_calculation = TourCalculation()
            tour = tour_calculation.get_country_and_image_related_with_tour()

            return render_to_response('account/tours/main.html', {'tours_country_search': tour['tours_country_search'],
                                                                  'cost_tours': tour['cost_tours'],
                                                                  'count': tour['count'], 'img_tour': tour['img_tour'],
                                                                  })

        except:
            return render_to_response('account/tours/main.html', {'empty': 'По вашему запросу ничего не найдено',
                                                                  })

    all_tour = AllTour.execute({})

    return render(request, 'account/tours/main.html', {'section': 'main',
                                                       'tours': all_tour.tours, 'cost_tours': all_tour.cost_tour,
                                                       'count': all_tour.count, 'img_tour': all_tour.img_tour,
                                                       'id_hotel': all_tour.id_hotel, 'img_hotel': all_tour.img_hotel,
                                                       'count_hotel': all_tour.hotel_count, 'star_hotel_main': all_tour.hotel_stars,
                                                       'group': all_tour.date_departure
                                                       })


def tour_detail(request, id_tour):
    """
    A view for description of each tour
    :param request:
    :param id_tour:
    :return: display the template detail.html with the description of the tour
    """

    _tour_detail = TourDetail.execute({
        'tour_detail': id_tour,
    })

    return render(request,
                  'account/tours/detail.html',
                  {'tours_detail': _tour_detail.tour, 'route': _tour_detail.route,
                   'stations': _tour_detail.stations, 'file_content': _tour_detail.tour_description,
                   'hotel': _tour_detail.hotel, 'detail_img': _tour_detail.tour_img,
                   'img_hotel': _tour_detail.image_hotel, 'count_hotel': _tour_detail.count_hotel,
                   'cart_product_form': _tour_detail.cart_tour_form
                   })


def hotel_detail(request, id_hotel):
    """
    A view for description of each hotel
    :param request:
    :param id_hotel:
    :return: display the template detail_hotel.html with the description of the tour
    """
    _hotel_detail = get_object_or_404(Hotel,
                                     idhotel=id_hotel)
    file_content = load_text_hotel(_hotel_detail)
    star_hotel = []
    for st in _hotel_detail.typeofhotel:
        star_hotel.append(st)
    return render(request,
                  'account/tours/detail_hotel.html', {'hotel_detail': _hotel_detail,
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
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

