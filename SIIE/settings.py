"""
Django settings for SIIE project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
#tiempo de desconeccion
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$*@a^%luw^9^xe%rlqc*7_o^obva+)1+ysd6r(-9yb2$yu4*3_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False
# '192.100.188.34','localhost', '*'
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    #Django Apps
    'django.contrib.admin',
    'django.contrib.auth', #Login
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Local apps
    'Apps.accounts',
    'Apps.biblioteca',
    'Apps.caja',
    'Apps.cajaNueva',
    'Apps.controlEscolar',
    'Apps.estadias',
    'Apps.planeacion',
    'Apps.servicioSocial',
    'Apps.titulacion',
    'Apps.utilerias',
    'Apps.vinculacion',
    #estilos
    'django_bootstrap_icons',
    #Importar y exportar
    'import_export',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #Logaut automatico
    'django_auto_logout.middleware.auto_logout' , 
]

ROOT_URLCONF = 'SIIE.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # !!! Add this !!!
                'django_auto_logout.context_processors.auto_logout_client',
            ],
        },
    },
]

WSGI_APPLICATION = 'SIIE.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'desarrollo',
        'USER': 'postgres',
        'PASSWORD': 'P@$$W0rd',
        'HOST': '192.168.3.5',
        #'PASSWORD': 'admin',
        #'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Conexxion a la base de datos en desarrollo interna
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'Universidad_siie.db',
#     }
# }


# Coneccion a la base de datos postgres local
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'desarrollo',
#         'USER': 'postgres',
#         'PASSWORD': 'admin',
#         'HOST': 'localhost',
#         'DATABASE_PORT': 5432,
#     }
# }


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

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_ROOT = BASE_DIR / '/static/'

STATICFILES_DIRS = (
    BASE_DIR, 'static',
)

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# django_project/settings.py 
# Direccion para redigir despues del inicio de sesion
LOGIN_REDIRECT_URL = "index"
# Direccion para redirigir despues de cerrar sesion
LOGOUT_REDIRECT_URL = 'login'

# Se configuro para desconectar el usuario en caso de no tener actividad
AUTO_LOGOUT = {
    'IDLE_TIME': timedelta(minutes=10), # Tiempo en que se desconecta la sesion por inactividad
    'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
    'MESSAGE': 'La sesión ha expirado. Vuelve a iniciar sesión para continuar.',
}

# Control recuperar contraseña uso de correo o para lo que se ocupa mandar correos
EMAIL_USE_TLS = True # Protocolo 
EMAIL_HOST = 'smtp.gmail.com' # Servicio de emil de google
EMAIL_PORT = 25
EMAIL_HOST_USER = 'tse.jacinto23@gmail.com' # Correo donde emviaremos los correos
EMAIL_HOST_PASSWORD = 'Mike23_$' # Contraseña del correo 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # Backeds del email
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

