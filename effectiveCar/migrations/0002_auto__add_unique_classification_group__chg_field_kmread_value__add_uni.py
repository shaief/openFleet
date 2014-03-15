# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Classification', fields ['group']
        db.create_unique(u'effectiveCar_classification', ['group'])


        # Changing field 'KMRead.value'
        db.alter_column(u'effectiveCar_kmread', 'value', self.gf('django.db.models.fields.IntegerField')())
        # Adding unique constraint on 'Department', fields ['name']
        db.create_unique(u'effectiveCar_department', ['name'])

        # Deleting field 'Treatment.reported_at'
        db.delete_column(u'effectiveCar_treatment', 'reported_at')

        # Adding field 'Treatment.timestamp'
        db.add_column(u'effectiveCar_treatment', 'timestamp',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Adding field 'Treatment.km_read'
        db.add_column(u'effectiveCar_treatment', 'km_read',
                      self.gf('django.db.models.fields.IntegerField')(default=datetime.datetime(2014, 3, 14, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'Department', fields ['name']
        db.delete_unique(u'effectiveCar_department', ['name'])

        # Removing unique constraint on 'Classification', fields ['group']
        db.delete_unique(u'effectiveCar_classification', ['group'])


        # Changing field 'KMRead.value'
        db.alter_column(u'effectiveCar_kmread', 'value', self.gf('django.db.models.fields.FloatField')())
        # Adding field 'Treatment.reported_at'
        db.add_column(u'effectiveCar_treatment', 'reported_at',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True),
                      keep_default=False)

        # Deleting field 'Treatment.timestamp'
        db.delete_column(u'effectiveCar_treatment', 'timestamp')

        # Deleting field 'Treatment.km_read'
        db.delete_column(u'effectiveCar_treatment', 'km_read')


    models = {
        u'effectiveCar.accident': {
            'Meta': {'object_name': 'Accident'},
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 14, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'driver': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'accidents/None/no-img.jpg'", 'max_length': '100'}),
            'license_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Car']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'effectiveCar.car': {
            'Meta': {'object_name': 'Car'},
            'car_model': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'classification': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Classification']"}),
            'color': ('django.db.models.fields.CharField', [], {'default': "'white'", 'max_length': '20'}),
            'current_owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Owner']"}),
            'date_of_purchase': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insurance_renewal_date': ('django.db.models.fields.DateField', [], {}),
            'km_read_at_purchase': ('django.db.models.fields.IntegerField', [], {}),
            'license_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '9'}),
            'license_renewal_date': ('django.db.models.fields.DateField', [], {}),
            'maker': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'production_year': ('django.db.models.fields.SmallIntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Active'", 'max_length': '30'})
        },
        u'effectiveCar.carownership': {
            'Meta': {'object_name': 'CarOwnership'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Car']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Owner']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 14, 0, 0)'})
        },
        u'effectiveCar.carstatus': {
            'Meta': {'object_name': 'CarStatus'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 14, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Car']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'effectiveCar.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'effectiveCar.classification': {
            'Meta': {'object_name': 'Classification'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'effectiveCar.department': {
            'Meta': {'object_name': 'Department'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'effectiveCar.kmread': {
            'Meta': {'object_name': 'KMRead'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Car']"}),
            'report_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'reported_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'effectiveCar.manager': {
            'Meta': {'object_name': 'Manager'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'effectiveCar.monthlyrecord': {
            'Meta': {'object_name': 'MonthlyRecord'},
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'fuel_consumed': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'km': ('django.db.models.fields.FloatField', [], {}),
            'license_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Car']"}),
            'month': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'effectiveCar.owner': {
            'Meta': {'object_name': 'Owner'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Department']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'owners/None/no-img.jpg'", 'max_length': '100'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'license_category': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'license_renewal_date': ('django.db.models.fields.DateField', [], {}),
            'manager_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Manager']"})
        },
        u'effectiveCar.parking': {
            'Meta': {'object_name': 'Parking'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.City']"}),
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 14, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Car']"})
        },
        u'effectiveCar.road6': {
            'Meta': {'object_name': 'Road6'},
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 14, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Car']"})
        },
        u'effectiveCar.treatment': {
            'Meta': {'object_name': 'Treatment'},
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'km_read': ('django.db.models.fields.IntegerField', [], {}),
            'license_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Car']"}),
            'remarks': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'treatmenttype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.TreatmentType']"}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'effectiveCar.treatmenttype': {
            'Meta': {'object_name': 'TreatmentType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_planned': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        }
    }

    complete_apps = ['effectiveCar']