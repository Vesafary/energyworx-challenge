from .default import *

DATABASES["default"] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': ':memory:',
    'TEST_CHARSET': 'UTF8',
    'TEST_NAME': ':memory:',
}
