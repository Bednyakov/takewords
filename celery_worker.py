from celery import Celery

def make_celery(app):
    from celery import Celery
    celery = Celery(
        app.import_name,
        backend=app.config['broker_url'],
        broker=app.config['result_backend']
    )
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery