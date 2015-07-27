# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Car'
        db.create_table('demo_car', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marka', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('seria', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('cars', ['Car'])


    def backwards(self, orm):
        # Deleting model 'Car'
        db.delete_table('demo_car')


    models = {
        'cars.car': {
            'Meta': {'object_name': 'Car', 'db_table': "'demo_car'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marka': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'seria': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['cars']