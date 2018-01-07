# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Article, Photo, Teacher, Person, Feedback

admin.site.register(Article)

admin.site.register(Photo)
admin.site.register(Teacher)
admin.site.register(Person)
admin.site.register(Feedback)
