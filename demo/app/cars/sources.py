# coding: utf-8
from creadoc.enums import SourceType
from creadoc.registry.source import Source, AttributeSource
from demo.app.cars.models import Car

__author__ = 'damirazo <me@damirazo.ru>'


class CarSource(Source):
    u"""
    Демонстрационный источник данных
    """
    tag = u'Автомобиль'
    fields = [
        AttributeSource(u'Наименование', 'marka'),
    ]
    context_name = 'row_id'

    def data(self):
        return Car.objects.get(pk=self.initial_value)


class VacationListSource(Source):
    tag = u'СписокОтпусков'
    type = SourceType.LIST

    def data(self):
        return [
            {
                u'ДатаНачала': '01.10.2010',
                u'ДатаОкончания': '10.10.2010',
            },
            {
                u'ДатаНачала': '01.11.2011',
                u'ДатаОкончания': '11.11.2011',
            },
            {
                u'ДатаНачала': '01.12.2012',
                u'ДатаОкончания': '12.12.2012',
            },
        ]
