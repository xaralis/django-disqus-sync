from urlparse import urlparse

from django.core.cache import cache

from disqusapi import DisqusAPI, Paginator

from disqus_sync import conf


def get_apicli():
    return DisqusAPI(public_key=conf.API_KEY, secret_key=conf.API_SECRET)


class DisqusCommentLoader(object):
    def __init__(self):
        self.disqus = get_apicli()

    def get_comments(self, since=None):
        # First, sync thread map to ensure nothing is missing.
        ThreadMap.refresh_data()

        # Now, query comments.
        kwargs = {
            'forum': conf.FORUM,
        }

        if since:
            kwargs['since'] = since.isoformat()
            kwargs['order'] = 'asc'

        for c in Paginator(self.disqus.forums.listPosts, **kwargs):
            yield c


class ThreadMap(dict):
    def __init__(self, *args, **kwargs):
        super(ThreadMap, self).__init__(self.get_data())

    def get_data(self):
        data = cache.get(conf.THREAD_MAP_CACHE_KEY)

        if data is None:
            data = self.refresh_data()

        return data

    @classmethod
    def to_relative_url(cls, url):
        return urlparse(url).path

    @classmethod
    def refresh_data(cls):
        disqus = get_apicli()
        data = []

        for t in Paginator(disqus.threads.list, forum=conf.FORUM):
            data.append((t['link'], t['id']))

        cache.set(conf.THREAD_MAP_CACHE_KEY, data, timeout=conf.THREAD_MAP_CACHE_TIMEOUT)
        return data
