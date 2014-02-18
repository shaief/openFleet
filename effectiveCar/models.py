from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(null=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name + " " + self.email


class Classification(models.Model):
    group = models.CharField(max_length=30)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.group


class Car(models.Model):
    license_id = models.CharField(max_length=9)
    classification = models.ForeignKey(Classification)
    car_model = models.CharField(max_length=20)
    maker = models.CharField(max_length=20)
    production_year = models.SmallIntegerField()
    date_of_purchase = models.DateField()
    license_renewal_date = models.DateField()
    insurance_renewal_date = models.DateField()
    current_owner = models.ForeignKey(Owner)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.license_id


class MonthlyRecord(models.Model):
    license_id = models.ForeignKey(Car)
    year = models.IntegerField()
    month = models.IntegerField()
    fuel_consumed = models.FloatField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return str(self.year) + " " + str(self.month)


class CarOwnership(models.Model):
    license_id = models.ForeignKey(Car)
    owner = models.ForeignKey(Owner)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.license_id + " " + self.owner + " "
        + self.start_date + " " + self.end_date


class TreatmentType(models.Model):
    name = models.CharField(max_length=400)
    is_planned = models.BooleanField(default=False)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name


class Treatment(models.Model):
    license_id = models.ForeignKey(Car)
    date = models.DateField()
    treatment_type = models.CharField(max_length=50)
    vendor = models.CharField(max_length=30)
    cost = models.FloatField()
    remarks = models.TextField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.license_id + " " + date + " " + cost


class KMRead(models.Model):
    license_id = models.ForeignKey(Car)
    reported_at = models.DateTimeField()
    report_type = models.CharField(max_length=8)  # precise / estimate
    # precise is a real time, smartphnoe based read, estimate is less accurate.
    timestamp = models.DateTimeField()  # if time is unknown, use 12:00
    value = models.FloatField()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.license_id + " " + reported_at + " " + value
