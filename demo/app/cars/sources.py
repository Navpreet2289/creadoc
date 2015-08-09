# coding: utf-8
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
