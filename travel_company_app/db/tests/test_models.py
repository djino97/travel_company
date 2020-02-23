from django.test import SimpleTestCase
from db.models import AuthGroup, Contract, CountryTable, Excursion, Groupp, Hotel, Hotelroom, Klient


class AuthGroupTest(SimpleTestCase):

    @classmethod
    def setUpClass(cls):
        AuthGroup.objects.create(name='FirstGroup')

    def setUp(self):
        self.auth_group = AuthGroup.objects.get(id=1)

    def test_name_label(self):
        field_label = self.auth_group._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        field_length = self.auth_group._meta.get_field('name').max_length
        self.assertEquals(field_length, 80)


class ContractTest(SimpleTestCase):

    @classmethod
    def setUpClass(cls):
        Contract.objects.create(field_contract=23, dateofconclusion='2020-12-05', typeofpayment='yandex')

    def setUp(self):
        self.contract = Contract.objects.get(field_contract=23)

    def test_number_contract_label(self):
        field_label = self.contract._meta.get_field('field_contract').verbose_name
        self.assertEquals(field_label, 'field contract')

    def test_date_of_conclusion_label(self):
        field_label = self.contract._meta.get_field('date_of_conclusion').verbose_name
        self.assertEquals(field_label, 'date of conclusion')

    def test_type_of_payment_label(self):
        field_label = self.contract._meta.get_field('type_of_payment').verbose_name
        self.assertEquals(field_label, 'type of payment')

    def test_type_of_payment_max_length(self):
        field_length = self.contract._meta.get_field('type_of_payment').max_length
        self.assertEquals(field_length, 255)


class CountryTableTest(SimpleTestCase):

    @classmethod
    def setUpClass(cls):
        CountryTable.objects.create(namecountry='Греция')

    def setUp(self):
        self.country_table = CountryTable.objects.get(namecountry='Греция')

    def test_name_country_label(self):
        field_label = self.country_table._meta.get_field('name_country').verbose_name
        self.assertEquals(field_label, 'name country')

    def test_name_country_max_length(self):
        field_length = self.country_table._meta.get_field('name country').max_length
        self.assertEquals(field_length, 255)


class ExcursionTest(SimpleTestCase):

    @classmethod
    def setUpClass(cls):
        Excursion.objects.create(id_excursion=15, name_excursion='Таинственная Венеция', time_start='12:30:00',
                                 duration='10:20:00', name_town='Венеция', image_excursion='mysterious_venice.png',
                                 slug_excursion=1, description_excursion='mysterious_venice.txt')

    def setUp(self):
        self.excursion = Excursion.objects.get(id_excursion=15)

    def test_id_excursion_label(self):
        field_label = self.excursion._meta.get_field('id_excursion').verbose_name
        self.assertEquals(field_label, 'id excursion')

    def test_name_excursion_label(self):
        field_label = self.excursion._meta.get_field('name_excursion').verbose_name
        self.assertEquals(field_label, 'name excursion')

    def test_time_start_label(self):
        field_label = self.excursion._meta.get_field('time_start').verbose_name
        self.assertEquals(field_label, 'time start')

    def test_duration_label(self):
        field_label = self.excursion._meta.get_field('duration').verbose_name
        self.assertEquals(field_label, 'duration')

    def test_name_town_label(self):
        field_label = self.excursion._meta.get_field('name_town').verbose_name
        self.assertEquals(field_label, 'name town')

    def test_image_excursion_label(self):
        field_label = self.excursion._meta.get_field('image_excursion').verbose_name
        self.assertEquals(field_label, 'image excursion')

    def test_slug_excursion_label(self):
        field_label = self.excursion._meta.get_field('slug_excursion').verbose_name
        self.assertEquals(field_label, 'slug excursion')

    def test_description_excursion_label(self):
        field_label = self.excursion._meta.get_field('description_excursion').verbose_name
        self.assertEquals(field_label, 'description excursion')

    def test_name_excursion_max_length(self):
        field_length = self.excursion._meta.get_field('name_excursion').max_length
        self.assertEquals(field_length, 255)

    def test_name_town_max_length(self):
        field_length = self.excursion._meta.get_field('name_town').max_length
        self.assertEquals(field_length, 255)


class GrouppTest(SimpleTestCase):

    @classmethod
    def setUpClass(cls):
        Groupp.objects.create(field_groupp=10, departure_date='2020-10-05', field_route=101)

    def setUp(self):
        self.group = Groupp.objects.get(field_groupp=10)

    def test_field_groupp_label(self):
        field_label = self.group._meta.get_field('field_groupp').verbose_name
        self.assertEquals(field_label, 'field groupp')

    def test_departure_date_label(self):
        field_label = self.group._meta.get_field('departure_date').verbose_name
        self.assertEquals(field_label, 'departure date')

    def test_field_route_label(self):
        field_label = self.group._meta.get_field('field_route').verbose_name
        self.assertEquals(field_label, 'field route')


class HotelTest(SimpleTestCase):

    @classmethod
    def setUpClass(cls):
        Hotel.objects.create(id_hotel=10, type_of_hotel='***', name_type='Mariano', duration_residence=15,
                             image_hotel='mariano.png', slug_hotel=10, description_hotel='mariano.txt')

    def setUp(self):
        self.hotel = Hotel.objects.get(id_hotel=10)

    def test_id_hotel_label(self):
        field_label = self.hotel._meta.get_field('id_hotel').verbose_name
        self.assertEquals(field_label, 'id hotel')

    def test_type_of_hotel_label(self):
        field_label = self.hotel._meta.get_field('type_of_hotel').verbose_name
        self.assertEquals(field_label, 'type of hotel')

    def test_name_type_label(self):
        field_label = self.hotel._meta.get_field('name_type').verbose_name
        self.assertEquals(field_label, 'name type')

    def test_duration_residence_label(self):
        field_label = self.hotel._meta.get_field('duration_residence').verbose_name
        self.assertEquals(field_label, 'duration residence')

    def test_image_hotel_label(self):
        field_label = self.hotel._meta.get_field('image hotel').verbose_name
        self.assertEquals(field_label, 'image hotel')

    def test_slug_hotel_label(self):
        field_label = self.hotel._meta.get_field('slug_hotel').verbose_name
        self.assertEquals(field_label, 'slug hotel')

    def test_description_hotel_label(self):
        field_label = self.hotel._meta.get_field('description_hotel').verbose_name
        self.assertEquals(field_label, 'description hotel')

    def test_type_of_hotel_max_length(self):
        field_length = self.hotel._meta.get_field('type_of_hotel').max_length
        self.assertEquals(field_length, 255)

    def test_name_type_max_length(self):
        field_length = self.hotel._meta.get_field('name_type').max_length
        self.assertEquals(field_length, 255)

    def test_slug_hotel_max_length(self):
        field_length = self.hotel._meta.get_field('slug_hotel').max_length
        self.assertEquals(field_length, 200)


class HotelroomTest(SimpleTestCase):

    @classmethod
    def setUpClass(cls):
        Hotelroom.objects.create(id_hotel_room=20, type_hotel_room='****', id_hotel=10)

    def setUp(self):
        self.hotel_room = Hotelroom.objects.get(id_hotel=20)

    def test_id_hotel_room_label(self):
        field_label = self.hotel_room._meta.get_field('id_hotel_room').verbose_name
        self.assertEquals(field_label, 'id hotel room')

    def test_type_hotel_room_label(self):
        field_label = self.hotel_room._meta.get_field('type_hotel_room').verbose_name
        self.assertEquals(field_label, 'type hotel room')

    def test_id_hotel_label(self):
        field_label = self.hotel_room._meta.get_field('id_hotel').verbose_name
        self.assertEquals(field_label, 'id hotel')

    def test_type_hotel_room_max_length(self):
        field_length = self.hotel_room._meta.get_field('type_hotel_room').max_length
        self.assertEquals(field_length, 200)


class KlientTest(SimpleTestCase):

    @classmethod
    def setUpClass(cls):
        Klient.objects.create(fio='Ковалев Иван Васильевич', date_of_birth='2020-10-05', email='kovalev@gmail.com',
                              address='Moscow, Lenina 20', phone=89610210423)

    def setUp(self):
        self.client = Klient.objects.get(id_hotel=20)

    def test_fio_label(self):
        field_label = self.client._meta.get_field('fio').verbose_name
        self.assertEquals(field_label, 'fio')

    def test_date_of_birth_label(self):
        field_label = self.client._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')

    def test_email_label(self):
        field_label = self.client._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_address_label(self):
        field_label = self.client._meta.get_field('address').verbose_name
        self.assertEquals(field_label, 'address')

    def test_phone_label(self):
        field_label = self.client._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'phone')

    def test_fio_max_length(self):
        field_length = self.client._meta.get_field('fio').max_length
        self.assertEquals(field_length, 255)

    def test_email_max_length(self):
        field_length = self.client._meta.get_field('email').max_length
        self.assertEquals(field_length, 255)

    def test_address_max_length(self):
        field_length = self.client._meta.get_field('address').max_length
        self.assertEquals(field_length, 255)


