from __future__ import absolute_import

from django import template

from disqus_sync import conf
from disqus_sync.models import DisqusComment
from disqus_sync.loader import ThreadMap


register = template.Library()

@register.inclusion_tag('disqus_sync/comments.html', takes_context=True)
def render_disqus_comments(context):
    thread_id = ThreadMap().get_thread_id_for_url(context['request'].path)
    return {
        'request': context['request'],
        'comments': DisqusComment.objects.filter(thread_id=thread_id),
        'conf': conf
    }
