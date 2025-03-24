from .base import config_parser


CSRF_TRUSTED_ORIGINS = []
try:
    _origins = config_parser.get("system", "CSRF_TRUSTED_ORIGINS", fallback="")
    if _origins:
        CSRF_TRUSTED_ORIGINS = [
            origin for origin in _origins.split(",") if origin
        ]
except Exception:
    pass
