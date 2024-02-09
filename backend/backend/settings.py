"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

SECRET_KEY = str(os.getenv("SECRET_KEY"))

DEBUG = False

ALLOWED_HOSTS = [".ec2-15-206-79-3.ap-south-1.compute.amazonaws.com"]

## Development Settings
if DEBUG:
    ALLOWED_HOSTS += [".localhost", "127.0.0.1", "[::1]", "web:8000"]
    ALLOWED_HOSTS = ["*"]


CORS_ALLOW_CREDENTIALS = True

# CORS_ORIGIN_WHITELIST = (
#     "http://localhost:8844",
#     "http://localhost:8846",
#     "http://localhost:8848",
# )

CORS_ALLOW_ALL_ORIGINS = True


INSTALLED_APPS = [
    "quiz.apps.QuizConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
]

# Allow specific headers
CORS_ALLOW_HEADERS = [
    "content-type",
    "content-disposition",
    "content-length",
]

# Allow specific methods
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]


## Security Settings
X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

CORS_ALLOW_CREDENTIALS = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


MEDIA_URL = "/media/"
MEDIA_ROOT = "/www/app/media/"
STATIC_ROOT = "/www/app/staticfiles/"
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True  # Change to True when in production with https
    CSRF_COOKIE_SECURE = True  # Change to True when in production with https
    SESSION_COOKIE_HTTPONLY = True  # Change to True when in production with https
    CSRF_TRUSTED_ORIGINS = [
        "http://ec2-15-206-79-3.ap-south-1.compute.amazonaws.com",
        "http://www.ec2-15-206-79-3.ap-south-1.compute.amazonaws.com",
    ]
    # SECURE_HSTS_SECONDS = 31536000  # 1 year
    # SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    # SECURE_HSTS_PRELOAD = True
    # SECURE_CONTENT_TYPE_NOSNIFF = True
    # SECURE_BROWSER_XSS_FILTER = True
    # X_FRAME_OPTIONS = "DENY"
    # ALLOWED_HOSTS = ["*"]
else:
    SECURE_PROXY_SSL_HEADER = None
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_HSTS_SECONDS = None
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
