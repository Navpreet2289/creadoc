# coding: utf-8
from creadoc.exceptions import SourceCanNotBeFilled

__author__ = 'damirazo <me@damirazo.ru>'


class CreaDocMapper(object):
    u"""
    Класс-заполнитель
    """

    def __init__(self, context):
        self.context = context

    def values(self, sources):
        result = {}

        for source in sources:
            context_name = source.context_name

            if context_name is not None:
                try:
                    value = getattr(self.context, context_name)
                except AttributeError:
                    raise SourceCanNotBeFilled((
                        u'Источник данных {} не удалось заполнить. '
                        u'Отсутствует значение {} в контексте!'
                    ).format(source.tag, context_name))
