# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CreadocReport'
        db.create_table('creadoc_report', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('shortname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('root_source', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('template', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('begin', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(1, 1, 1, 0, 0))),
            ('end', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(9999, 12, 31, 0, 0))),
        ))
        db.send_create_signal('creadoc', ['CreadocReport'])


    def backwards(self, orm):
        # Deleting model 'CreadocReport'
        db.delete_table('creadoc_report')


    models = {
        'creadoc.creadocreport': {
            'Meta': {'object_name': 'CreadocReport', 'db_table': "'creadoc_report'"},
            'begin': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(1, 1, 1, 0, 0)'}),
            'end': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(9999, 12, 31, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'root_source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'shortname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'template': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['creadoc']