from __future__ import absolute_import

from django import template

from disqus_sync import conf
from disqus_sync.models import DisqusComment
from disqus_sync.loader import ThreadMap


register = template.Library()

@register.inclusion_tag('disqus_sync/comments.html', takes_context=True)
def render_disqus_comments(context):
    try:
        thread_id = ThreadMap()[context['request'].build_absolute_uri()]
        comments = DisqusComment.objects.filter(thread_id=thread_id)
    except KeyError:
        # thread_id could not be resolved
        comments = []

    return {
        'request': context['request'],
        'comments': comments,
        'conf': conf
    }
