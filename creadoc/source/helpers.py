# coding: utf-8
from creadoc.source.variable import VariableDataSource
from creadoc.source.enums import DataSourceTypeEnum

__author__ = 'damirazo <me@damirazo.ru>'


BASE_CATEGORY = u'Общие переменные'


def variable_creator(name, value, category=None, description=None):
    u"""
    Формирование переменной, возвращающего один объект
    :param name: Наименование источника данных
    :param value: Значение, возвращаемое источником данных
    :param category: Наименование категории
    :param description: Описание переменной
    :return: ElementDataSource
    """
    data_source = VariableDataSource()
    data_source.type = DataSourceTypeEnum.VARIABLE
    data_source.name = name
    data_source.data = lambda: value
    data_source.category = category or BASE_CATEGORY
    data_source.description = description or u''

    return data_source
