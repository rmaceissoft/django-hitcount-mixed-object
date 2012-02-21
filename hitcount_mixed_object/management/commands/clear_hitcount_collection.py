from django.core.management.base import NoArgsCommand

from hitcount_mixed_object.backends import get_backend

class Command(NoArgsCommand):
    """
    loop over all ordered items of completed orders, and push hit count into mongodb database
    """

    def handle_noargs( self, **options ):
        backend = get_backend()
        backend.clear_hitcount_collection()
        print 'hitcount collection was cleared'