# coding: utf-8
from creadoc.source.constants import BASE_CATEGORY
from creadoc.source.data_source import DataSource
from creadoc.source.variable import Variable

__author__ = 'damirazo <me@damirazo.ru>'


def variable_creator(name, value, category=None, description=None):
    u"""
    Формирование переменной, возвращающего один объект
    :param name: Наименование источника данных
    :param value: Значение, возвращаемое источником данных
    :param category: Наименование категории
    :param description: Описание переменной
    :return: ElementDataSource
    """
    variable = Variable(
        name=name,
        category=category or BASE_CATEGORY,
        description=description or u'',
    )

    if callable(value):
        variable.value = value
    else:
        variable.value = lambda: value

    return variable


def source_creator(guid, name, url):
    data_source = DataSource()
    data_source.guid = guid
    data_source.url = url
    data_source.name = name

    return data_source
