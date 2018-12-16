import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'rss.settings'
django.setup()