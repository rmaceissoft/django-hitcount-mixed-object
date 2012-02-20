from django.conf import settings

HITCOUNT_MIXED_OBJECT_BACKEND = getattr(settings, 'HITCOUNT_MIXED_OBJECT_BACKEND', 'hitcount_mmixed_object.backends.mongodb')
