from .base import *

ENV = 'heroku'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

ALLOWED_HOSTS = ['pacific-sands-5085.herokuapp.com']
