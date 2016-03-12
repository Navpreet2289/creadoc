# coding: utf-8
from django.db import models

__author__ = 'damirazo <me@damirazo.ru>'


class CreadocReport(models.Model):
    u"""
    Модель шаблона отчетной формы
    """
    guid = models.CharField(
        max_length=128,
        verbose_name=u'Уникальный идентификатор шаблона',
        unique=True,
    )
    name = models.CharField(
        max_length=128,
        verbose_name=u'Наименование шаблона'
    )

    class Meta:
        db_table = 'creadoc_report'
        verbose_name = u'Шаблон отчетной формы'
        verbose_name_plural = u'Шаблоны отчетных форм'
