from django.db import models


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


class City(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=35)  # Field name made lowercase.
    countrycode = models.ForeignKey('Country', models.DO_NOTHING, db_column='CountryCode')  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=20)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    code = models.CharField(db_column='Code', primary_key=True, max_length=3)  # Field name made lowercase
    continent = models.CharField(db_column='Continent', max_length=13)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=26)  # Field name made lowercase.
    surfacearea = models.FloatField(db_column='SurfaceArea')  # Field name made lowercase.
    indepyear = models.SmallIntegerField(db_column='IndepYear', blank=True, null=True)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population')  # Field name made lowercase.
    lifeexpectancy = models.FloatField(db_column='LifeExpectancy', blank=True, null=True)  # Field name made lowercase.
    gnp = models.FloatField(db_column='GNP', blank=True, null=True)  # Field name made lowercase.
    gnpold = models.FloatField(db_column='GNPOld', blank=True, null=True)  # Field name made lowercase.
    localname = models.CharField(db_column='LocalName', max_length=45)  # Field name made lowercase.
    governmentform = models.CharField(db_column='GovernmentForm', max_length=45)  # Field name made lowercase.
    headofstate = models.CharField(db_column='HeadOfState', max_length=60, blank=True, null=True)  # Field name made lowercase.
    capital = models.IntegerField(db_column='Capital', blank=True, null=True)  # Field name made lowercase.
    code2 = models.CharField(db_column='Code2', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'country'


class Countrylanguage(models.Model):
    countrycode = models.ForeignKey(Country, models.DO_NOTHING, db_column='CountryCode')  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=30)  # Field name made lowercase.
    isofficial = models.CharField(db_column='IsOfficial', max_length=1)  # Field name made lowercase.
    percentage = models.FloatField(db_column='Percentage')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'countrylanguage'
        unique_together = (('countrycode', 'language'),)


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

