# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    img = models.ImageField(upload_to='media/', null=True, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Feedback(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Имя")
    email = models.EmailField(max_length=255, verbose_name=u"Email")
    text = models.TextField(verbose_name=u"Сообщение")

    def __str__(self):
        return self.name

class Photo(models.Model):
    img = models.ImageField(upload_to='media/', null=True, blank=True)
    text =models.CharField(max_length=255,verbose_name="text")
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.text

class Teacher(models.Model):
    img = models.ImageField(upload_to='media/', null=True, blank=True)
    position = models.CharField(max_length=255,verbose_name=u"Должность")
    number = models.IntegerField(verbose_name=u"Номер")
    name = models.CharField(max_length=255,verbose_name=u"Имя")
    email = models.CharField(max_length=30,verbose_name=u"email")
    id = models.IntegerField(primary_key=True,verbose_name="id")
    def __str__(self):
        return self.name


