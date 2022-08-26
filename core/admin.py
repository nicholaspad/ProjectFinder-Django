from django.contrib import admin
from .models import Config, ConfigAdmin, EmailLog, EmailLogAdmin, Entry

admin.site.register(Config, ConfigAdmin)
admin.site.register(Entry)
admin.site.register(EmailLog, EmailLogAdmin)

ADMIN_SITE_NAME = "ProjectFinder Admin"
admin.site.site_header = ADMIN_SITE_NAME
admin.site.site_title = ADMIN_SITE_NAME
admin.site.index_title = ADMIN_SITE_NAME
