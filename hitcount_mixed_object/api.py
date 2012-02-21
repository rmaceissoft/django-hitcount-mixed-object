"""
public interface to use for developers
"""
from hitcount_mixed_object.backends import get_backend


def push_hit(object, related_objects=None, hit_count=1):
    backend = get_backend()
    backend.push_hit(object, related_objects, hit_count)


def get_hit_count(object, related_objects=None):
    backend = get_backend()
    return backend.get_hit_count(object, related_objects)


def get_mixed_objects(filters=None, limit=None, offset=None, order_by=None):
    backend = get_backend()
    return backend.get_mixed_objects(filters, limit, offset, order_by)


