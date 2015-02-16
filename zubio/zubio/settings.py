"""
Django settings for zubio project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qp$jh4a)g)%2xxt%-v28(=36lm6bz$c5k=w9%wv(nk3_ldmor@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1','zubio.in']


# Application definition

INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users_zubio',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Provider Specific Accounts
    #'allauth.socialaccount.providers.amazon',
    #'allauth.socialaccount.providers.angellist',
    #'allauth.socialaccount.providers.bitbucket',
    # 'allauth.socialaccount.providers.bitly',
    # 'allauth.socialaccount.providers.dropbox',
    'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.flickr',
    # 'allauth.socialaccount.providers.feedly',
    #'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.instagram',
    # 'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.linkedin_oauth2',
    # 'allauth.socialaccount.providers.openid',
    #'allauth.socialaccount.providers.persona',
    #'allauth.socialaccount.providers.soundcloud',
    #'allauth.socialaccount.providers.stackexchange',
    # 'allauth.socialaccount.providers.tumblr',
    # 'allauth.socialaccount.providers.twitch',
    'allauth.socialaccount.providers.twitter',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',    
    'django.contrib.messages.context_processors.messages',
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
    'django.core.context_processors.request',
)


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


ROOT_URLCONF = 'zubio.urls'

WSGI_APPLICATION = 'zubio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

SITE_ID = 2