from core.settings.base import *

DEBUG = False

ALLOWED_HOSTS = [
    # ".brb-titans.uz",
    "brb.falconsoft.uz",
]

CSRF_TRUSTED_ORIGINS = [
    "https://www.brb-titans.uz",
    "https://brb.falconsoft.uz",
    "wss://www.brb-titans.uz",
    "wss://brb.falconsoft.uz",
]
CSRF_COOKIE_SECURE = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PASS"),
        "HOST": env.str("DB_HOST"),
        "PORT": env.str("DB_PORT"),
    }
}

LOGGER_BOT_TOKEN = env.str("LOGGER_BOT_TOKEN")
LOGGER_CHAT_ID = env.str("LOGGER_CHAT_ID")

CORS_ALLOWED_ORIGINS = [
    "https://www.brb-titans.uz",
    "https://brb.falconsoft.uz",
]
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True
