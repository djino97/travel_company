# Create your models here.
from django.db import models
from django.core.urlresolvers import reverse


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Contract(models.Model):
    field_contract = models.IntegerField(db_column='№Contract',
                                         primary_key=True)
    dateofconclusion = models.DateField(db_column='DateOfConclusion', blank=True,
                                        null=True)
    typeofpayment = models.CharField(db_column='TypeOfPayment', max_length=255, blank=True,
                                     null=True)

    class Meta:
        managed = True
        db_table = 'contract'


class CountryTable(models.Model):
    namecountry = models.CharField(db_column='NameCountry', primary_key=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'country_table'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Excursion(models.Model):
    nameexcursion = models.CharField(db_column='NameExcursion', max_length=255, blank=True, null=True)
    timestart = models.TimeField(db_column='TimeStart', blank=True, null=True)
    duration = models.TimeField(db_column='Duration', blank=True, null=True)
    idexcursion = models.IntegerField(db_column='IDExcursion', primary_key=True)
    nametown = models.ForeignKey('Town', db_column='NameTown', max_length=255, blank=True)
    image_excursion = models.ImageField(db_column='image_excursion', upload_to='image_excursion/')
    slug_excursion = models.SlugField(max_length=200, db_index=True)
    description_excursion = models.FileField(db_column='desc_excursion', upload_to='description_excursion/', blank=True)

    class Meta:
        managed = True
        db_table = 'excursion'


class Groupp(models.Model):
    field_groupp = models.IntegerField(db_column='№Groupp', primary_key=True)
    departuredate = models.DateField(db_column='DepartureDate', blank=True, null=True)
    field_route = models.ForeignKey('Route', db_column='№Route', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'groupp'


class Hotel(models.Model):
    idhotel = models.IntegerField(db_column='IDHotel', primary_key=True)
    typeofhotel = models.CharField(db_column='TypeOfHotel', max_length=255, blank=True, null=True)
    nametype = models.CharField(db_column='NameType', max_length=255, blank=True, null=True)
    durationresidence = models.IntegerField(db_column='DurationResidence', blank=True, null=True)
    image_hotel = models.ImageField(db_column='image_hotel', upload_to='image_hotel/')
    slug_hotel = models.SlugField(max_length=200, db_index=True)
    description_hotel = models.FileField(db_column='desc_hotel', upload_to='description_hotel/', blank=True)

    class Meta:
        managed = True
        db_table = 'hotel'

    def get_absolute_url(self):
        return reverse('hotel:detail_hotel',
                       args=[self.idhotel])


class Hotelroom(models.Model):
    idhotelroom = models.IntegerField(db_column='IDHotelRoom', primary_key=True)
    typehotelroom = models.CharField(db_column='TypeHotelRoom', max_length=255, blank=True, null=True)
    idhotel = models.ForeignKey('Hotel', db_column='IDHotel', blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'hotelroom'


class Klient(models.Model):
    fio = models.CharField(db_column='FIO', max_length=255, blank=True, null=True)
    dateofbirth = models.DateField(db_column='Dateofbirth', blank=True, null=True)
    email = models.CharField(db_column='EMail', primary_key=True, max_length=255)
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)
    phone = models.BigIntegerField(db_column='Phone', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'klient'


class Putevka(models.Model):
    field_pytevki = models.IntegerField(db_column='№Pytevki', primary_key=True)
    name_toure = models.ForeignKey('Tour', db_column='NameTour')
    cost = models.DecimalField(db_column='Cost', max_digits=15, decimal_places=2, blank=True, null=True)
    email = models.ForeignKey('Klient', db_column='EMail', max_length=255, blank=True, null=True)
    field_contract = models.ForeignKey('Contract', db_column='№Contract', blank=True, null=True)
    idhotelroom = models.IntegerField(db_column='IDHotelRoom', blank=True, null=True)
    field_groupp = models.IntegerField(db_column='№Groupp', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'putevka'

    def __str__(self):
        return 'Putevka {}'.format(self.name_toure)


class Putevkaexcursion(models.Model):
    idexcursion = models.ForeignKey('Excursion', db_column='IDExcursion', blank=True, )
    field_putevka = models.ForeignKey('Putevka', db_column='№Putevka', blank=True)

    class Meta:
        managed = True
        db_table = 'putevkaexcursion'
        unique_together = (('idexcursion', 'field_putevka'),)


class Tour(models.Model):
    id_tour = models.IntegerField(db_column='IdTour', primary_key=True, blank=True)
    name_tour = models.CharField(db_column='NameTour', max_length=255, blank=True, null=True)
    image_tour = models.ImageField(db_column='image_tour', upload_to='image_tour/')
    slug = models.SlugField(max_length=200, db_index=True)
    description_tour = models.FileField(blank=True, db_column='desc_tour', upload_to='/description_tour/')

    class Meta:
        managed = True
        db_table = 'tour'
        ordering = ('name_tour',)
        index_together = (('id_tour', 'slug'),)

    def get_absolute_url(self):
        return reverse('tours:tours_detail',
                       args=[self.id_tour])


class Route(models.Model):
    field_route = models.IntegerField(db_column='№Route', primary_key=True)
    name_toure = models.ForeignKey('Tour', db_column='NameTour')
    costofroute = models.DecimalField(db_column='CostOfRoute', max_digits=15, decimal_places=2, blank=True, null=True)
    durationofroute = models.IntegerField(db_column='DurationOfRoute', blank=True, null=True)
    season = models.CharField(db_column='Season', max_length=255, blank=True, null=True)
    minquantitypeople = models.IntegerField(db_column='MinQuantityPeople', blank=True, null=True)
    maxquantitypeople = models.IntegerField(db_column='MaxQuantityPeople', blank=True, null=True)
    insuranceamount = models.DecimalField(db_column='InsuranceAmount', max_digits=15, decimal_places=2, blank=True, null=True)
    image_route = models.ImageField(db_column='image_route', upload_to='image_route/')
    slug_route = models.SlugField(max_length=200, db_index=True)
    description_route = models.FileField(db_column='desc_route', upload_to='description_route/', blank=True)

    class Meta:
        managed = True
        db_table = 'route'


class Routehotel(models.Model):
    field_route = models.ForeignKey('Route', db_column='№Route', blank=True, null=True)
    idhotel = models.ForeignKey('Hotel', db_column='IDHotel', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'routehotel'


class Station(models.Model):
    numberstation = models.IntegerField(db_column='NumberStation', primary_key=True)
    field_route = models.ForeignKey('Route', db_column='№Route', blank=True, null=True)

    durationtimeresidence = models.CharField(db_column='DurationTimeResidence', max_length=255, blank=True, null=True)
    nametown = models.ForeignKey('Town', db_column='NameTown', max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'station'


class Town(models.Model):
    nametown = models.CharField(db_column='NameTown', primary_key=True, max_length=255)
    namecountry = models.ForeignKey('CountryTable', db_column='NameCountry', max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'town'
