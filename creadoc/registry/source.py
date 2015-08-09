# coding: utf-8
import abc
from creadoc.enums import SourceType
from creadoc.exceptions import (
    SourceValidationException,
    SourceTagDuplicateException)

__author__ = 'damirazo <me@damirazo.ru>'


class SourceRegistry(object):
    u"""
    Реестр источников данных
    """

    # Зарегистрированные источники данных
    _data = {}

    @classmethod
    def register(cls, source):
        u"""
        Регистрация источника данных в реестре
        """
        assert isinstance(source, Source), (
            u'Источник данных должен являться потомком класса Source')

        tag = source.tag

        if tag in cls._data:
            raise SourceTagDuplicateException((
                u'Тег {} уже используется в источнике данных {}'
            ).format(tag, cls._data[tag].__name__))

        cls._data[tag] = source

    @classmethod
    def source_by_tag(cls, tag):
        u"""
        Поиск источника данных с указанным тегом
        """
        return cls._data.get(tag)

    @classmethod
    def sources(cls):
        u"""
        Список всех зарегистрированных источников данных
        """
        return cls._data


class Source(object):
    u"""
    Абстрактный класс источника данных
    """
    __metaclass__ = abc.ABCMeta

    # Наименование тега,
    # которому будет сопоставляться этот источник данных в шаблоне
    tag = None
    # Поля источника данных.
    # В свою очередь могут сами являться источниками данных.
    fields = None
    # Ссылка на родительский источник данных
    parent = None
    # Наименование параметра контекста,
    # на основе которого будет заполнятся данный источник данных.
    # Имеет смысл только для источников верхнего уровня.
    context_name = None
    # Инициирующее значение, заданное классом-заполнителем,
    # на основе которой формируется значение источника данных
    initial_value = None
    # Тип источника данных (обычный/списочный)
    type = SourceType.SINGLE

    def fill(self, initial_value=None):
        u"""
        Заполнение инициирующего значения
        """
        self.initial_value = initial_value

    def harvest_data(self, parent=None):
        u"""
        Метод, возвращающий сформированный набор данных для заполнения шаблона

        Для тега {{ Автомобиль.Наименование }}
        результатирующий набор данных будет:
        {u'Автомобиль': {u'Наименование': 'Ford Focus'}}
        """
        result = {}

        self.parent = parent

        if self.fields is not None:
            for source in self.fields:
                result[source.tag] = source.harvest_data(self)
        else:
            result = self.data()

        return result

    def data(self):
        u"""
        Метод, возвращающий значение источника данных
        """
        raise NotImplementedError

    @classmethod
    def check_children(cls, fields):
        u"""
        Проверка на наличие указанной иерархии в дочерних полях
        """
        checked_field = fields[0]
        children_fields = fields[1:]

        # Проверяем, что заявлено наличие потомка у указанного источника
        # и при этом у него есть потомки
        if checked_field and not cls.fields:
            raise SourceValidationException

        # Проверяем что указанный потомок есть в списке потомков
        # данного источника
        elif cls.fields and not cls.has_children(checked_field):
            raise SourceValidationException

        # Проверяем, что еще остались потомки
        elif children_fields:
            cls.fields[checked_field].check_children(children_fields)

    @classmethod
    def has_children(cls, tag):
        u"""
        Проверка наличия потомка с указанным именем
        """
        for field in cls.fields:
            if field.tag == tag:
                return True

        return False


class AttributeSource(Source):
    u"""
    Источник данных, возвращающий значение атрибута
    с указанным именем у родительского источника данных
    """

    def __init__(self, tag_name, attr_name):
        self.tag = tag_name
        self.attr_name = attr_name

    def data(self):
        return getattr(self.parent.data(), self.attr_name, '')
