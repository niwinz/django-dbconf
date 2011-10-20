# -*- coding: utf-8 -*-

from .models import *
from django.contrib import admin

class ConfigModelAdmin(admin.ModelAdmin):
    list_display = ('key', 'val')
    list_display_links = list_display

    def queryset(self, *args, **kwargs):
        return Conf.objects.all().order_by('key')


admin.site.register(Conf, ConfigModelAdmin)
