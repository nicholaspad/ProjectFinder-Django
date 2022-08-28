import dj_database_url

DEBUG = False

ALLOWED_HOSTS = [".herokuapp.com"]

DATABASES = {"default": dj_database_url.config(conn_max_age=600, ssl_require=True)}

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
