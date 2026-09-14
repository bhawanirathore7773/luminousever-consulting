from pathlib import Path
import os
BASE_DIR=Path(__file__).resolve().parent.parent.parent
SECRET_KEY=os.environ.get("SECRET_KEY","dev-only-change-me")
DEBUG=os.environ.get("DEBUG","True").lower()=="true"
ALLOWED_HOSTS=[x.strip() for x in os.environ.get("ALLOWED_HOSTS","localhost,127.0.0.1").split(",") if x.strip()]
DATABASE_URL=os.environ.get("DATABASE_URL","")
REDIS_URL=os.environ.get("REDIS_URL","redis://localhost:6379/0")
CACHE_VERSION=os.environ.get("CACHE_VERSION","1")
LEAD_NOTIFICATION_EMAIL=os.environ.get("LEAD_NOTIFICATION_EMAIL","")
DEFAULT_FROM_EMAIL=os.environ.get("DEFAULT_FROM_EMAIL","noreply@example.com")

INSTALLED_APPS=[
"django.contrib.admin","django.contrib.auth","django.contrib.contenttypes","django.contrib.sessions",
"django.contrib.messages","django.contrib.staticfiles","rest_framework",
"apps.core","apps.services","apps.solutions","apps.industries","apps.sap_expertise",
"apps.case_studies","apps.insights","apps.team","apps.contact","apps.assessments","apps.seo",
]
MIDDLEWARE=[
"django.middleware.security.SecurityMiddleware","whitenoise.middleware.WhiteNoiseMiddleware","django.contrib.sessions.middleware.SessionMiddleware",
"django.middleware.common.CommonMiddleware","django.middleware.csrf.CsrfViewMiddleware",
"django.contrib.auth.middleware.AuthenticationMiddleware","django.contrib.messages.middleware.MessageMiddleware",
"django.middleware.clickjacking.XFrameOptionsMiddleware","apps.core.middleware.RequestTimingMiddleware"]
ROOT_URLCONF="config.urls"
TEMPLATES=[{"BACKEND":"django.template.backends.django.DjangoTemplates","DIRS":[BASE_DIR/"templates"],"APP_DIRS":True,"OPTIONS":{"context_processors":["django.template.context_processors.request","django.contrib.auth.context_processors.auth","django.contrib.messages.context_processors.messages","apps.core.context_processors.site_meta"]}}]
WSGI_APPLICATION="config.wsgi.application"
if DATABASE_URL:
    import dj_database_url
    DATABASES={"default":dj_database_url.parse(DATABASE_URL,conn_max_age=60,ssl_require=not DEBUG)}
else:
    DATABASES={"default":{"ENGINE":"django.db.backends.sqlite3","NAME":BASE_DIR/"db.sqlite3"}}
CACHES={"default":{"BACKEND":"django.core.cache.backends.redis.RedisCache","LOCATION":REDIS_URL,"TIMEOUT":300}}
CELERY_BROKER_URL=REDIS_URL
CELERY_RESULT_BACKEND=REDIS_URL
CELERY_TASK_TRACK_STARTED=True
CELERY_TASK_TIME_LIMIT=300
CELERY_TASK_SOFT_TIME_LIMIT=240
STATIC_URL="/static/"
STATIC_ROOT=BASE_DIR/"staticfiles"
STATICFILES_DIRS=[BASE_DIR/"static"]
STORAGES={"default":{"BACKEND":"django.core.files.storage.FileSystemStorage"},"staticfiles":{"BACKEND":"whitenoise.storage.CompressedManifestStaticFilesStorage"}}
MEDIA_URL="/media/"
MEDIA_ROOT=BASE_DIR/"media"
DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"
USE_TZ=True
LANGUAGE_CODE="en-us"
TIME_ZONE="Asia/Kolkata"
LEAD_NOTIFICATION_EMAIL=LEAD_NOTIFICATION_EMAIL
DEFAULT_FROM_EMAIL=DEFAULT_FROM_EMAIL

