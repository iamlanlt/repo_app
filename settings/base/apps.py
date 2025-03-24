DJANGO_APPs = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

EXTERNAL_APPS = [
    "django_extensions",
    "django_filters",
    "rest_framework",
    "rest_framework.authtoken",
    "django_celery_beat",
    "django_celery_results",
]
INTERNAL_APPS = []

INSTALLED_APPS = DJANGO_APPs + EXTERNAL_APPS + INTERNAL_APPS
