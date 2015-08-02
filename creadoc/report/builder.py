# coding: utf-8
from creadoc.report.document import CreaDoc

__author__ = 'damirazo <me@damirazo.ru>'


class CreaDocBuilder(object):
    u"""
    Сборщик печатной формы
    """

    def __init__(self, report):
        self.report = report
        self.path = self.report.template.path
        self.document = CreaDoc(self.path)

    def build(self, mapper):
        available_tags = self.document.wrapper.tags
        self.document.wrapper._normalize_runs()
        pass
