import dj_database_url
from .base import *


SECRET_KEY = '$#wm#rn#kq&k46_by+vdday0l+u#a_mhq)j^($y(owehw1+*h8'
DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {'default': dj_database_url.config(conn_max_age=600, ssl_require=False)}
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
