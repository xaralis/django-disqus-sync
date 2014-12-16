from disqus_sync.models import DisqusComment

try:
    # Define task only if celery is available.
    from celery.task import task
    from celery.utils.log import get_task_logger

    logger = get_task_logger(__name__)

    @task(name='disqus_sync')
    def disqus_sync():
        DisqusComment.objects.sync()

except ImportError:
    pass
