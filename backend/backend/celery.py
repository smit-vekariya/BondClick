import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# install celery from here https://github.com/tporadowski/redis/releases
app = Celery('backend')
app.conf.enable_utc = False
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object(settings, namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


# celery -A backend.celery worker --pool=solo -l info

# celery -A backend worker --loglevel=INFO --pool=solo

# celery -A backend beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
