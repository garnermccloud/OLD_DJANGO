import os
import sys	
sys.path.append('~/public/procrastigain.com/public/procrastigain/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Procrastigain.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()