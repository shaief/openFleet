from .base import *

ENV = 'heroku'

DEBUG = False
TEMPLATE_DEBUG = DEBUG
DEBUG_TOOLBAR_PATCH_SETTINGS = False

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

ALLOWED_HOSTS = ['openfleet.herokuapp.com']

# copied from openAir dokku.py:
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = environ.get('S3_KEY')
AWS_SECRET_ACCESS_KEY = environ.get('S3_SECRET')
AWS_STORAGE_BUCKET_NAME = environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = False
AWS_PRELOAD_METADATA = True
AWS_IS_GZIPPED = True
AWS_S3_SECURE_URLS = False
AWS_HEADERS = {
    # 'Cache-Control': 'public, max-age=86400',
}
STATIC_URL = 'https://{}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)
