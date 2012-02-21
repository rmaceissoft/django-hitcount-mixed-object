from hitcount_mixed_object import conf as settings
from django.utils.importlib import import_module


class InvalidBackend(Exception):
    pass


_connected = False

def is_connected():
    """ public method to get connection status
    """
    global _connected
    return _connected


def mark_as_connected():
    """ public method to set as True connection status
    """
    global _connected
    _connected = True

def get_backend():
    try:
        backend = import_module(settings.HITCOUNT_MIXED_OBJECT_BACKEND)
    except:
        raise InvalidBackend("Could not load '%s' as a backend" % settings.HITCOUNT_MIXED_OBJECT_BACKEND )

    if not is_connected():
        backend.init_connection()
        mark_as_connected()

    return backend
