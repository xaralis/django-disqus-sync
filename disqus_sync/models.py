from django.db import models

from disqus_sync.loader import DisqusCommentLoader


class DisqusCommentManager(models.Manager):
    def sync(self):
        loader = DisqusCommentLoader()
        last_entry = self.aggregate(last_date=models.Max('date'))['last_date'] or None

        for comment in loader.get_comments(since=last_entry):
            self.get_or_create(comment_id=comment['id'], defaults={
                'thread_id': comment['thread'],
                'forum_id': comment['forum'],
                'body': comment['message'],
                'parent_comment_id': comment['parent'],
                'author_name': comment['author']['name'],
                'author_email': comment['author'].get('email'),
                'author_url': comment['author']['url'],
                'date': comment['createdAt']
            })


class DisqusComment(models.Model):
    comment_id = models.CharField(max_length=32, primary_key=True)
    thread_id = models.CharField(max_length=32)
    forum_id = models.CharField(max_length=32)
    parent_comment_id = models.CharField(max_length=32, null=True, blank=True)
    body = models.TextField()
    author_name = models.CharField(max_length=200)
    author_email = models.EmailField(null=True, blank=True)
    author_url = models.URLField(null=True, blank=True)
    date = models.DateTimeField()

    objects = DisqusCommentManager()

    def __unicode__(self):
        return '<DisqusComment: %s>' % self.comment_id
