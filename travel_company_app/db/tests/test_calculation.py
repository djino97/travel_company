from django.test import SimpleTestCase
from db.calculation import *


class Hotel:

    def __init__(self, number_hotel, image_hotel):
        self.number_hotel = number_hotel
        self.image_hotel = image_hotel


class Tour:

    def __init__(self, id_tour):
        self.id_tour = id_tour


class Route:

    def __init__(self, tour, cost_of_route):
        self.name_tour = tour
        self.cost_of_route = cost_of_route


class HotelImgParserTest(SimpleTestCase):

    def setUp(self):
        self.hotel_img = HotelImgParser()

    def test_get_count_and_image_hotel_return_hotel_count_and_image(self):
        hotels = (Hotel(1, 'mariano.png'), Hotel(2, 'macadi,png'), Hotel(3, 'grand.png'))
        image_hotel, count_hotel = self.hotel_img.get_hotel_count_and_image(hotels)

        self.assertEquals(image_hotel, ['/static/toursimage/image_hotel/mariano.png',
                                        '/static/toursimage/image_hotel/macadi,png',
                                        '/static/toursimage/image_hotel/grand.png'
                                        ])
        self.assertEquals(count_hotel, [0, 1, 2])


class TourParserTest(SimpleTestCase):

    def setUp(self):
        self.tours = (Tour(1), Tour(2), Tour(3))
        self.tour_parser = TourParser(self.tours)

    def test_get_cost_tours_successful_return_count_and_coast_tour(self):
        routes = (Route(self.tours[0], 10000), Route(self.tours[1], 20000), Route(self.tours[2], 35000))
        result = self.tour_parser.get_cost_tours(self.tours, routes)

        self.assertEquals(result[0], [10000, 20000, 35000])
        self.assertEquals(result[1], [0, 1, 2])

