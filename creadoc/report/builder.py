# coding: utf-8
from creadoc.helper.tags import get_by_key
from creadoc.registry.source import SourceRegistry
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
        u"""
        Сборка печатной формы
        """
        # Нормализация документа
        self.document.wrapper.normalize()

        # Обработка обычных тегов
        self.prepare_tags()
        # Обработка списочных тегов
        self.prepare_cycles()

        return self.document

    def data_formation(self):
        u"""
        Формирование данных по тегам
        """
        to_replace = {}
        values = self.mapper.fill(self.document.wrapper.sources())

        for tag_data in self.document.wrapper.tags():
            tag_name = tag_data[1]
            segments = tag_name.split('.')
            value = get_by_key(values, segments)
            to_replace[tag_name] = value or ''

        return to_replace

    def prepare_tags(self):
        u"""
        Обработка обычных тегов
        """
        self.document.wrapper.replace_tags(self.data_formation())

    def prepare_cycles(self):
        u"""
        Обработка списочных тегов
        """
        self.document.wrapper.prepare_cycles()
