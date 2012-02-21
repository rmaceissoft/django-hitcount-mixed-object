from hitcount_mixed_object import conf as settings
from django.utils.importlib import import_module


class InvalidBackend(Exception):
    pass


_connected = False

def get_backend():
    try:
        backend = import_module(settings.HITCOUNT_MIXED_OBJECT_BACKEND)
    except:
        raise InvalidBackend("Could not load '%s' as a backend" % settings.HITCOUNT_MIXED_OBJECT_BACKEND )

    global _connected
    if not _connected:
        backend.init_connection()
        _connected = True


    return backend
