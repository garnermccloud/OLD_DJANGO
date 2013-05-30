# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Start_Time'
        db.create_table('Listigain_start_time', (
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Listigain.Task'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2013, 5, 19))),
        ))
        db.send_create_signal('Listigain', ['Start_Time'])

        # Adding model 'End_Time'
        db.create_table('Listigain_end_time', (
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Listigain.Task'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2013, 5, 19))),
        ))
        db.send_create_signal('Listigain', ['End_Time'])

        # Deleting field 'Task.priority'
        db.delete_column('Listigain_task', 'priority')

        # Deleting field 'Task.skip'
        db.delete_column('Listigain_task', 'skip')

        # Deleting field 'Task.difficulty'
        db.delete_column('Listigain_task', 'difficulty')

        # Deleting field 'Task.time'
        db.delete_column('Listigain_task', 'time')

        # Adding field 'Task.date_due'
        db.add_column('Listigain_task', 'date_due', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2013, 5, 19)), keep_default=False)

        # Adding field 'Task.importance'
        db.add_column('Listigain_task', 'importance', self.gf('django.db.models.fields.IntegerField')(default=4, max_length=1), keep_default=False)

        # Adding field 'Task.time_created'
        db.add_column('Listigain_task', 'time_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2013, 5, 19)), keep_default=False)

        # Adding field 'Task.enjoyment'
        db.add_column('Listigain_task', 'enjoyment', self.gf('django.db.models.fields.IntegerField')(default=4, max_length=1), keep_default=False)

        # Adding field 'Task.duration_max'
        db.add_column('Listigain_task', 'duration_max', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4), keep_default=False)

        # Adding field 'Task.duration_est'
        db.add_column('Listigain_task', 'duration_est', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting model 'Start_Time'
        db.delete_table('Listigain_start_time')

        # Deleting model 'End_Time'
        db.delete_table('Listigain_end_time')

        # Adding field 'Task.priority'
        db.add_column('Listigain_task', 'priority', self.gf('django.db.models.fields.CharField')(default=1, max_length=3), keep_default=False)

        # Adding field 'Task.skip'
        db.add_column('Listigain_task', 'skip', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True), keep_default=False)

        # Adding field 'Task.difficulty'
        db.add_column('Listigain_task', 'difficulty', self.gf('django.db.models.fields.CharField')(default=1, max_length=3), keep_default=False)

        # Adding field 'Task.time'
        db.add_column('Listigain_task', 'time', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Deleting field 'Task.date_due'
        db.delete_column('Listigain_task', 'date_due')

        # Deleting field 'Task.importance'
        db.delete_column('Listigain_task', 'importance')

        # Deleting field 'Task.time_created'
        db.delete_column('Listigain_task', 'time_created')

        # Deleting field 'Task.enjoyment'
        db.delete_column('Listigain_task', 'enjoyment')

        # Deleting field 'Task.duration_max'
        db.delete_column('Listigain_task', 'duration_max')

        # Deleting field 'Task.duration_est'
        db.delete_column('Listigain_task', 'duration_est')
    
    
    models = {
        'Listigain.end_time': {
            'Meta': {'object_name': 'End_Time'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Listigain.Task']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2013, 5, 19)'})
        },
        'Listigain.start_time': {
            'Meta': {'object_name': 'Start_Time'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Listigain.Task']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2013, 5, 19)'})
        },
        'Listigain.task': {
            'Meta': {'object_name': 'Task'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date_due': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2013, 5, 19)'}),
            'duration_est': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'duration_max': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '4'}),
            'enjoyment': ('django.db.models.fields.IntegerField', [], {'default': '4', 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.IntegerField', [], {'default': '4', 'max_length': '1'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.date(2013, 5, 19)'}),
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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 19, 19, 1, 0, 588000)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 19, 19, 1, 0, 588000)'}),
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
