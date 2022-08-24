from django.contrib import admin
from .models import Config, ConfigAdmin, Entry

admin.site.register(Config, ConfigAdmin)
admin.site.register(Entry)

ADMIN_SITE_NAME = "ProjectFinder Admin"
admin.site.site_header = ADMIN_SITE_NAME
admin.site.site_title = ADMIN_SITE_NAME
admin.site.index_title = ADMIN_SITE_NAME
