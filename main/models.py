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
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    image = models.ImageField(upload_to=image_upload_to, verbose_name='Картинка')
    text = RedactorField(verbose_name='Текст',
                         upload_to=image_upload_to,
                         # redactor_options={'buttons': ['image'],},
                         allow_image_upload=True,
                         allow_file_upload=True)
    date = models.DateTimeField(auto_now=True, verbose_name='Дата')

    def __unicode__(self):
        return self.title


class Npa(models.Model):
    class Meta:
        ordering = '-date'.split()
        verbose_name = 'НПА'
        verbose_name_plural = 'НПА'
    name = models.CharField(max_length=100, verbose_name='Приказ')
    number = models.CharField(max_length=100, verbose_name='Номер')
    text = RedactorField(verbose_name='Текст',
                         upload_to=image_upload_to,
                         # redactor_options={'buttons': ['image'],},
                         allow_image_upload=True,
                         allow_file_upload=True)
    date = models.DateTimeField(auto_now=True, verbose_name='Дата')
    file = models.FileField(upload_to=image_upload_to, blank=True, null=True, verbose_name='Файл')

    def __unicode__(self):
        return self.name


class Education(models.Model):
    class Meta:
        ordering = '-date'.split()
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
    choices = (
        ('ПДМО', 'ПДМО'),
        ('НМО', 'НМО')
    )
    category = models.CharField(choices=choices,
                                max_length=100, verbose_name='Категория')
    name = models.CharField(max_length=100, verbose_name='Заголовок')
    text = RedactorField(verbose_name='Текст',
                         upload_to=image_upload_to,
                         # redactor_options={'buttons': ['image'],},
                         allow_image_upload=True,
                         allow_file_upload=True)
    date = models.DateTimeField(auto_now=True, verbose_name='Дата')
    file = models.FileField(upload_to=image_upload_to, blank=True, null=True, verbose_name='Файл')

    def __unicode__(self):
        return self.name


class Atestation(models.Model):
    class Meta:
        ordering = '-date'.split()
        verbose_name = 'аттестация'
        verbose_name_plural = 'аттестации'
    name = models.CharField(max_length=100, verbose_name='Приказ')
    number = models.CharField(max_length=100, verbose_name='Номер')
    text = RedactorField(verbose_name='Текст',
                         upload_to=image_upload_to,
                         # redactor_options={'buttons': ['image'],},
                         allow_image_upload=True,
                         allow_file_upload=True)
    date = models.DateTimeField(auto_now=True, verbose_name='Дата')

    def __unicode__(self):
        return self.name


class Protocol(models.Model):
    class Meta:
        ordering = '-date'.split()
        verbose_name = 'протокол'
        verbose_name_plural = 'протоколы'
    name = models.CharField(max_length=100, verbose_name='Отделение')
    text = RedactorField(verbose_name='Текст',
                         upload_to=image_upload_to,
                         # redactor_options={'buttons': ['image'],},
                         allow_image_upload=True,
                         allow_file_upload=True)
    date = models.DateTimeField(auto_now=True, verbose_name='Дата')

    def __unicode__(self):
        return self.name
