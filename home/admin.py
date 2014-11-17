from django.contrib import admin

from models import Testers


class TestersAdmin(admin.ModelAdmin):
    pass
admin.site.register(Testers, TestersAdmin)
