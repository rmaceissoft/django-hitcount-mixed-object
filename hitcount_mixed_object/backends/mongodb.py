import logging
from mongoengine import *
from django.contrib.contenttypes.models import ContentType
from hitcount_mixed_object import conf


class MixedObject(Document):
    content_type_id = StringField(required=True)
    object_id = StringField(required=True)

    related_objects = ListField(StringField())

    hit_count = IntField()

    def get_object(self):
        """ return model instance represented by content_type_id & object_id instance values
        """
        ct = ContentType.objects.get(id=self.content_type_id)
        return ct.get_object_for_this_type(id=self.object_id)

    def get_related_objects(self):
        """ return a list of model instances represented by related_objects value
        """
        list_related_objects = list()
        for related_object in self.related_objects:
            content_type_id, object_id = related_object.split(";")
            ct = ContentType.objects.get(id=content_type_id)
            list_related_objects.append(ct.get_object_for_this_type(id=object_id))
        return list_related_objects


# short cuts method
def get_tuple_object(object):
    ct = ContentType.objects.get_for_model(object)
    return str(ct.pk), str(object.pk)

_ct = ContentType.objects.get_for_model

def get_related_objects_sorted(related_objects):
    if related_objects:
        list_related_objects = [(_ct(rel_object).pk, rel_object.pk) for rel_object in related_objects]
        sorted_list = sorted(list_related_objects)
        sorted_list = ((str(item0), str(item1)) for item0, item1 in sorted_list)
        return [';'.join(item) for item in sorted_list]
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
    params = dict(
        content_type_id = content_type_id,
        object_id = object_id,
        related_objects = related_objects_id,
        defaults = dict(hit_count=hit_count)
    )
    try:
        mixed_object, created = MixedObject.objects.get_or_create(**params)
        if mixed_object and not created:
            # update hitcount value with atomic updates
            MixedObject.objects(id=mixed_object.id).update(inc__hit_count=hit_count)
    except Exception, ex:
        logging.error(ex)


def get_hit_count(object, related_objects):
    content_type_id, object_id = get_tuple_object(object)
    related_objects_id = get_related_objects_sorted(related_objects)
    try:
        MixedObject.objects.get_or_create
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


def get_mixed_objects(filters, limit, offset, order_by):
    queryset = MixedObject.objects(**filters)
    if order_by:
        queryset = queryset.order_by(order_by)
    if offset:
        queryset = queryset.skip(offset)
    if limit:
        queryset = queryset.limit(limit)
    return queryset

