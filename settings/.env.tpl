[system]
DEBUG=true
SECRET_KEY=YOUR_SECRET_KEY
DATABASE_URL=postgres://repo_app:password@localhost:5432/repo_app
#DATABASE_URL=sqlite:///db.sqlite3  # or use sqlite3 to quickly setup development environment
SENTRY_DSN=YOUR_SENTRY_DSN
SENTRY_TRACES_SAMPLE_RATE=0.3
SENTRY_SAMPLE_RATE=0.5
CSRF_TRUSTED_ORIGINS=  # a list of origins seperated by commas
[celery]
BROKER_URL=redis://localhost:6379/0
TASK_ALWAYS_EAGER=True
TASK_EAGER_PROPAGATES=True

[cache]
URL=redis://localhost:6379/0
PREFIX=
TIMEOUT=2592000
