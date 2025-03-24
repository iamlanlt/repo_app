from .base import config_parser
from .internationalization import TIME_ZONE

# Celery Configuration Options
# Celery
# -------------------------------------------------------------------------------
# https://docs.celeryproject.org/en/stable/userguide/configuration.html
CELERY_BROKER_URL = config_parser.get(
    "celery", "BROKER_URL", fallback="redis://localhost:6379/0"
)
CELERY_RESULT_BACKEND = "django-db"
CELERY_CACHE_BACKEND = "django-cache"
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_SERIALIZER = "pickle"
CELERY_RESULT_SERIALIZER = "pickle"
CELERY_ACCEPT_CONTENT = ["pickle"]
CELERY_TASK_DEFAULT_QUEUE = "default"
CELERY_TASK_SOFT_TIME_LIMIT = 60 * 60 * 6  # default to 6 hours.
CELERY_TASK_ALWAYS_EAGER = config_parser.getboolean(
    "celery", "TASK_ALWAYS_EAGER", fallback=True
)
CELERY_TASK_EAGER_PROPAGATES = config_parser.getboolean(
    "celery", "TASK_EAGER_PROPAGATES", fallback=True
)

''' Example
CELERY_BEAT_SCHEDULE = {
    "task_name": {
        "task": "namespace.module.task",
        "schedule": 10 # in seconds
        # or by crontab: https://docs.celeryq.dev/en/3.1/userguide/periodic-tasks.html#crontab-schedules
        "schedule": crontab(minutes="*/5")
    }
}
'''
CELERY_BEAT_SCHEDULE = {}
