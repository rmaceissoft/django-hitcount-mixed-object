from mongoengine import *
from django.contrib.contenttypes.models import ContentType
from hitcount_mixed_object import conf


class MixedObject(Document):
    content_type_id = StringField(required=True)
    object_id = StringField(required=True)

    related_objects = ListField(StringField())

    hit_count = IntField()


# short cuts method
def get_tuple_object(object):
    ct = ContentType.objects.get_for_model(object)
    return str(ct.pk), str(object.pk)


def get_related_objects_sorted(related_objects):
    if related_objects:
        sorted_list = sorted(related_objects, key=lambda obj : obj.pk)
        return [str(item.pk) for item in sorted_list]
    else:
        return []


# backend methods
def init_connection():
    connection_settings = dict(
        host = conf.MONGO_DB_HOST,
        port = conf.MONGO_DB_PORT,
        db = conf.MONGO_DB_NAME,
        username = conf.MONGO_DB_USERNAME,
        password = conf.MONGO_DB_PASSWORD
    )
    connect(**connection_settings)


def push_hit(object, related_objects, hit_count=1):
    content_type_id, object_id = get_tuple_object(object)
    related_objects_id = get_related_objects_sorted(related_objects)
    try:
        mixed_object = MixedObject.objects(
            content_type_id = content_type_id,
            object_id = object_id,
            related_objects = related_objects_id
        ).get()
    except MixedObject.DoesNotExist:
        mixed_object = MixedObject(
            content_type_id = content_type_id,
            object_id = object_id,
            related_objects = related_objects_id
        )
        mixed_object.hit_count = hit_count
        mixed_object.save()
    else:
        mixed_object.hit_count += hit_count
        mixed_object.save()


def get_hit_count(object, related_objects):
    content_type_id, object_id = get_tuple_object(object)
    related_objects_id = get_related_objects_sorted(related_objects)
    try:
        mixed_object = MixedObject.objects(
            content_type_id = content_type_id,
            object_id = object_id,
            related_objects = related_objects_id
        ).get()
    except MixedObject.DoesNotExist:
        return 0
    else:
        return mixed_object.hit_count


def clear_hitcount_collection():
    """ clear all elements from collection into db related to backend
    """
    MixedObject.objects.delete()