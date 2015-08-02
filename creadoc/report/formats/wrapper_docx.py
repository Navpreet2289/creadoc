# coding: utf-8
from operator import attrgetter
from docx import Document
from creadoc.report.constants import RE_TAG_TEMPLATE, OPEN_TAG, CLOSE_TAG
from creadoc.report.formats.interface import CreaDocFormatWrapper

__author__ = 'damirazo <me@damirazo.ru>'


class DocxCreaDocFormatWrapper(CreaDocFormatWrapper):
    u"""
    Класс-обертка для работы с документами в формате docx
    """

    def main(self):
        self.document = Document(self.source_path)

    @property
    def tags(self):
        u"""
        Список тегов внутри документа
        """
        return RE_TAG_TEMPLATE.findall(self._full_text())

    def replace_tags(self, params):
        u"""
        Замена тегов в документе на указанные значения
        """
        # Перед сборкой требуется "нормализовать" документ,
        # объединив все "раны", в которых находятся теги
        self._normalize_runs()

    def save(self, path):
        u"""
        Сохранение документа
        """
        pass

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

    def _normalize_runs(self):
        u"""
        Нормализация "ранов" в документе.
        Требуется по причине того, что один тег может быть разбит сразу
        по нескольким "ранам" по различным причинам
        (элементы орфографического словаря, различные стили для символов).
        Поэтому нам необходимо найти все "раны", из которых состоит тег,
        затем объединить их всех в один "ран".
        """
        storage = []

        for paragraph in self.document.paragraphs:
            tag_started = False
            current_tag = u''

            start_index = 0
            end_index = 0

            for i, run in enumerate(paragraph.runs):
                if OPEN_TAG in run.text:
                    start_index = i
                    tag_started = True

                if tag_started:
                    current_tag += run.text

                if CLOSE_TAG in run.text:
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
