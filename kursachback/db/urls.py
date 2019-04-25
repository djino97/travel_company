from django.conf.urls import url
from . import views
from django.conf.urls import url, include



urlpatterns = [
    # post views
    #url(r'^login/$', views.user_login, name='login'),
    #url(r'^register/$', views.register, name='register'),

# login / logout urls
    url(r'^account/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^account/logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^account/logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    url(r'^$', views.main, name='main'),
    url(r'^account/register/$', views.register, name='register'),
    url(r'^(?P<idhotel>\d+)/(?P<slug_hotel>[-\w]+)/$', views.hotel_detali, name='detail_hotel'),
    url(r'^detail/(?P<id_tour>\d+)/(?P<slug>[-\w]+)/', views.tour_detali, name='tours_detail'),
]

