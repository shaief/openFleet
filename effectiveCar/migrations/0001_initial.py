# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Owner'
        db.create_table(u'effectiveCar_owner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
        ))
        db.send_create_signal(u'effectiveCar', ['Owner'])

        # Adding model 'Classification'
        db.create_table(u'effectiveCar_classification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'effectiveCar', ['Classification'])

        # Adding model 'Car'
        db.create_table(u'effectiveCar_car', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('license_id', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('classification', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.Classification'])),
            ('car_model', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('maker', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('production_year', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('date_of_purchase', self.gf('django.db.models.fields.DateField')()),
            ('license_renewal_date', self.gf('django.db.models.fields.DateField')()),
            ('insurance_renewal_date', self.gf('django.db.models.fields.DateField')()),
            ('current_owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.Owner'])),
        ))
        db.send_create_signal(u'effectiveCar', ['Car'])

        # Adding model 'MonthlyRecord'
        db.create_table(u'effectiveCar_monthlyrecord', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('car', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.Car'])),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('month', self.gf('django.db.models.fields.IntegerField')()),
            ('fuel_consumed', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'effectiveCar', ['MonthlyRecord'])

        # Adding model 'CarOwnership'
        db.create_table(u'effectiveCar_carownership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('car', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.Car'])),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.Owner'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal(u'effectiveCar', ['CarOwnership'])

        # Adding model 'TreatmentType'
        db.create_table(u'effectiveCar_treatmenttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('is_planned', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'effectiveCar', ['TreatmentType'])

        # Adding model 'Treatment'
        db.create_table(u'effectiveCar_treatment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('car', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.Car'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('treatment_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('cost', self.gf('django.db.models.fields.FloatField')()),
            ('remarks', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'effectiveCar', ['Treatment'])

        # Adding model 'KMRead'
        db.create_table(u'effectiveCar_kmread', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('car', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.Car'])),
            ('reported_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('report_type', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('value', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'effectiveCar', ['KMRead'])


    def backwards(self, orm):
        # Deleting model 'Owner'
        db.delete_table(u'effectiveCar_owner')

        # Deleting model 'Classification'
        db.delete_table(u'effectiveCar_classification')

        # Deleting model 'Car'
        db.delete_table(u'effectiveCar_car')

        # Deleting model 'MonthlyRecord'
        db.delete_table(u'effectiveCar_monthlyrecord')

        # Deleting model 'CarOwnership'
        db.delete_table(u'effectiveCar_carownership')

        # Deleting model 'TreatmentType'
        db.delete_table(u'effectiveCar_treatmenttype')

        # Deleting model 'Treatment'
        db.delete_table(u'effectiveCar_treatment')

        # Deleting model 'KMRead'
        db.delete_table(u'effectiveCar_kmread')


    models = {
        u'effectiveCar.car': {
            'Meta': {'object_name': 'Car'},
            'car_model': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'classification': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Classification']"}),
            'current_owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Owner']"}),
            'date_of_purchase': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insurance_renewal_date': ('django.db.models.fields.DateField', [], {}),
            'license_id': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'license_renewal_date': ('django.db.models.fields.DateField', [], {}),
            'maker': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'production_year': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'effectiveCar.carownership': {
            'Meta': {'object_name': 'CarOwnership'},
            'car': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Car']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Owner']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'effectiveCar.classification': {
            'Meta': {'object_name': 'Classification'},
            'group': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'effectiveCar.kmread': {
            'Meta': {'object_name': 'KMRead'},
            'car': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Car']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report_type': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'reported_at': ('django.db.models.fields.DateTimeField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'effectiveCar.monthlyrecord': {
            'Meta': {'object_name': 'MonthlyRecord'},
            'car': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Car']"}),
            'fuel_consumed': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'effectiveCar.owner': {
            'Meta': {'object_name': 'Owner'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'effectiveCar.treatment': {
            'Meta': {'object_name': 'Treatment'},
            'car': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Car']"}),
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {}),
            'treatment_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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