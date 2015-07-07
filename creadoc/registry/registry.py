# coding: utf-8
from creadoc.exceptions import SourceTagDuplicateException
from creadoc.registry.source import Source

__author__ = 'damirazo <me@damirazo.ru>'


class SourceRegistry(object):
    u"""
    Реестр источников данных
    """

    _data = {}

    def __new__(cls, *args, **kwargs):
        raise RuntimeError(
            u'Инстанцирование класса {} запрещено!'.format(cls.__name__)
        )

    @classmethod
    def register(cls, source):
        assert issubclass(source, Source), (
            u'Источник данных должен являться потомком класса Source')

        tag = source.tag

        if tag in cls._data:
            raise SourceTagDuplicateException((
                u'Тег {} уже используется в источнике данных {}'
            ).format(tag, cls._data[tag].__name__))

        cls._data[tag] = source

    @classmethod
    def source_by_tag(cls, tag):
        return cls._data.get(tag)

    @classmethod
    def source_by_full_tag(cls, full_tag):
        pass

    @classmethod
    def sources(cls):
        return cls._data


class PackRegistry(object):
    u"""
    Реестр паков, в которые возможно добавление печатных форм
    """

    _packs = {}

    @classmethod
    def add(cls, *packs):
        for pack, title in packs:
            if pack.url not in cls._packs:
                cls._packs[pack.get_short_name()] = title

    @classmethod
    def items(cls):
        return cls._packs.iteritems()
