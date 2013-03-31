import os
import sys

sys.path.append('/home/gmccloud/public/procrastigain.com/public/Procrastigain')

os.environ['PYTHON_EGG_CACHE'] = '/home/gmccloud/public/procrastigain.com/public/.python-egg'

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()