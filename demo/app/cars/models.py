# coding: utf-8
from django.db import models

__author__ = 'damirazo <me@damirazo.ru>'


class Car(models.Model):
    u"""
    Модель записей об автомобиле
    """
    marka = models.CharField(max_length=128, verbose_name=u'Марка автомобиля')
    seria = models.CharField(max_length=128, verbose_name=u'Серия автомобиля')
    year = models.IntegerField(verbose_name=u'Год выпуска')

    class Meta:
        db_table = 'demo_car'
        verbose_name = u'Автомобиль'
        verbose_name_plural = u'Автомобили'
