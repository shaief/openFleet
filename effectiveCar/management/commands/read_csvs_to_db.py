# coding=utf-8

import os
import csv
from django.core.management.base import BaseCommand
from openFleet.settings.base import PROJECT_DIR
from effectiveCar.models import (Car, Classification,
                                 Owner, Department, Manager)
from django.db.models import Q


class Command(BaseCommand):
    help = 'Run it to fill the DB with parameters information' \
           'from "cars.csv"'

    def handle(self, *args, **options):
    # def handle(self, *args, **options):
        print "Adding cars to DB from CSV"
        path = os.path.join(PROJECT_DIR,
                            'CSVs',
                            'cars.csv')
        with open(path) as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                if reader.line_num != 1:  # skip first row
                    try:
                        cl = Classification.objects.get(group=row[2])
                        cl.description = row[2]
                        print "updated field: " + cl.group
                    except Classification.DoesNotExist:
                        print "Add classification: " + row[2]
                        cl = Classification.objects.create(
                            group=row[2],
                            description=row[2],
                        )
                    cl.save()
                    try:
                        d = Department.objects.get(name=row[14])
                        print "updated department field: " + d.name
                    except Department.DoesNotExist:
                        print "Add Department: " + row[14]
                        d = Department.objects.create(
                            name=row[14],
                        )
                    d.save
                    try:
                        m = Manager.objects.get(name=row[15])
                    except Manager.DoesNotExist:
                        print "Add Manager: " + row[15]
                        m = Manager.objects.create(
                            name=row[15],
                        )
                    m.save
                    name_split = row[11].split(' ')
                    try:
                        o = Owner.objects.get(Q(first_name=name_split[0]) &
                                              Q(last_name=name_split[1]))
                    except Owner.DoesNotExist:
                        print "Add Owner: " + row[11]
                        o = Owner.objects.create(
                            first_name=name_split[0],
                            last_name=name_split[1],
                            license_renewal_date=row[13],
                            department=Department.objects.get(name=row[14]),
                            manager_name=Manager.objects.get(name=row[15]),
                        )
                    o.save
                    try:
                        c = Car.objects.get(license_id=row[0])
                        c.nickname = row[1]
                        c.classification = Classification.objects.get(
                            group=row[2])
                        c.car_model = row[3]
                        c.maker = row[4]
                        c.color = row[5]
                        c.production_year = row[6]
                        c.date_of_purchase = row[7]
                        c.km_read_at_purchase = row[8]
                        c.license_renewal_date = row[9]
                        c.insurance_renewal_date = row[10]
                        c.current_owner = Owner.objects.get(
                            Q(first_name=name_split[0]) &
                            Q(last_name=name_split[1]))
                        c.status = row[12]
                    except Car.DoesNotExist:
                        c = Car.objects.create(
                            license_id=row[0],
                            classification=Classification.objects.get(
                                group=row[2]),
                            car_model=row[3],
                            maker=row[4],
                            color=row[5],
                            production_year=row[6],
                            date_of_purchase=row[7],
                            km_read_at_purchase=row[8],
                            license_renewal_date=row[9],
                            insurance_renewal_date=row[10],
                            current_owner=Owner.objects.get(
                                Q(first_name=name_split[0]) &
                                Q(last_name=name_split[1])),
                            status=row[12],
                        )
                    print "updated field: " + c.license_id
                    c.save()
