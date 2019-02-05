# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from rango.models import Category, Page, PageAdmin


# Register your models here.
admin.site.register(Category)
admin.site.register(Page, PageAdmin)
