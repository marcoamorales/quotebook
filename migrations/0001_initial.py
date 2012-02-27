# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Quote'
        db.create_table('quotebook_quote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('quotebook', ['Quote'])

        # Adding model 'Book'
        db.create_table('quotebook_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quote', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quotebook.Quote'])),
        ))
        db.send_create_signal('quotebook', ['Book'])


    def backwards(self, orm):
        
        # Deleting model 'Quote'
        db.delete_table('quotebook_quote')

        # Deleting model 'Book'
        db.delete_table('quotebook_book')


    models = {
        'quotebook.book': {
            'Meta': {'object_name': 'Book'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quote': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quotebook.Quote']"})
        },
        'quotebook.quote': {
            'Meta': {'object_name': 'Quote'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['quotebook']
