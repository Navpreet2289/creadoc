# coding: utf-8
import abc
from creadoc.exceptions import SourceValidationException

__author__ = 'damirazo <me@damirazo.ru>'


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
            for tag_name, source in self.fields.iteritems():
                result[tag_name] = source.harvest_data(self)
        else:
            result = self.data()

        return result

    def data(self):
        u"""
        """
        raise NotImplementedError

    @classmethod
    def validate_children(cls, fields):
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
        elif cls.fields and checked_field not in cls.fields:
            raise SourceValidationException
        # Проверяем, что еще остались потомки
        elif children_fields:
            cls.fields[checked_field].validate_children(children_fields)


class AttributeSource(Source):

    def __init__(self, attr_name):
        self.attr_name = attr_name

    def data(self):
        return getattr(self.parent, self.attr_name, 'sdfsd')
