# coding: utf-8
from operator import attrgetter
from creadoc.models import CreadocReportDataSource
from creadoc.source.exceptions import (
    DuplicateVariableException, DuplicateDataSourceException)

__author__ = 'damirazo <me@damirazo.ru>'


class DataSourceRegistry(object):
    u"""
    Реестр источников данных
    """

    # Список зарегистрированных переменных
    __variables = []
    # Список зарегистрированных источников данных
    __sources = []
    __source_groups = {}

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
        u"""
        Перечисление всех зарегистрированных переменных
        """
        return cls.__variables

    @classmethod
    def add_sources(cls, *sources):
        u"""
        Регистрация источников данных в реестре
        :param sources: Перечисление источников данных
        """
        for source in sources:
            if source.group in cls.__source_groups:
                raise DuplicateDataSourceException((
                    u'Источник данных с именем "{}" '
                    u'уже зарегистрирован в реестре в источнике данных "{}"'
                ).format(
                    source.group,
                    cls.__source_groups[source.group].__class__.__name__,
                ))

            cls.__sources.append(source)
            cls.__source_groups[source.group] = source

    @classmethod
    def sources(cls):
        u"""
        Перечисление всех зарегистрированных источников данных
        """
        return cls.__sources

    @classmethod
    def connected_sources(cls, report_id):
        u"""
        Список всех подключенных к шаблону с указанным id источников данных
        Для нового шаблона список будет пустым
        :param report_id: Идентификатор шаблона
        :return:
        """
        result = []
        connected_source_ids = CreadocReportDataSource.objects.filter(
            report__id=report_id
        ).values_list('source_uid', flat=True)

        for source in cls.__sources:
            if source.guid in connected_source_ids:
                result.append(source)

        return result


DSR = DataSourceRegistry
