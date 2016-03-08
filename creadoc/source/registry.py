# coding: utf-8
__author__ = 'damirazo <me@damirazo.ru>'


class DataSourceRegistry(object):
    u"""
    Реестр источников данных
    """

    __data = []
    __data_by_name = {}

    @classmethod
    def register(cls, *data_sources):
        for data_source in data_sources:
            cls.__data.append(data_source)
            cls.__data_by_name[data_source.name] = data_source

    @classmethod
    def get_by_name(cls, name):
        return cls.__data_by_name.get(name)

    @classmethod
    def all(cls):
        return cls.__data


DSR = DataSourceRegistry
