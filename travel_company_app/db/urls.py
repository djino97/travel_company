from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^account/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^account/logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^account/logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    url(r'^$', views.main, name='main'),
    url(r'^account/register/$', views.register, name='register'),
    url(r'^hotel/(?P<id_hotel>\d+)/$', views.hotel_detail, name='detail_hotel'),
    url(r'^tour/(?P<id_tour>\d+)/$', views.tour_detail, name='tours_detail'),
]

