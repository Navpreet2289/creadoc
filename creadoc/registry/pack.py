# coding: utf-8
import datetime
from creadoc.helper.cls import Singletone
from creadoc.models import CreadocReport

__author__ = 'damirazo <me@damirazo.ru>'


@Singletone
class PackRegistry(object):
    u"""
    Реестр паков, в которые возможно добавление печатных форм
    """

    _packs = {}

    def add(self, *packs):
        for params in packs:
            shortname = params[0].get_short_name()
            name = params[1]

            param_window = None
            if len(params) > 2:
                param_window = params[2]

            if shortname not in self._packs:
                item = PackRegistryItem(
                    shortname=shortname,
                    name=name,
                    param_window=param_window,
                )
                self._packs[item.shortname] = item

    def items(self):
        return self._packs.iteritems()


class PackRegistryItem(object):
    u"""
    Элемент реестра паков
    """

    __slots__ = ['shortname', 'name', 'param_window']

    def __init__(self, shortname, name, param_window=None):
        self.shortname = shortname
        self.name = name
        self.param_window = param_window

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
