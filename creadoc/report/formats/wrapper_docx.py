# coding: utf-8
from operator import attrgetter
from docx import Document
from creadoc.exceptions import CreaDocException
from creadoc.registry.source import SourceRegistry
from creadoc.report.constants import (
    RE_TAG_TEMPLATE, OPEN_TAG, CLOSE_TAG,
    RE_START_CYCLE_TEMPLATE, RE_END_CYCLE_TEMPLATE,
    CLOSE_BLOCK_TAG, OPEN_BLOCK_TAG)
from creadoc.report.formats.interface import CreaDocFormatWrapper

__author__ = 'damirazo <me@damirazo.ru>'


class DocxCreaDocFormatWrapper(CreaDocFormatWrapper):
    u"""
    Класс-обертка для работы с документами в формате docx
    """

    def main(self):
        self.document = Document(self.source_path)

    def tags(self):
        u"""
        Список тегов внутри документа
        """
        return RE_TAG_TEMPLATE.findall(self._full_text())

    def sources(self):
        u"""
        Список источников данных верхнего уровня
        """
        result = {}

        for joined_tags in self.tags():
            segments = joined_tags.split('.')
            root_tag = segments[0]

            source = SourceRegistry.source_by_tag(root_tag)
            result[root_tag] = source

        return result

    def save(self, path):
        u"""
        Сохранение документа
        """
        pass

    def normalize(self):
        u"""
        Нормализация "ранов" в документе.
        Требуется по причине того, что один тег может быть разбит сразу
        по нескольким "ранам" по различным причинам
        (элементы орфографического словаря, различные стили для символов).
        Поэтому нам необходимо найти все "раны", из которых состоит тег,
        затем объединить их всех в один "ран".
        """
        # Нормализация обычных тегов
        self._normalize_runs(OPEN_TAG, CLOSE_TAG)
        # Нормализация блочных тегов
        self._normalize_runs(OPEN_BLOCK_TAG, CLOSE_BLOCK_TAG)

    def cycles(self):
        u"""
        Получение информации о наличии блоков с циклами в документе
        """
        params = []
        cycle_block_started = False
        current_tag = {}

        for p_num, paragraph in enumerate(self.document.paragraphs):
            for r_num, run in enumerate(paragraph.runs):
                text = run.text

                if RE_START_CYCLE_TEMPLATE.match(text):
                    if cycle_block_started:
                        raise CreaDocException(
                            u'Обнаружено начало блока цикла '
                            u'до завершения другого блока цикла'
                        )

                    data = RE_START_CYCLE_TEMPLATE.findall(text)

                    cycle_block_started = True
                    current_tag = {
                        'begin_paragraph': p_num,
                        'begin_run': r_num,
                        'params': data,
                    }

                if RE_END_CYCLE_TEMPLATE.match(text):
                    if not cycle_block_started:
                        raise CreaDocException(
                            u'Обнаружен закрывающий тег блока с циклом, '
                            u'однако блок с циклом еще не открыт'
                        )

                    cycle_block_started = False
                    current_tag.update({
                        'end_paragraph': p_num,
                        'end_run': r_num,
                    })
                    params.append(current_tag)

        # Проверяем, что мы закрыли все обнаруженные теги
        if current_tag is not None and cycle_block_started:
            raise CreaDocException(u'В шаблоне имеется незакрытый тег цикла')

        return params

    def _paragraphs(self):
        u"""
        Список параграфов внутри документа
        """
        result = []

        for paragraph in self.document.paragraphs:
            result.append(u''.join(map(attrgetter('text'), paragraph.runs)))

        return result

    def _full_text(self):
        u"""
        Полный текст документа
        """
        return u'\n'.join(self._paragraphs())

    def _normalize_runs(self, open_tag, close_tag):
        u"""
        Выполнение нормализации "ранов" для тегов
        с указанными признаками открытия и закрытия
        """
        storage = []

        for paragraph in self.document.paragraphs:
            tag_started = False
            current_tag = u''

            start_index = 0
            end_index = 0

            for i, run in enumerate(paragraph.runs):
                if open_tag in run.text:
                    start_index = i
                    tag_started = True

                if tag_started:
                    current_tag += run.text

                if close_tag in run.text:
                    end_index = i
                    tag_started = False

                    storage.append({
                        'text': current_tag,
                        'start': start_index,
                        'end': end_index,
                        'paragraph': paragraph,
                    })

        for element in storage:
            paragraph = element['paragraph']
            start = element['start']
            end = element['end']
            text = element['text']

            start_run = paragraph.runs[start]
            start_run.text = text

            for x in xrange(start + 1, end + 1):
                del paragraph.runs[x]
