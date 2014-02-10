from django.db import models


class Car(models.Model):
    license_id = models.CharField(max_length=9)
    current_owner = models.CharField(max_length=40, null=True, blank=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.license_id + " " + self.current_owner


class MonthlyRecord(models.Model):
    car = models.ForeignKey(Car)
    year = models.IntegerField()
    month = models.IntegerField()
    fuel_consumed = models.FloatField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.car + " " + self.year + " " + self.month


class Owner(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name


class CarOwnership(models.Model):
    car = models.ForeignKey(Car)
    owner = models.ForeignKey(Owner)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name


class TreatmentType(models.Model):
    name = models.CharField(max_length=400)
    is_planned = models.BooleanField(default=False)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name


class Treatment(models.Model):
    car = models.ForeignKey(Car)
    date = models.DateField()
    treatment_type = models.CharField(max_length=50)
    vendor = models.CharField(max_length=30)
    cost = models.FloatField()
    remarks = models.TextField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name


class KMRead(models.Model):
    car = models.ForeignKey(Car)
    report_type = models.CharField(max_length=8)  # precise / estimate
    # precise is a real time, smartphnoe based read, estimate is less accurate.
    timestamp = models.DateTimeField()  # if time is unknown, use 12:00
    value = models.FloatField()
    reported_at = models.DateTimeField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name
