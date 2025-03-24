"""
    This configuration file overrides some necessary configs
    to deploy the app to production environment.
"""

from .base import *  # noqa
from .base import config_parser


# Cache settings
CACHE_URL = config_parser.get(
    "cache", "URL", fallback="redis://127.0.0.1:6379/2"
)
CACHE_PREFIX = config_parser.get("cache", "PREFIX", fallback="")
CACHE_TIMEOUT = config_parser.getint(
    "cache", "TIMEOUT", fallback=24 * 60 * 60 * 30  # timeout after 30 days
)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": CACHE_URL,
        "KEY_PREFIX": CACHE_PREFIX + "default",
        "TIMEOUT": CACHE_TIMEOUT,
    },
}

# Session settings
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
