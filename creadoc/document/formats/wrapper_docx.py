# coding: utf-8
from operator import attrgetter
from docx import Document
from creadoc.document.constants import RE_TAGS
from creadoc.document.formats.interface import CreaDocFormatWrapper

__author__ = 'damirazo <me@damirazo.ru>'


class DocxCreaDocFormatWrapper(CreaDocFormatWrapper):
    u"""
    Класс-обертка для работы с документами в формате docx
    """

    def main(self):
        self.document = Document(self.source_path)

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

    @property
    def tags(self):
        u"""
        Список тегов внутри документа
        """
        return RE_TAGS.findall(self._full_text())

    def replace_tags(self, params):
        pass

    def save(self, path):
        pass
