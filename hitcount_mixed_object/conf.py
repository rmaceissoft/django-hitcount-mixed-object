from django.conf import settings

HITCOUNT_MIXED_OBJECT_BACKEND = getattr(settings, 'HITCOUNT_MIXED_OBJECT_BACKEND', 'hitcount_mixed_object.backends.mongodb')


#settings related to mongo backend

MONGO_DB_HOST = getattr(settings, 'MONGO_DB_HOST', 'localhost')
MONGO_DB_PORT = getattr(settings, 'MONGO_DB_PORT', 27017)
MONGO_DB_NAME = getattr(settings, 'MONGO_DB_NAME', 'mixed_object')
MONGO_DB_USERNAME = getattr(settings, 'MONGO_DB_USERNAME', None)
MONGO_DB_PASSWORD = getattr(settings, 'MONGO_DB_PASSWORD', None)
