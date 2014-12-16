from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


try:
    API_KEY = settings.DISQUS_API_KEY
    API_SECRET = settings.DISQUS_API_SECRET
    FORUM = settings.DISQUS_WEBSITE_SHORTNAME
except AttributeError:
    raise ImproperlyConfigured('In order to use disqus_sync you have to specify '
                               'DISQUS_API_KEY, DISQUS_API_SECRET and '
                               'DISQUS_WEBSITE_SHORTNAME in your Django settings.')


THREAD_MAP_CACHE_TIMEOUT = getattr(settings, 'DISQUS_THREAD_MAP_CACHE', 24 * 60 * 60)
THREAD_MAP_CACHE_KEY = getattr(settings, 'DISQUS_THREAD_MAP_CACHE_KEY', 'disqus:threadmap')
