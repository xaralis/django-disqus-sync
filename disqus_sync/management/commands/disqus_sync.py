from __future__ import absolute_import

from django.core.management.base import NoArgsCommand

from disqus_sync.models import DisqusComment


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        DisqusComment.objects.sync()

