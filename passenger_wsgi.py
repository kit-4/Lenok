# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1208057/data/www/lenok.space/AngelinaLenok')
sys.path.insert(1, '/var/www/u1208057/data/djangoenv/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'AngelinaLenok.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
