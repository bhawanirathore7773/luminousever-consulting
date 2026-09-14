from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(BASE_DIR / ".env")

SECRET_KEY = env("SECRET_KEY", default="django-insecure-change-me-in-production")
DEBUG = env("DEBUG", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])

INSTALLED_APPS = [
    "django.contrib.admin","django.contrib.auth","django.contrib.contenttypes",
    "django.contrib.sessions","django.contrib.messages","django.contrib.staticfiles",
    "apps.core","apps.services","apps.solutions","apps.industries","apps.sap_expertise",
    "apps.case_studies","apps.insights","apps.team","apps.contact","apps.assessments",
    "apps.seo","apps.analytics",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"
TEMPLATES = [{
    "BACKEND":"django.template.backends.django.DjangoTemplates",
    "DIRS":[BASE_DIR / "templates"],
    "APP_DIRS":True,
    "OPTIONS":{"context_processors":[
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
    ]},
}]
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

DATABASES = {
    "default": env.db("DATABASE_URL", default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}")
}
DATABASES["default"]["CONN_MAX_AGE"] = env.int("DB_CONN_MAX_AGE", default=60)

CACHES = {
    "default": {
        "BACKEND":"django_redis.cache.RedisCache",
        "LOCATION":env("REDIS_URL", default="redis://127.0.0.1:6379/1"),
        "OPTIONS":{"CLIENT_CLASS":"django_redis.client.DefaultClient"},
        "KEY_PREFIX":"luminousever",
        "TIMEOUT":300,
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

LANGUAGE_CODE="en-us"
TIME_ZONE="Asia/Kolkata"
USE_I18N=True
USE_TZ=True

STATIC_URL="/static/"
STATIC_ROOT=BASE_DIR / "staticfiles"
STATICFILES_DIRS=[BASE_DIR / "static"]
STORAGES={
    "default":{"BACKEND":"django.core.files.storage.FileSystemStorage"},
    "staticfiles":{"BACKEND":"whitenoise.storage.CompressedManifestStaticFilesStorage"},
}
MEDIA_URL="/media/"
MEDIA_ROOT=BASE_DIR / "media"

DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"
LOGIN_URL="/admin/login/"
CSRF_COOKIE_SECURE=env.bool("CSRF_COOKIE_SECURE", default=False)
SESSION_COOKIE_SECURE=env.bool("SESSION_COOKIE_SECURE", default=False)
SECURE_HSTS_SECONDS=env.int("SECURE_HSTS_SECONDS", default=0)
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=False
SECURE_CONTENT_TYPE_NOSNIFF=True
SECURE_REFERRER_POLICY="strict-origin-when-cross-origin"
X_FRAME_OPTIONS="DENY"

SECURE_PROXY_SSL_HEADER=("HTTP_X_FORWARDED_PROTO","https")
CSRF_TRUSTED_ORIGINS=env.list("CSRF_TRUSTED_ORIGINS", default=[])

EMAIL_BACKEND=env("EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")
DEFAULT_FROM_EMAIL=env("DEFAULT_FROM_EMAIL", default="hello@luminousever.com")

CSP_DEFAULT_SRC=("'self'",)
CSP_STYLE_SRC=("'self'","'unsafe-inline'")
CSP_SCRIPT_SRC=("'self'",)
CSP_IMG_SRC=("'self'","data:","https:")
CSP_FONT_SRC=("'self'","data:")

CACHES["default"]["OPTIONS"]["IGNORE_EXCEPTIONS"] = True
