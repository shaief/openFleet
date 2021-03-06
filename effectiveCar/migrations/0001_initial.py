# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Department'
        db.create_table(u'effectiveCar_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'effectiveCar', ['Department'])

        # Adding model 'Manager'
        db.create_table(u'effectiveCar_manager', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
        ))
        db.send_create_signal(u'effectiveCar', ['Manager'])

        # Adding model 'Owner'
        db.create_table(u'effectiveCar_owner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
            ('license_category', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('license_renewal_date', self.gf('django.db.models.fields.DateField')()),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.Department'])),
            ('manager_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.Manager'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='owners/None/no-img.jpg', max_length=100)),
        ))
        db.send_create_signal(u'effectiveCar', ['Owner'])

        # Adding unique constraint on 'Owner', fields ['first_name', 'last_name']
        db.create_unique(u'effectiveCar_owner', ['first_name', 'last_name'])

        # Adding model 'Classification'
        db.create_table(u'effectiveCar_classification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'effectiveCar', ['Classification'])

        # Adding model 'Car'
        db.create_table(u'effectiveCar_car', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('license_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=9)),
            ('classification', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.Classification'])),
            ('car_model', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('maker', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('color', self.gf('django.db.models.fields.CharField')(default='white', max_length=20)),
            ('production_year', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('date_of_purchase', self.gf('django.db.models.fields.DateField')()),
            ('km_read_at_purchase', self.gf('django.db.models.fields.IntegerField')()),
            ('license_renewal_date', self.gf('django.db.models.fields.DateField')()),
            ('insurance_renewal_date', self.gf('django.db.models.fields.DateField')()),
            ('current_owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.Owner'])),
            ('status', self.gf('django.db.models.fields.CharField')(default='Active', max_length=30)),
        ))
        db.send_create_signal(u'effectiveCar', ['Car'])

        # Adding model 'CarStatus'
        db.create_table(u'effectiveCar_carstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('license_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.Car'])),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 3, 27, 0, 0))),
        ))
        db.send_create_signal(u'effectiveCar', ['CarStatus'])

        # Adding model 'MonthlyRecord'
        db.create_table(u'effectiveCar_monthlyrecord', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('license_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.Car'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('month', self.gf('django.db.models.fields.IntegerField')()),
            ('fuel_consumed', self.gf('django.db.models.fields.FloatField')()),
            ('cost', self.gf('django.db.models.fields.FloatField')()),
            ('km', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'effectiveCar', ['MonthlyRecord'])

        # Adding unique constraint on 'MonthlyRecord', fields ['license_id', 'year', 'month']
        db.create_unique(u'effectiveCar_monthlyrecord', ['license_id_id', 'year', 'month'])

        # Adding model 'CarOwnership'
        db.create_table(u'effectiveCar_carownership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('license_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.Car'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.Owner'])),
            ('start_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 3, 27, 0, 0))),
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
            ('license_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.Car'])),
            ('treatmenttype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.TreatmentType'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('km_read', self.gf('django.db.models.fields.IntegerField')()),
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('cost', self.gf('django.db.models.fields.FloatField')()),
            ('remarks', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'effectiveCar', ['Treatment'])

        # Adding model 'KMRead'
        db.create_table(u'effectiveCar_kmread', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('license_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.Car'])),
            ('reported_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('report_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
        ))
        db.send_create_signal(u'effectiveCar', ['KMRead'])

        # Adding model 'City'
        db.create_table(u'effectiveCar_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'effectiveCar', ['City'])

        # Adding model 'Parking'
        db.create_table(u'effectiveCar_parking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('license_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.Car'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.City'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 3, 27, 0, 0))),
            ('cost', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'effectiveCar', ['Parking'])

        # Adding model 'Road6'
        db.create_table(u'effectiveCar_road6', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('license_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.Car'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 3, 27, 0, 0))),
            ('cost', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'effectiveCar', ['Road6'])

        # Adding model 'Accident'
        db.create_table(u'effectiveCar_accident', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('license_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['effectiveCar.Car'])),
            ('driver', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 3, 27, 0, 0))),
            ('cost', self.gf('django.db.models.fields.FloatField')()),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='accidents/None/no-img.jpg', max_length=100)),
        ))
        db.send_create_signal(u'effectiveCar', ['Accident'])


    def backwards(self, orm):
        # Removing unique constraint on 'MonthlyRecord', fields ['license_id', 'year', 'month']
        db.delete_unique(u'effectiveCar_monthlyrecord', ['license_id_id', 'year', 'month'])

        # Removing unique constraint on 'Owner', fields ['first_name', 'last_name']
        db.delete_unique(u'effectiveCar_owner', ['first_name', 'last_name'])

        # Deleting model 'Department'
        db.delete_table(u'effectiveCar_department')

        # Deleting model 'Manager'
        db.delete_table(u'effectiveCar_manager')

        # Deleting model 'Owner'
        db.delete_table(u'effectiveCar_owner')

        # Deleting model 'Classification'
        db.delete_table(u'effectiveCar_classification')

        # Deleting model 'Car'
        db.delete_table(u'effectiveCar_car')

        # Deleting model 'CarStatus'
        db.delete_table(u'effectiveCar_carstatus')

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

        # Deleting model 'City'
        db.delete_table(u'effectiveCar_city')

        # Deleting model 'Parking'
        db.delete_table(u'effectiveCar_parking')

        # Deleting model 'Road6'
        db.delete_table(u'effectiveCar_road6')

        # Deleting model 'Accident'
        db.delete_table(u'effectiveCar_accident')


    models = {
        u'effectiveCar.accident': {
            'Meta': {'object_name': 'Accident'},
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 27, 0, 0)'}),
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
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 27, 0, 0)'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'effectiveCar.carstatus': {
            'Meta': {'object_name': 'CarStatus'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 27, 0, 0)'}),
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
            'Meta': {'unique_together': "(('license_id', 'year', 'month'),)", 'object_name': 'MonthlyRecord'},
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'fuel_consumed': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'km': ('django.db.models.fields.FloatField', [], {}),
            'license_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Car']"}),
            'month': ('django.db.models.fields.IntegerField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'effectiveCar.owner': {
            'Meta': {'unique_together': "(('first_name', 'last_name'),)", 'object_name': 'Owner'},
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
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 27, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Car']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'effectiveCar.road6': {
            'Meta': {'object_name': 'Road6'},
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 27, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['effectiveCar.Car']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
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