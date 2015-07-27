# coding: utf-8
import datetime
from creadoc.models import CreadocReport

__author__ = 'damirazo <me@damirazo.ru>'


class PackRegistry(object):
    u"""
    Реестр паков, в которые возможно добавление печатных форм
    """

    _packs = {}

    @classmethod
    def add(cls, *packs):
        u"""
        Добавление списка паков для регистрации в реестре
        """
        for params in packs:
            shortname = params[0].get_short_name()
            name = params[1]

            if shortname not in cls._packs:
                item = PackRegistryItem(
                    shortname=shortname,
                    name=name,
                )
                cls._packs[item.shortname] = item

    @classmethod
    def items(cls):
        return cls._packs.iteritems()


class PackRegistryItem(object):
    u"""
    Элемент реестра паков
    """

    __slots__ = ['shortname', 'name']

    def __init__(self, shortname, name):
        self.shortname = shortname
        self.name = name

    def reports(self, date=None):
        u"""
        Возвращает все доступные указанному паку печатные формы,
        актуальные на указанную дату
        """
        if date is None:
            date = datetime.date.today()

        return CreadocReport.objects.filter(
            shortname=self.shortname,
            begin__lte=date,
            end__gte=date,
        )
