from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('celery-example.tasks',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0',
             include=['celery-example.tasks'])

# app = Celery('tasks', backend='redis://localhost:6379/0',
#              broker='redis://localhost:6379/0')

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
