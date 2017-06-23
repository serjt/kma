# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from redactor.fields import RedactorField


def image_upload_to(instance, filename):
    return "%s" % filename


class Kabar(models.Model):
    class Meta:
        ordering = '-date'.split()
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_upload_to)
    text = RedactorField(verbose_name='Текст',
                         upload_to=image_upload_to,
                         # redactor_options={'buttons': ['image'],},
                         allow_image_upload=True,
                         allow_file_upload=True)
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Npa(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    text = RedactorField(verbose_name='Текст',
                         upload_to=image_upload_to,
                         # redactor_options={'buttons': ['image'],},
                         allow_image_upload=True,
                         allow_file_upload=True)
    date = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to=image_upload_to, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Education(models.Model):
    choices = (
        ('ПДМО', 'ПДМО'),
        ('НМО', 'НМО')
    )
    category = models.CharField(choices=choices,
                                max_length=100)
    name = models.CharField(max_length=100)
    text = RedactorField(verbose_name='Текст',
                         upload_to=image_upload_to,
                         # redactor_options={'buttons': ['image'],},
                         allow_image_upload=True,
                         allow_file_upload=True)
    date = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to=image_upload_to, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Atestation(models.Model):
    name = models.CharField(max_length=100)
    text = RedactorField(verbose_name='Текст',
                         upload_to=image_upload_to,
                         # redactor_options={'buttons': ['image'],},
                         allow_image_upload=True,
                         allow_file_upload=True)
    date = models.DateTimeField(auto_now=True)
    number = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Protocol(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    text = RedactorField(verbose_name='Текст',
                         upload_to=image_upload_to,
                         # redactor_options={'buttons': ['image'],},
                         allow_image_upload=True,
                         allow_file_upload=True)
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
