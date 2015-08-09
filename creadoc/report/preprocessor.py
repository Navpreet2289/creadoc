# coding: utf-8
from creadoc.report.document import CreaDoc
from creadoc.exceptions import SourceValidationException
from creadoc.registry.source import SourceRegistry

__author__ = 'damirazo <me@damirazo.ru>'


class DocumentPreprocessor(object):
    u"""
    Обработчик шаблона печатной формы
    Используется для валидации при загрузке нового шаблона
    """

    def __init__(self, document):
        u"""
        :param document: Путь до шаблона или открытый файловый дескриптор
        """
        self.document = CreaDoc(document)
        self.source_registry = SourceRegistry

    def prepare(self):
        u"""
        Обработка шаблона
        """
        # Этапы обработки

        # Нормализация документа
        self.document.wrapper.normalize()

        # 1. Анализ обнаруженных внутри документа тегов
        allowed_tags = self.check_tags()

        return allowed_tags

    def check_tags(self):
        u"""
        Валидация тегов, обнаруженных внутри документа
        Каждый источник данных способен выполнить валидацию
        своих потомков самостоятельно.
        Также существует возможность управления механизмом валидации
        на уровне любого из источников данных.
        По умолчанию управление отдается лишь тем источникам данных,
        что имеют потомков.
        """
        tags = self.document.wrapper.tags()

        result = {}

        for tag, modifier, _ in tags:
            segments = tag.split('.')
            root_tag = segments[0]

            source = self.source_registry.source_by_tag(root_tag)

            if source is None:
                result[tag] = False
                continue

            try:
                source.check_children(segments[1:])
            except SourceValidationException as exc:
                result[tag] = False
                continue

            result[tag] = True

        return result
