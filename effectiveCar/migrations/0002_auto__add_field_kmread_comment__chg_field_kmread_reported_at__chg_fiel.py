# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'KMRead.comment'
        db.add_column(u'effectiveCar_kmread', 'comment',
                      self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True),
                      keep_default=False)


        # Changing field 'KMRead.reported_at'
        db.alter_column(u'effectiveCar_kmread', 'reported_at', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'KMRead.timestamp'
        db.alter_column(u'effectiveCar_kmread', 'timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Adding field 'Car.color'
        db.add_column(u'effectiveCar_car', 'color',
                      self.gf('django.db.models.fields.CharField')(default='white', max_length=20),
                      keep_default=False)

        # Adding field 'Car.status'
        db.add_column(u'effectiveCar_car', 'status',
                      self.gf('django.db.models.fields.CharField')(default='Active', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'KMRead.comment'
        db.delete_column(u'effectiveCar_kmread', 'comment')


        # Changing field 'KMRead.reported_at'
        db.alter_column(u'effectiveCar_kmread', 'reported_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'KMRead.timestamp'
        db.alter_column(u'effectiveCar_kmread', 'timestamp', self.gf('django.db.models.fields.DateTimeField')())
        # Deleting field 'Car.color'
        db.delete_column(u'effectiveCar_car', 'color')

        # Deleting field 'Car.status'
        db.delete_column(u'effectiveCar_car', 'status')


    models = {
        u'effectiveCar.car': {
            'Meta': {'object_name': 'Car'},
            'car_model': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'classification': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Classification']"}),
            'color': ('django.db.models.fields.CharField', [], {'default': "'white'", 'max_length': '20'}),
            'current_owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Owner']"}),
            'date_of_purchase': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insurance_renewal_date': ('django.db.models.fields.DateField', [], {}),
            'license_id': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'license_renewal_date': ('django.db.models.fields.DateField', [], {}),
            'maker': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'production_year': ('django.db.models.fields.SmallIntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Active'", 'max_length': '30'})
        },
        u'effectiveCar.carownership': {
            'Meta': {'object_name': 'CarOwnership'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Car']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Owner']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'effectiveCar.classification': {
            'Meta': {'object_name': 'Classification'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'effectiveCar.kmread': {
            'Meta': {'object_name': 'KMRead'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Car']"}),
            'report_type': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'reported_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'effectiveCar.monthlyrecord': {
            'Meta': {'object_name': 'MonthlyRecord'},
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'fuel_consumed': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Car']"}),
            'month': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'effectiveCar.owner': {
            'Meta': {'object_name': 'Owner'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_renewal_date': ('django.db.models.fields.DateField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'effectiveCar.treatment': {
            'Meta': {'object_name': 'Treatment'},
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Car']"}),
            'remarks': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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