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
        pass

    def prepare_cycles(self):
        for cycle in self.document.wrapper.cycles():
            pass
