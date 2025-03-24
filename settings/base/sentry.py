from .base import config_parser, ENVIRONMENT

SENTRY_DSN = config_parser.get("system", "SENTRY_DSN", fallback="")
SENTRY_TRACES_SAMPLE_RATE = config_parser.getfloat(
    "system", "SENTRY_TRACES_SAMPLE_RATE", fallback=1
)
SENTRY_SAMPLE_RATE = config_parser.getfloat(
    "system", "SENTRY_SAMPLE_RATE", fallback=1
)

if SENTRY_DSN and ENVIRONMENT == "prod":
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=SENTRY_TRACES_SAMPLE_RATE,
        sample_rate=SENTRY_SAMPLE_RATE,
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
    )
