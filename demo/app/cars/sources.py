# coding: utf-8
from creadoc.registry.source import Source, AttributeSource

__author__ = 'damirazo <me@damirazo.ru>'


class CarSource(Source):
    tag = u'Автомобиль'
    fields = {
        u'Наименование': AttributeSource('marka'),
    }
