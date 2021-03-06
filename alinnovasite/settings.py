"""
Django settings for alinnovasite project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=&5yt=6agf(qprony!=n&gqd=8@2zfuui@n*mr^y!u3nfx%&vs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'blog.apps.BlogConfig',
	'social_django',
	'core.apps.CoreConfig',
	'django.contrib.admin',
	#'django_facebook',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'alinnovasite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				#'django_facebook.context_processors.facebook', # <--
				#'django.core.context_processors.request', #<--
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'social_django.context_processors.backends',  # <--
				'social_django.context_processors.login_redirect', # <--
            ],
        },
    },
]



WSGI_APPLICATION = 'alinnovasite.wsgi.application'

AUTHENTICATION_BACKENDS = (
	'social_core.backends.github.GithubOAuth2',
	'social_core.backends.twitter.TwitterOAuth',
	'social_core.backends.facebook.FacebookOAuth2',
	'social_core.backends.linkedin.LinkedinOAuth',
	'social_core.backends.linkedin.LinkedinOAuth2',
	#'django_facebook.auth_backends.FacebookBackend',
	'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_FACEBOOK_KEY = '1927682667549629'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '8789bbffcc7733918d9af5cb223d1ade'  # App Secret

SOCIAL_AUTH_LINKEDIN_KEY = '77gumjzpziazln'
SOCIAL_AUTH_LINKEDIN_SECRET = 'FMHMUvMuIDulNuHm'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_basicprofile']
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = ['email-address', 'headline', 'industry']
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA      = [
    ('id', 'id'),
    ('first-name', 'first_name'),
    ('last-name', 'last_name'),
    ('email-address', 'email_address'),
    ('headline', 'headline'),
    ('industry', 'industry')
]
FIELD_SELECTORS = ['email-address',]




# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
