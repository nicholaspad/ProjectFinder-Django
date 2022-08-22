from django.contrib import admin
from .models import Config

admin.site.register(Config)

ADMIN_SITE_NAME = "ProjectFinder Admin"
admin.site.site_header = ADMIN_SITE_NAME
admin.site.site_title = ADMIN_SITE_NAME
admin.site.index_title = ADMIN_SITE_NAME
