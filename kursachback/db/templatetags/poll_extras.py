from django import template

register = template.Library()


@register.filter(name='dict_value_or_null')
def dict_value_or_null(dict, key):
    b = dict[key]
    return b


@register.filter(name='get_url')
def dict_value_or_null(obj, key):
    b = obj[key].get_absolute_url()
    return b


@register.filter(name='get_name_tour')
def dict_value_or_null(obj, key):
    b = obj[key].name_tour
    return b


@register.filter(name='img_hotel')
def img_hotel(obj, key):
    key = key - 1
    f = '/static/toursimage/image_hotel/%s' % obj[key].image_hotel
    return f


@register.filter(name='get_name_hotel')
def get_name_hotel(hotel, key):
    hotel = hotel[key].nametype
    return hotel


@register.filter(name='cart_img_tour')
def cart_img_tour(key):
    f = '/static/toursimage/image_tour/%s' % key.image_tour
    return f


@register.filter(name='star_hotel')
def star_hotel(obj, key):
    f = len(obj[key].typeofhotel) + 1
    return f
