from django.contrib import admin
from .models import Klient, Tour, Excursion, Town, Route

admin.site.register(Klient)
admin.site.register(Excursion)
admin.site.register(Town)
admin.site.register(Route)


class TourAdmin(admin.ModelAdmin):
    list_display = ['id_tour', 'name_tour', 'image_tour', 'slug']
    prepopulated_fields = {'slug': ('id_tour',)}
admin.site.register(Tour, TourAdmin)



