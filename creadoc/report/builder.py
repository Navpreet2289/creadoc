# coding: utf-8
from creadoc.report.document import CreaDoc

__author__ = 'damirazo <me@damirazo.ru>'


class CreaDocBuilder(object):
    u"""
    Сборщик печатной формы
    """

    def __init__(self, report, mapper):
        self.report = report
        self.path = self.report.template.path
        self.document = CreaDoc(self.path)
        self.mapper = mapper

    def build(self):
        self.document.wrapper.normalize()

        self.prepare_tags()
        self.prepare_cycles()

    def prepare_tags(self):
        values = self.mapper.fill(self.document.wrapper.sources())

        for joined_tag in self.document.wrapper.tags():
            segments = joined_tag[0].split('.')
            root_tag = segments[0]

            value = self.get_by_key(values, segments)
            pass

    def prepare_cycles(self):
        for cycle in self.document.wrapper.cycles():
            pass

    def get_by_key(self, data, path):
        u"""
        Возвращает значение с указанным ключем
        """
        result = reduce(
            lambda dct, k: dct and dct.get(k) or None,
            path, data)

        return result
