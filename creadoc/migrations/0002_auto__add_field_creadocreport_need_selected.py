# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CreadocReport.need_selected'
        db.add_column('creadoc_report', 'need_selected',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CreadocReport.need_selected'
        db.delete_column('creadoc_report', 'need_selected')


    models = {
        u'creadoc.creadocreport': {
            'Meta': {'object_name': 'CreadocReport', 'db_table': "'creadoc_report'"},
            'begin': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(1, 1, 1, 0, 0)'}),
            'end': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(9999, 12, 31, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'need_selected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'root_source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'shortname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'template': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['creadoc']