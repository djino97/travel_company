from travel_company_app import settings


class HotelImgParser:

    def __init__(self):
        self.file_content = []
        self.count = []

    def __get_hotels_img_by_number(self, hotel_key, number_hotel):
        f = '/static/toursimage/image_hotel/%s' % number_hotel.image_hotel
        self.count.append(hotel_key)
        self.file_content.append(f)

    def get_hotel_count_and_image(self, hotel):
        for key, i in enumerate(hotel):
            self.__get_hotels_img_by_number(key, i)

        return self.file_content, self.count


class TourParser:

    def __init__(self, tour):
        self.cost = []
        self.count_tours = []
        self.tmp_a = 0
        self.tour = tour

    def get_cost_tours(self, tours, routes):
        if len(routes) > 1 and len(tours) > 1:
            self.__parsing_tours_and_routes(tours, routes)
            return [self.cost, self.count_tours]

        elif len(routes) > 1:
            self.__parsing_routes(routes)
            return [self.cost, self.count_tours]

        else:
            for route in routes:
                self.__adding_in_the_list_new_cost_tour(route)
            return [self.cost, self.count_tours]

    def __parsing_tours_and_routes(self, tours, routes):
        for route in routes:
            for key, tour in enumerate(tours):
                self.search_and_adding_coincide_tours(key, tour, route)
            if self.tmp_a != 0:
                self.cost.append(self.tmp_a)
                self.tmp_a = 0

    def search_and_adding_coincide_tours(self, tour_key, tour, route):

        if route.name_tour.id_tour == tour.id_tour:
            self.tmp_a = self.tmp_a + route.cost_of_route
            self.count_tours.append(tour_key)

    def __parsing_routes(self, routes):
        for route in routes:
            self.__adding_in_the_list_new_route(route)

    def __adding_in_the_list_new_route(self, route):
        self.count_tours.append(0)
        a = + route.costofroute
        self.cost.append(a)

    def __adding_in_the_list_new_cost_tour(self, route):
        a = + route.costofroute
        self.cost.append(a)
        self.count_tours.append(0)


class ImageTour:

    def __init__(self, tour):
        self.img_content = []
        self.__path = '/static/toursimage/image_tour/{}'
        self.tour = tour

    def get_path_tours_to_image(self):
        for i in self.tour:
            img_tour = self.__path.format(i.image_tour)
            self.img_content.append(img_tour)
        return self.img_content

    def get_path_tour_to_image(self):
        return self.__path.format(self.tour.image_tour)


def load_text(tours_detail):
    f = open(settings.MEDIA_ROOT + 'description_tour/%s' % tours_detail.description_tour,
             'r')
    file_content = f.read()
    f.close()
    return file_content


def load_text_hotel(hotel_detail):
    f = open(settings.MEDIA_ROOT + 'description_hotel/%s' % hotel_detail.description_hotel,
             'r')
    file_content = f.read()
    f.close()
    return file_content


def search_tour_country(route_country):
    f = []
    if len(route_country) > 1:
        for b in route_country:
            f.append(b.field_route)
        else:
            f = list(set(f))

    else:
        for b in route_country:
            f.append(b.field_route)
    return f


def pars(hotelroute):
    hotel = []
    for a in hotelroute:
        hotel.append(a.idhotel.idhotel)

    return hotel


def get_id_hotel_room(id_hotel_room):
    for id_room in id_hotel_room:
        room = id_room.idhotelroom
        return room
