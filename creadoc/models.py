# coding: utf-8
import datetime
from django.db import models

__author__ = 'damirazo <me@damirazo.ru>'


class CreadocReport(models.Model):
    u"""
    Запись объекта печатной формы
    """
    name = models.CharField(
        max_length=255,
        verbose_name=u'Наименование печатной формы')
    shortname = models.CharField(
        max_length=255,
        verbose_name=u'Ссылка на пак')
    root_source = models.CharField(
        max_length=255,
        null=True,
        verbose_name=u'Корневой источник данных')
    template = models.FileField(
        upload_to='report_templates',
        verbose_name=u'Шаблон печатной формы')
    begin = models.DateField(
        default=datetime.date.min,
        verbose_name=u'Дата начала действия печатной формы')
    end = models.DateField(
        default=datetime.date.max,
        verbose_name=u'Дата окончания действия печатной формы')

    class Meta:
        db_table = 'creadoc_report'
        verbose_name = u'Печатная форма'
        verbose_name_plural = u'Печатные формы'
