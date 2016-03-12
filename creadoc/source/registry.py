# coding: utf-8
from operator import attrgetter
from creadoc.source.exceptions import DuplicateVariableException

__author__ = 'damirazo <me@damirazo.ru>'


class DataSourceRegistry(object):
    u"""
    Реестр источников данных
    """

    # Список зарегистрированных переменных
    __variables = []
    __sources = []

    @classmethod
    def add_variables(cls, *variables):
        u"""
        Регистрация шаблонных переменных
        :param VariableDataSource variables: Одна или несколько
            шаблонных переменных
        """
        existed_names = set(map(attrgetter('name'), cls.__variables))
        added_names = set(map(attrgetter('name'), variables))

        crossed_names = existed_names & added_names

        # Проверка на наличие возможного пересечения в именах переменных
        if crossed_names:
            raise DuplicateVariableException((
                u'Выявлено одно или несколько переменных '
                u'с одинаковыми именами: {}'
            ).format(u', '.join(crossed_names)))

        cls.__variables.extend(variables)

    @classmethod
    def variables(cls):
        return cls.__variables

    @classmethod
    def add_sources(cls, *sources):
        cls.__sources.extend(sources)

    @classmethod
    def sources(cls):
        return cls.__sources


DSR = DataSourceRegistry
