from .settings import *

import pymysql

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'alipay',
        'USER': 'root',
        'PASSWORD': 'Quattro!',
    }
}

STATIC_ROOT = '/var/alipay/static/'
MEDIA_ROOT = '/var/alipay/media/'

DOMAIN = 'https://zhuti.metatype.cn'


DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800