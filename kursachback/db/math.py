import settings 

def load_text(tours_detail):
    f = open(settings.MEDIA_ROOT + '/toursimage/description_tour/%s' % tours_detail.description_tour,
             'r')
    file_content = f.read()
    f.close()
    return file_content

def load_text_hotel(hotel_detail):
    f = open(settings.MEDIA_ROOT + '/toursimage/description_hotel/%s' % hotel_detail.description_hotel,
             'r')
    file_content = f.read()
    f.close()
    return file_content


def img_hotel(hotel):
    file_content = []
    count = []
    for key, i in enumerate(hotel):
        count.append(key)
        f = '/static/toursimage/image_hotel/%s' % i.image_hotel
        file_content.append(f)
    return file_content, count


def img_tours(tour):
    img_content = []
    for i in tour:
        f = '/static/toursimage/image_tour/%s' % i.image_tour
        img_content.append(f)
    return img_content


def img_tour_detail(tour):
    tour_detail = '/static/toursimage/image_tour/%s' % tour.image_tour
    return tour_detail


def coast_tours(tours, routs):
    coast = []
    a = 0
    count = []

    if len(routs) > 1 and len(tours) > 1:
        for route_key, route in enumerate(routs):
            for key, tour in enumerate(tours):
                if route_key != 1:
                    count.append(key)
                if route.name_toure.id_tour == tour.id_tour:
                    a = a + route.costofroute
            if a > 0:
                coast.append(a)
        return [coast, count]

    elif len(routs) > 1:
        for route_key, route in enumerate(routs):
            count.append(0)
            a = + route.costofroute
            coast.append(a)
        return [coast, count]

    else:
        for rout in routs:
            a = + rout.costofroute
            coast.append(a)
            count.append(0)
            return [coast, count]


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

