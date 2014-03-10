from .base import *

ENV = 'heroku'

DEBUG = False
TEMPLATE_DEBUG = DEBUG
DEBUG_TOOLBAR_PATCH_SETTINGS = False

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

ALLOWED_HOSTS = ['openfleet.herokuapp.com']
