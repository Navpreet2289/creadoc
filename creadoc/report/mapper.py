# coding: utf-8
from creadoc.exceptions import SourceCanNotBeFilled

__author__ = 'damirazo <me@damirazo.ru>'


class CreaDocMapper(object):
    u"""
    Заполнитель источников данных на основе значений из `ActionContext`
    """

    def __init__(self, context):
        self.context = context

    def fill(self, sources):
        u"""
        Инициализация источников данных стартовыми значениями
        Возвращает словарь, где в качестве ключа содержится наименование тега,
        в качестве значения заполненная структура,
        возвращенная источником данных
        """
        result = {}

        for tag, source in sources.iteritems():
            if source is None:
                continue

            context_name = source.context_name

            if context_name is not None:
                try:
                    value = getattr(self.context, context_name)
                except AttributeError:
                    raise SourceCanNotBeFilled((
                        u'Источник данных {} не удалось заполнить. '
                        u'Отсутствует значение {} в контексте!'
                    ).format(source.tag, context_name))

                source.fill(value)

            result[source.tag] = source.harvest_data()

        return result
