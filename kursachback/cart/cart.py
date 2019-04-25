from decimal import Decimal
from django.conf import settings
from db.models import Tour


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, tour, hotelroom,typeofpayment, route, quantity=1, update_quantity=False):
        """
        Добавить тур в корзину или обновить его количество.
        """
        tour_id = str(tour.id_tour)
        if tour_id not in self.cart:
            self.cart[tour_id] = {'quantity': 0,
                                  'price': str(route.costofroute),
                                  'hotelroom': str(hotelroom),
                                  'typeofpayment': typeofpayment}
        if update_quantity:
            self.cart[tour_id]['quantity'] = quantity
        else:
            self.cart[tour_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, tour):
        """
        Удаление тура из корзины.
        """
        tour_id = str(tour.id_tour)
        if tour_id in self.cart:
            del self.cart[tour_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине и получение туров из базы данных.
        """
        tour_ids = self.cart.keys()
        # получение объектов tour и добавление их в корзину
        tours = Tour.objects.filter(id_tour__in=tour_ids)
        for tour in tours:
            self.cart[str(tour.id_tour)]['tour'] = tour

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Подсчет всех туров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет общей стоимости туров в корзине.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

