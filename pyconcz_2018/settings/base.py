"""
Django settings for pyconcz_2018 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
TMP_DIR = os.path.join(BASE_DIR, '..', 'tmp')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'provide in local.py'

ADMINS = [
    ('admins', 'admin@pycon.cz'),
]

DEFAULT_FROM_EMAIL = 'admin@pycon.cz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SITE_ID = 1

if DEBUG:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = [
        'cz.pycon.org',
        'pycon.cz',
    ]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'raven.contrib.django.raven_compat',
    'import_export',

    'pyconcz_2018.announcements',
    'pyconcz_2018.common',
    'pyconcz_2018.team',
    'pyconcz_2018.proposals',
    'pyconcz_2018.sponsors',
    'pyconcz_2018.programme',
    'pyconcz_2018.intermission',

    'widget_tweaks',
    'emojificate',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pyconcz_2018.urls'

PHASE = [
    '00-init',  # Initial phase
    '10-date-place',  # Date and place announced
    '20-cfp-opened',  # Call for papers open
    '30-cfp-extended',  # Call for papers extended
    '40-cfp-closed',  # Call for papers is closed
    '50-cfp-evaluated',  # Papers were evaluated
    '60-earlybird',  # Early bird ticket sales start
    '70-finaid-opened',
    '80-talks-published',  # even if only part of them
    '90-finaid-closed',
    '100-tickets-sold-out',
    '110-schedule-published',
    '120-workshop-registration-opened',
    '130-day-1',
    '140-day-2',
    '150-day-3',
    '160-after',
    '170-videos-published',
]

PHASE_CURRENT = 17

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates' + '/' + PHASE[PHASE_CURRENT]),
            os.path.join(BASE_DIR, 'templates/default/'),
            os.path.join(BASE_DIR, 'templates/old/'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'pyconcz_2018.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

try:
    DB_USER = os.environ['DB_USER']
    DB_HOST = os.environ['DB_HOST']
    DB_PASS = os.environ['DB_PASS']
except KeyError:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'pyconcz',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'HOST': DB_HOST,
            'NAME': os.environ.get('DB_NAME', DB_USER),
            'USER': DB_USER,
            'PASSWORD': DB_PASS,
            'PORT': os.environ.get('DB_PORT', 5432),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
]

USE_TZ = True
TIME_ZONE = 'Europe/Prague'

FORMAT_MODULE_PATH = [
    'pyconcz_2018.formats'
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/2018/static/'
STATIC_ROOT = os.path.join(TMP_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(TMP_DIR, 'media')

SLACK_WEBHOOK = ''  # This variable is set in local.py

TALKS_DATES = [datetime.date(2018, 6, 1), datetime.date(2018, 6, 2)]
WORKSHOPS_DATES = [datetime.date(2018, 6, 3)]
TALKS_ROOMS = [
    (1, 'Main'),
    (2, 'Theatre'),
]
WORKSHOPS_ROOMS = [
    (4, 'room 301'),
    (5, 'room 302'),
    (6, 'room 303'),
    (7, 'room 343'),
    (8, 'room 346'),
    (9, 'room 347'),
    (10, 'room 348'),
    (11, 'room 349'),
    (20, 'Respirium'),
]
SPRINT_ROOMS = [

]

OTHER_ROOMS = [
    (30, 'Foyer'),
    (40, 'Backyard'),
    (50, 'Red room'),
    (60, 'Fish tank'),
]

ALL_ROOMS = TALKS_ROOMS + WORKSHOPS_ROOMS + SPRINT_ROOMS + OTHER_ROOMS
