from service_objects.services import Service
from django.forms import ModelChoiceField
from django.shortcuts import get_object_or_404
from cart.forms import CartAddTourForm

from db.models import (Tour, Route, Station, Routehotel, Hotel, Groupp)
from db.calculation import TourParser, search_tour_country, load_text_hotel, ImageTour, HotelImgParser, pars, load_text


class TourCalculation:

    country = None
    season = None
    date = None

    route = ()

    @staticmethod
    def put_get_request(get_request):
        TourCalculation.country = get_request['country']
        TourCalculation.season = get_request['season']
        TourCalculation.date = get_request['date']

    @staticmethod
    def find_route_related_request(get_request):

        if get_request['country'] and get_request['season'] and get_request['date']:
            TourCalculation.route = TourCalculation.get_route_related_with_country_season_date()

        elif get_request['country']:
            TourCalculation.route = TourCalculation.get_route_related_with_country()

        elif get_request['season']:
            TourCalculation.route = TourCalculation.get_route_related_with_season()

        elif get_request['date']:
            TourCalculation.route = TourCalculation.get_route_related_with_date()

        else:
            raise

    @staticmethod
    def get_route_related_with_country():
        return Route.objects.filter(station__nametown__namecountry=TourCalculation.country)

    @staticmethod
    def get_route_related_with_season():
        return Route.objects.filter(season=TourCalculation.season)

    @staticmethod
    def get_route_related_with_date():
        return Route.objects.filter(groupp__departuredate=TourCalculation.date)

    @staticmethod
    def get_route_related_with_country_season_date():
        return Route.objects.filter(groupp__departuredate=TourCalculation.date).\
                    filter(season=TourCalculation.season).filter(station__nametown__namecountry=TourCalculation.country)

    def get_country_and_image_related_with_tour(self):
        tours_country = search_tour_country(TourCalculation.route)
        tours_country_search = Tour.objects.filter(route__field_route__in=tours_country)

        cost_tours, count = self.__get_cost_tours_and_count_tours(tours_country, tours_country_search)

        img_tour = self.__get_image_tour(tours_country_search)

        return {'tours_country_search': tours_country_search, 'cost_tours': cost_tours,
                'count': count, 'img_tour': img_tour}

    def __get_cost_tours_and_count_tours(self, tours_country, tours_country_search):
        tour_parser = TourParser(tours_country_search)
        route_country = Route.objects.filter(field_route__in=tours_country)

        return tour_parser.get_cost_tours(tours_country_search, route_country)

    def __get_image_tour(self, tours_country_search):
        image_tour = ImageTour(tours_country_search)

        return image_tour.get_path_tours_to_image()


class AllTour(Service):
    tours = None
    date_departure = None

    def process(self):
        tours = Tour.objects.all()
        self.tours = tours
        tour_parser = TourParser(tours)

        self.date_departure = Groupp.objects.all()

        self.__put_tours_image_and_tours_cost_and_tour_counting(tours, tour_parser)
        self.__put_hotels_and_hotels_image_and_hotel_counting()
        return self

    def __put_tours_image_and_tours_cost_and_tour_counting(self, tours, tour_parser):
        image_tour = ImageTour(tours)
        self.img_tour = image_tour.get_path_tours_to_image()

        route = Route.objects.all()
        self.cost_tour, self.count = tour_parser.get_cost_tours(tours, route)

    def __put_hotels_and_hotels_image_and_hotel_counting(self):
        id_hotel = Hotel.objects.all()
        self.id_hotel = id_hotel

        instance_img_hotel = HotelImgParser()
        self.__put_hotel_stars(id_hotel)

        self.img_hotel, self.hotel_count = instance_img_hotel.get_number_hotel(id_hotel)

    def __put_hotel_stars(self, hotel):
        star_hotel_main = {}
        number_hotel = 0

        for st in hotel:
            star_hotel_main[number_hotel] = st.typeofhotel
            number_hotel += 1

        self.hotel_stars = star_hotel_main


class TourDetail(Service):
    tour_detail = ModelChoiceField(queryset=Tour.objects.all())

    tour = None

    def process(self):
        tour_detail = self.cleaned_data['tour_detail']
        self.tour = tour_detail

        self.__put_tour_image_and_tour_description()
        self.__put_route_and_stations_related_with_tour()
        self.__put_hotel_and_image_hotel_and_count_hotel()
        self.__put_cart_tour_form()

        return self

    def __put_tour_image_and_tour_description(self):
        self.tour_img = ImageTour(self.tour).get_path_tour_to_image()
        self.tour_description = load_text(self.tour)

    def __put_route_and_stations_related_with_tour(self):
        self.route = get_object_or_404(Route, name_toure=self.tour.id_tour)
        self.stations = Station.objects.filter(field_route=self.route.field_route)

    def __put_hotel_and_image_hotel_and_count_hotel(self):
        hotel_route = Routehotel.objects.filter(field_route=self.route.field_route)
        id_hotel = pars(hotel_route)
        self.hotel = Hotel.objects.filter(idhotel__in=id_hotel)
        instance_img_hotel = HotelImgParser()
        self.image_hotel, self.count_hotel = instance_img_hotel.get_number_hotel(self.hotel)

    def __put_cart_tour_form(self):
        self.cart_tour_form = CartAddTourForm()

