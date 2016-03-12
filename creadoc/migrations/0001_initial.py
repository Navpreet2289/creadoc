# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CreadocReport'
        db.create_table('creadoc_report', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('guid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'creadoc', ['CreadocReport'])


    def backwards(self, orm):
        # Deleting model 'CreadocReport'
        db.delete_table('creadoc_report')


    models = {
        u'creadoc.creadocreport': {
            'Meta': {'object_name': 'CreadocReport', 'db_table': "'creadoc_report'"},
            'guid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['creadoc']