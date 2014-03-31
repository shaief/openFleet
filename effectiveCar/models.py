from django.conf import settings
from django.db import models
from datetime import datetime


class Department(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name


class Manager(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=30)
    email = models.EmailField(null=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name


class Owner(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    # CHOICES = ['A2', 'A1', 'A', 'B', 'C1', 'C',
    #            'D', 'D1', 'D2', 'D3', 'E', '1']
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    license_category = models.CharField(max_length=2)
    license_renewal_date = models.DateField()
    department = models.ForeignKey(Department)
    manager_name = models.ForeignKey(Manager)
    image = models.ImageField(upload_to='owners/',
                              default='owners/None/no-img.jpg')

    class Meta:
        unique_together = ("first_name", "last_name")

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.first_name + " " + self.last_name


class Classification(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    group = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.group


class Car(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    This_Year = datetime.today().year
    CHOICES = [(i, i) for i in range(This_Year-8, This_Year+1)]
    nickname = models.CharField(max_length=100)
    license_id = models.CharField(max_length=9, unique=True)
    classification = models.ForeignKey(Classification)
    car_model = models.CharField(max_length=20)
    maker = models.CharField(max_length=20)
    color = models.CharField(max_length=20, default='white')
    production_year = models.SmallIntegerField(choices=CHOICES)
    date_of_purchase = models.DateField()
    km_read_at_purchase = models.IntegerField()
    license_renewal_date = models.DateField()
    insurance_renewal_date = models.DateField()
    current_owner = models.ForeignKey(Owner)
    status = models.CharField(max_length=30, default='Active')

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.license_id


class CarStatus(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    CHOICES = (('active', 'Active'),
               ('not active', 'Not active'),
               ('sold', 'Sold'))
    license_id = models.ForeignKey(Car)
    status = models.CharField(max_length=20, choices=CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateField(default=datetime.today())

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.status


class MonthlyRecord(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    This_Year = datetime.today().year
    YEAR_CHOICE = [(i, i) for i in range(This_Year-1, This_Year+1)]
    MONTH_CHOICE = [(i, i) for i in range(1, 13)]
    license_id = models.ForeignKey(Car)
    timestamp = models.DateTimeField(auto_now_add=True)
    year = models.IntegerField(choices=YEAR_CHOICE)
    month = models.IntegerField(choices=MONTH_CHOICE)
    fuel_consumed = models.FloatField()
    cost = models.FloatField()
    km = models.FloatField()

    class Meta:
            unique_together = ("license_id", "year", "month")

    def __unicode__(self):  # Python 3: def __str__(self):
        return str(self.year) + " " + str(self.month)


class CarOwnership(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    license_id = models.ForeignKey(Car)
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Owner)
    start_date = models.DateField(default=datetime.today())
    end_date = models.DateField(null=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.license_id + " " + self.owner + " "
        + self.start_date + " " + self.end_date


class TreatmentType(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=400)
    is_planned = models.BooleanField(default=False)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name


class Treatment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    license_id = models.ForeignKey(Car)
    treatmenttype = models.ForeignKey(TreatmentType)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    date = models.DateField(auto_now_add=True)
    km_read = models.IntegerField()
    vendor = models.CharField(max_length=30)
    cost = models.FloatField()
    remarks = models.TextField(null=True, blank=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.license_id + " " + self.date + " " + self.cost


class KMRead(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    CHOICES = (('percise', 'Percise'), ('estimate', 'Estimate'))
    license_id = models.ForeignKey(Car)
    reported_at = models.DateTimeField(default=datetime.now, blank=True)
    report_type = models.CharField(max_length=10, choices=CHOICES)
    # precise is a real time, smartphnoe based read, estimate is less accurate.
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField()
    comment = models.CharField(max_length=400, blank=True, null=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return str(self.comment)


class City(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name


class Parking(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    license_id = models.ForeignKey(Car)
    timestamp = models.DateTimeField(auto_now_add=True)
    city = models.ForeignKey(City)
    date = models.DateField(default=datetime.today())
    cost = models.FloatField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.license_id + " " + self.city


class Road6(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    license_id = models.ForeignKey(Car)
    timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateField(default=datetime.today())
    cost = models.FloatField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.license_id + " " + str(self.date)


class Accident(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    license_id = models.ForeignKey(Car)
    driver = models.CharField(max_length=50, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateField(default=datetime.today())
    cost = models.FloatField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='accidents/%Y/%m/%d',
                              default='accidents/None/no-img.jpg')

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.driver

#TODO:
# 1. accidents history.
# 2. treatment history.
