# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('field_contract', models.IntegerField(primary_key=True, serialize=False, db_column='№Contract')),
                ('dateofconclusion', models.DateField(blank=True, null=True, db_column='DateOfConclusion')),
                ('typeofpayment', models.CharField(max_length=255, blank=True, null=True, db_column='TypeOfPayment')),
            ],
            options={
                'db_table': 'contract',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CountryTable',
            fields=[
                ('namecountry', models.CharField(primary_key=True, max_length=255, serialize=False, db_column='NameCountry')),
            ],
            options={
                'db_table': 'country_table',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Excursion',
            fields=[
                ('nameexcursion', models.CharField(max_length=255, blank=True, null=True, db_column='NameExcursion')),
                ('timestart', models.TimeField(blank=True, null=True, db_column='TimeStart')),
                ('duration', models.TimeField(blank=True, null=True, db_column='Duration')),
                ('idexcursion', models.IntegerField(primary_key=True, serialize=False, db_column='IDExcursion')),
                ('image_excursion', models.ImageField(db_column='image_excursion', upload_to='image_excursion/')),
                ('slug_excursion', models.SlugField(max_length=200)),
                ('description_excursion', models.FileField(blank=True, db_column='desc_excursion', upload_to='description_excursion/')),
            ],
            options={
                'db_table': 'excursion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Groupp',
            fields=[
                ('field_groupp', models.IntegerField(primary_key=True, serialize=False, db_column='№Groupp')),
                ('departuredate', models.DateField(blank=True, null=True, db_column='DepartureDate')),
            ],
            options={
                'db_table': 'groupp',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('idhotel', models.IntegerField(primary_key=True, serialize=False, db_column='IDHotel')),
                ('typeofhotel', models.CharField(max_length=255, blank=True, null=True, db_column='TypeOfHotel')),
                ('nametype', models.CharField(max_length=255, blank=True, null=True, db_column='NameType')),
                ('durationresidence', models.IntegerField(blank=True, null=True, db_column='DurationResidence')),
                ('image_hotel', models.ImageField(db_column='image_hotel', upload_to='image_hotel/')),
                ('slug_hotel', models.SlugField(max_length=200)),
                ('description_hotel', models.FileField(blank=True, db_column='desc_hotel', upload_to='description_hotel/')),
            ],
            options={
                'db_table': 'hotel',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Hotelroom',
            fields=[
                ('idhotelroom', models.IntegerField(primary_key=True, serialize=False, db_column='IDHotelRoom')),
                ('typehotelroom', models.CharField(max_length=255, blank=True, null=True, db_column='TypeHotelRoom')),
                ('idhotel', models.ForeignKey(blank=True, null=True, db_column='IDHotel', to='db.Hotel')),
            ],
            options={
                'db_table': 'hotelroom',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('fio', models.CharField(max_length=255, blank=True, null=True, db_column='FIO')),
                ('dateofbirth', models.DateField(blank=True, null=True, db_column='Dateofbirth')),
                ('email', models.CharField(primary_key=True, max_length=255, serialize=False, db_column='EMail')),
                ('address', models.CharField(max_length=255, blank=True, null=True, db_column='Address')),
                ('phone', models.BigIntegerField(blank=True, null=True, db_column='Phone')),
            ],
            options={
                'db_table': 'klient',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Putevka',
            fields=[
                ('field_pytevki', models.IntegerField(primary_key=True, serialize=False, db_column='№Pytevki')),
                ('cost', models.DecimalField(blank=True, null=True, db_column='Cost', max_digits=15, decimal_places=2)),
                ('idhotelroom', models.IntegerField(blank=True, null=True, db_column='IDHotelRoom')),
                ('field_groupp', models.IntegerField(blank=True, null=True, db_column='№Groupp')),
                ('email', models.ForeignKey(max_length=255, blank=True, null=True, db_column='EMail', to='db.Klient')),
                ('field_contract', models.ForeignKey(blank=True, null=True, db_column='№Contract', to='db.Contract')),
            ],
            options={
                'db_table': 'putevka',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Putevkaexcursion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('field_putevka', models.ForeignKey(blank=True, db_column='№Putevka', to='db.Putevka')),
                ('idexcursion', models.ForeignKey(blank=True, db_column='IDExcursion', to='db.Excursion')),
            ],
            options={
                'db_table': 'putevkaexcursion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('field_route', models.IntegerField(primary_key=True, serialize=False, db_column='№Route')),
                ('costofroute', models.DecimalField(blank=True, null=True, db_column='CostOfRoute', max_digits=15, decimal_places=2)),
                ('durationofroute', models.IntegerField(blank=True, null=True, db_column='DurationOfRoute')),
                ('season', models.CharField(max_length=255, blank=True, null=True, db_column='Season')),
                ('minquantitypeople', models.IntegerField(blank=True, null=True, db_column='MinQuantityPeople')),
                ('maxquantitypeople', models.IntegerField(blank=True, null=True, db_column='MaxQuantityPeople')),
                ('insuranceamount', models.DecimalField(blank=True, null=True, db_column='InsuranceAmount', max_digits=15, decimal_places=2)),
                ('image_route', models.ImageField(db_column='image_route', upload_to='image_route/')),
                ('slug_route', models.SlugField(max_length=200)),
                ('description_route', models.FileField(blank=True, db_column='desc_route', upload_to='description_route/')),
            ],
            options={
                'db_table': 'route',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Routehotel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('field_route', models.ForeignKey(blank=True, null=True, db_column='№Route', to='db.Route')),
                ('idhotel', models.ForeignKey(blank=True, null=True, db_column='IDHotel', to='db.Hotel')),
            ],
            options={
                'db_table': 'routehotel',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('numberstation', models.IntegerField(primary_key=True, serialize=False, db_column='NumberStation')),
                ('durationtimeresidence', models.CharField(max_length=255, blank=True, null=True, db_column='DurationTimeResidence')),
                ('field_route', models.ForeignKey(blank=True, null=True, db_column='№Route', to='db.Route')),
            ],
            options={
                'db_table': 'station',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id_tour', models.IntegerField(primary_key=True, blank=True, serialize=False, db_column='IdTour')),
                ('name_tour', models.CharField(max_length=255, blank=True, null=True, db_column='NameTour')),
                ('image_tour', models.ImageField(db_column='image_tour', upload_to='image_tour/')),
                ('slug', models.SlugField(max_length=200)),
                ('description_tour', models.FileField(blank=True, db_column='desc_tour', upload_to='description_tour/')),
            ],
            options={
                'db_table': 'tour',
                'ordering': ('name_tour',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('nametown', models.CharField(primary_key=True, max_length=255, serialize=False, db_column='NameTown')),
                ('namecountry', models.ForeignKey(max_length=255, blank=True, null=True, db_column='NameCountry', to='db.CountryTable')),
            ],
            options={
                'db_table': 'town',
                'managed': True,
            },
        ),
        migrations.AlterIndexTogether(
            name='tour',
            index_together=set([('id_tour', 'slug')]),
        ),
        migrations.AddField(
            model_name='station',
            name='nametown',
            field=models.ForeignKey(max_length=255, blank=True, null=True, db_column='NameTown', to='db.Town'),
        ),
        migrations.AddField(
            model_name='route',
            name='name_toure',
            field=models.ForeignKey(db_column='NameTour', to='db.Tour'),
        ),
        migrations.AddField(
            model_name='putevka',
            name='name_toure',
            field=models.ForeignKey(db_column='NameTour', to='db.Tour'),
        ),
        migrations.AddField(
            model_name='groupp',
            name='field_route',
            field=models.ForeignKey(blank=True, null=True, db_column='№Route', to='db.Route'),
        ),
        migrations.AddField(
            model_name='excursion',
            name='nametown',
            field=models.ForeignKey(max_length=255, blank=True, db_column='NameTown', to='db.Town'),
        ),
        migrations.AlterUniqueTogether(
            name='putevkaexcursion',
            unique_together=set([('idexcursion', 'field_putevka')]),
        ),
    ]
