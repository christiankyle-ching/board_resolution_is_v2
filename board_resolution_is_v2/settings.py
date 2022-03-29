"""
Django settings for board_resolution_is_v2 project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['BRIS_SECRET']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INTERNAL_IPS = [
    '127.0.0.1',
]

ALLOWED_HOSTS = [
    # Local server
    '127.0.0.1',
    'localhost',

    # TODO: Change based on IP in the environment. ex. 192.168.1.*
    # Consider also using * if port 80 and 443 will not be opened in firewall anyway
    # Local PCs
    '*'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Deployment
    'mod_wsgi.server',

    # Packages
    'tailwind',
    'theme',
    'django_browser_reload',

    # Custom Apps
    'resolutions.apps.ResolutionsConfig',
    'users.apps.UsersConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'board_resolution_is_v2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Custom Context Processors
                'theme.context_processors.other_accounts'
            ],
        },
    },
]

WSGI_APPLICATION = 'board_resolution_is_v2.wsgi.application'

# Theming
TAILWIND_APP_NAME = 'theme'

# TODO: Replace with where your nodejs/npm is located
# Use `where npm` in cmd to know the location, assuming you have nodejs installed
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['PSQL_BRIS_DBNAME'],
        'USER': os.environ['PSQL_USER'],
        'PASSWORD': os.environ['PSQL_PASSWORD'],
        'HOST': os.environ['PSQL_HOST'],
        'PORT': os.environ['PSQL_PORT'],
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

MEDIA_ROOT = 'media'  # Folder path where files are stored in server
MEDIA_URL = '/media/'  # URL path for download

STATIC_ROOT = 'static'  # Folder path where files are stored in server
STATIC_URL = '/static/'  # URL path for download

AUTH_USER_MODEL = 'users.User'

# TODO: Modify these values (Client-based)
CLIENT_NAME = "PLV Board Resolution"

# Email Backend (Gmail)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ['BRIS_EMAIL_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['BRIS_EMAIL_PASSWORD']

DEFAULT_FROM_EMAIL = os.environ['BRIS_EMAIL_USERNAME']

# Default Redirects

LOGIN_URL = 'users:auth:login'
LOGIN_REDIRECT_URL = 'resolutions:index'
LOGOUT_REDIRECT_URL = 'users:auth:login'
