# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'New'
        db.create_table(u'news_new', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('categories', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['news.NewCategory'])),
        ))
        db.send_create_signal(u'news', ['New'])

        # Adding model 'NewCategory'
        db.create_table(u'news_newcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'news', ['NewCategory'])

        # Adding model 'Language'
        db.create_table(u'news_language', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'news', ['Language'])


    def backwards(self, orm):
        # Deleting model 'New'
        db.delete_table(u'news_new')

        # Deleting model 'NewCategory'
        db.delete_table(u'news_newcategory')

        # Deleting model 'Language'
        db.delete_table(u'news_language')


    models = {
        u'news.language': {
            'Meta': {'object_name': 'Language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'news.new': {
            'Meta': {'object_name': 'New'},
            'categories': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['news.NewCategory']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'news.newcategory': {
            'Meta': {'object_name': 'NewCategory'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['news']