from pathlib import Path
from environs import Env # new
from pathlib import Path

env = Env() # new
env.read_env() # new

AUTH_USER_MODEL = "accounts.CustomUser" # new
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)


ALLOWED_HOSTS = [".herokuapp.com", "localhost", "127.0.0.1"] # new

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "whitenoise.runserver_nostatic", # new
    'django.contrib.staticfiles',
    "django.contrib.sites", # new
    "rest_framework", # new
    "corsheaders", # new
    "rest_framework.authtoken", # new
    "allauth", # new
    "allauth.account", # new
    "allauth.socialaccount", # new
    "dj_rest_auth", # new
    "dj_rest_auth.registration", # new
    "drf_spectacular", # new
    "accounts.apps.AccountsConfig", # new
    "posts.apps.PostsConfig", # new
]

REST_FRAMEWORK = { # new
"DEFAULT_PERMISSION_CLASSES": [
"rest_framework.permissions.IsAuthenticated", # new

],

"DEFAULT_AUTHENTICATION_CLASSES": [ # new
"rest_framework.authentication.SessionAuthentication",
"rest_framework.authentication.TokenAuthentication", # new
],
"DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema", # new

}

SPECTACULAR_SETTINGS = {
"TITLE": "Blog API Project",
"DESCRIPTION": "A sample blog to learn about DRF",
"VERSION": "1.0.0",
# OTHER SETTINGS
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware", # new
    "corsheaders.middleware.CorsMiddleware", # new
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]




CORS_ORIGIN_WHITELIST = (
"http://localhost:3000",
"http://localhost:8000",
)

CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"] # new


ROOT_URLCONF = 'django_project.urls'

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
                "django.template.context_processors.request", # new
            ],
        },
    },
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" # new
SITE_ID = 1 # new

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
        "default": env.dj_db_url("DATABASE_URL") # new
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"] # new
STATIC_ROOT = BASE_DIR / "staticfiles" # new
STATICFILES_STORAGE ="whitenoise.storage.CompressedManifestStaticFilesStorage" # new

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
