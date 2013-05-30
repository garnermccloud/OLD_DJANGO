# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Marginal_Duration'
        db.create_table('Listigain_marginal_duration', (
            ('time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 5, 27, 18, 52, 16, 874000))),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Listigain.Task'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marginal_duration', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal('Listigain', ['Marginal_Duration'])

        # Deleting field 'Task.duration_max'
        db.delete_column('Listigain_task', 'duration_max')

        # Adding field 'Task.complete_percentage'
        db.add_column('Listigain_task', 'complete_percentage', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting model 'Marginal_Duration'
        db.delete_table('Listigain_marginal_duration')

        # Adding field 'Task.duration_max'
        db.add_column('Listigain_task', 'duration_max', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4), keep_default=False)

        # Deleting field 'Task.complete_percentage'
        db.delete_column('Listigain_task', 'complete_percentage')
    
    
    models = {
        'Listigain.end_time': {
            'Meta': {'object_name': 'End_Time'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Listigain.Task']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 27, 18, 52, 16, 873000)'})
        },
        'Listigain.marginal_duration': {
            'Meta': {'object_name': 'Marginal_Duration'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marginal_duration': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Listigain.Task']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 27, 18, 52, 16, 874000)'})
        },
        'Listigain.start_time': {
            'Meta': {'object_name': 'Start_Time'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Listigain.Task']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 27, 18, 52, 16, 870000)'})
        },
        'Listigain.task': {
            'Meta': {'object_name': 'Task'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'complete_percentage': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date_due': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 27, 18, 52, 16, 866000)'}),
            'duration_est': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'enjoyment': ('django.db.models.fields.IntegerField', [], {'default': '4', 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.IntegerField', [], {'default': '4', 'max_length': '1'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 27, 18, 52, 16, 868000)', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 27, 18, 52, 17, 44000)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 27, 18, 52, 17, 43000)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['Listigain']
