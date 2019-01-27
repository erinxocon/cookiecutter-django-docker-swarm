from .base_settings import *
from .base_settings import env

DEBUG = True

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "{{cookiecutter.docker_host}}"]

CACHES = {"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache", "LOCATION": ""}}

LOCAL_ADMIN = "admin"
LOCAL_PASS = "haxor"

TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG  # type: ignore

EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = 1025

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}

INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
if env("USE_DOCKER") == "yes":
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [ip[:-1] + "3" for ip in ips]


INSTALLED_APPS += ["django_extensions"]
