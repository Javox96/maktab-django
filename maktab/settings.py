import os
from pathlib import Path

from django.contrib import messages

BASE_DIR = Path(__file__).resolve().parent.parent

# ────────────────────────────────────────────────
# XAVFSIZLIK
# ────────────────────────────────────────────────
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure--116yjsm92i0kt#vwgalic8rn&)y!zx(8^0hzw!fcz!#1r*q5d',
)
DEBUG = os.environ.get('DEBUG', 'True') == 'False'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# ────────────────────────────────────────────────
# ILOVALAR
# ────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Loyiha ilovalari
    'main',
    'account',
    'quiz',
    # Uchinchi tomon
    'crispy_forms',
    'crispy_bootstrap5',
]

# ────────────────────────────────────────────────
# MIDDLEWARE
# ────────────────────────────────────────────────
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

ROOT_URLCONF = 'maktab.urls'

# ────────────────────────────────────────────────
# TEMPLATES
# ────────────────────────────────────────────────
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
                'django.template.context_processors.static',
                'maktab.context_processors.login_modal',
            ],
        },
    },
]

WSGI_APPLICATION = 'maktab.wsgi.application'

# ────────────────────────────────────────────────
# MA'LUMOTLAR BAZASI
# ────────────────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ────────────────────────────────────────────────
# AUTENTIFIKATSIYA
# ────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LOGIN_URL = 'account:login'
LOGIN_REDIRECT_URL = 'main:index'
LOGOUT_REDIRECT_URL = 'main:index'

# ────────────────────────────────────────────────
# SESSIYA VA COOKIE XAVFSIZLIGI
# ────────────────────────────────────────────────
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 86400 * 14        # 2 hafta
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True       # Eski brauzerlar uchun

# ────────────────────────────────────────────────
# LOKALIZATSIYA
# ────────────────────────────────────────────────
LANGUAGE_CODE = 'uz'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

# ────────────────────────────────────────────────
# STATIK VA MEDIA FAYLLAR
# ────────────────────────────────────────────────
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'assets']
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ────────────────────────────────────────────────
# XABARLAR
# ────────────────────────────────────────────────
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# ────────────────────────────────────────────────
# UCHINCHI TOMON
# ────────────────────────────────────────────────
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'