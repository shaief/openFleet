# -*- coding: utf-8 -*-

import os
import csv

from django.core.management.base import BaseCommand, CommandError

from openFleet.settings.base import BASE_DIR
from effectiveCar.models import Car, Owner


class Command(BaseCommand):
    help = 'Fill the DB with cars, owners, and some data to play with' \
           'from "cars.csv"'

    def handle(self, *args, **options):
        path = os.path.join(BASE_DIR,
                            'docs',
                            'cars.csv')
        with open(path) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if reader.line_num != 1:  # skip first row
                    c, created = Car.objects.get_or_create(
                        name=row[2])
                    Owner.objects.get_or_create(
                        name=row[1], car=c, is_knesset_member=True,
                        image_url=row[4]
                    )

        # adding independent party to the DB
        #Party.objects.get_or_create(name=u'לא משוייך')