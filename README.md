django-disqus-sync
=================

This app is lightweight SEO optimizer for DISQUS comment system for your Django
application.

It features Django management command/Celery task to sync comments from DISQUS to
your database and to embed them to the page for web crawlers like Google. DISQUS
comment system is JS based and Google still has issues indexing it.

This app also features template tag to embed prerendered comments to your page.

Installation & usage
-----

First, install using pip:


```
pip install django-disqus-sync
```

Next, you need to create DISQUS app in order to be able to use their API to download
comments.

You can create your app here: https://disqus.com/api/applications/

Then, configure in your django `settings.py` using keys you were given:

```
DISQUS_API_KEY = '...'
DISQUS_API_SECRET = '...'
DISQUS_WEBSITE_SHORTNAME = '[NAME OF YOUR DISQUS FORUM HERE]'
```

Also make sure you have **some cache configured** since this apps needs it to
save queries and load temporary URL to THREAD list.

Next, you need to setup period updates of comments in your forum. Either set up
a cron to run management command:

```
manage.py disqus_sync
```

Or, you can use Celery to run it. Celery task should be auto-registered and you
only need to configure Celerybeat to fire it up from time to time.


Last, use the templatetag in your templates to embed comments:

```
{% load disqus_sync %}
{% render_disqus_comments %}
```

That's it, comments should be rendered to your page. **They will not be seen
in browser, because they are by default wrapped in "display: none;" div.**

You can override template used to render the comments by creating
`disqus_sync/comments.html`, `disqus_sync/comment.html` or both.
