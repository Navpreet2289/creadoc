# coding: utf-8
from copy import copy, deepcopy
from operator import attrgetter
from docx import Document
from creadoc.enums import SourceType
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
        Теги, находящиеся внутри блока цикла являются динамическими
        и не возвращаются данным методом
        """
        tags = []
        block_started = False

        for paragraph in self.document.paragraphs:
            for run in paragraph.runs:
                if RE_START_CYCLE_TEMPLATE.match(run.text):
                    block_started = True

                if RE_END_CYCLE_TEMPLATE.match(run.text):
                    block_started = False

                # Учитываем только теги,
                # которые находятся за пределами блока цикла
                if not block_started and RE_TAG_TEMPLATE.match(run.text):
                    tags.append(RE_TAG_TEMPLATE.findall(run.text)[0])

        return tags

    def has_tag(self, tag_name):
        for tag, modifier, _ in self.tags():
            if tag == tag_name:
                return True

        return False

    def sources(self):
        u"""
        Список источников данных верхнего уровня
        """
        result = {}

        for joined_tags in self.tags():
            segments = joined_tags[0].split('.')
            root_tag = segments[0]

            source = SourceRegistry.source_by_tag(root_tag)
            result[root_tag] = source

        return result

    def save(self, path):
        u"""
        Сохранение документа
        """
        self.document.save(path)

    def replace_tags(self, params):
        u"""
        Замена тегов на указанные эквиваленты в шаблоне
        """
        for paragraph in self.document.paragraphs:
            for run in paragraph.runs:
                if RE_TAG_TEMPLATE.match(run.text):
                    tag_name = RE_TAG_TEMPLATE.findall(run.text)[0][0]

                    if not self.has_tag(tag_name):
                        continue

                    run.text = params.get(tag_name, '')

    def prepare_cycles(self):
        u"""
        Обработка циклов
        """
        # Глобальное смещение индексов
        # Происходит потому, что при копировании элементов в блоке с циклом
        # нам необходимо также увеличить значения всех индексов
        global_shift_index = 0
        # Получение реального индекса на основе глобального
        index = lambda num: num + global_shift_index

        for cycle in self.cycles():
            # Параметры цикла:
            # 1. Внешнее наименование списочного тега
            # 2. Наименование тега на каждой итерации
            # для одного из объектов цикла
            tag, inner_tag = cycle['params'][0]

            # Индекс параграфа, с которого начинается блок цикла
            begin_paragraph = index(cycle['begin_paragraph'])
            # Индекс параграфа, на котором завершается блок цикла
            end_paragraph = index(cycle['end_paragraph'])
            # Индекс рана, в котором начинается блок цикла
            begin_run = cycle['begin_run']
            # Индекс рана, в котором завершается блок цикла
            end_run = cycle['end_run']

            source = SourceRegistry.source_by_tag(tag)

            if source.type != SourceType.LIST:
                raise CreaDocException(
                    u'"{}" не является списочным тегом!'.format(source.tag))

            # Срез всех параграфов, которые входят в блок цикла
            paragraphs = self.document.paragraphs[
                begin_paragraph + 1: end_paragraph
            ]

            _p = []

            for i, paragraph in enumerate(paragraphs, start=begin_paragraph + 1):
                _p.append(deepcopy(paragraph))

            rows = source.harvest_data()
            end_of_block = self.document.paragraphs[end_paragraph - 1]

            for i, row in enumerate(rows, start=1):
                # Для первой итерации нет необходимости
                # производить вставку параграфов
                if i > 1:
                    prev_p = end_of_block
                    for p in _p:
                        prev_p._p.addnext(p._p)
                        prev_p = p

                        global_shift_index += 1

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
        # TODO: Не находит теги, перенесенные в другие параграфы
        params = []
        cycle_block_started = False
        current_tag = {}

        for p_num, paragraph in enumerate(self.document.paragraphs):
            for r_num, run in enumerate(paragraph.runs):
                text = run.text

                if RE_START_CYCLE_TEMPLATE.search(text):
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

                if RE_END_CYCLE_TEMPLATE.search(text):
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

            has_tag = any([
                open_tag in paragraph.text,
                close_tag in paragraph.text,
            ])

            # Пропускаем параграфы, которые не содержат теги
            if not has_tag:
                continue

            # Ссылка на предыдущий ран
            prev_run = None

            for i, run in enumerate(paragraph.runs):
                has_open_tag = lambda: (
                    open_tag in run.text
                    or (prev_run and open_tag in prev_run.text + run.text)
                )
                has_close_tag = lambda: (
                    close_tag in run.text
                    or (prev_run and close_tag in prev_run.text + run.text)
                )

                if has_open_tag:
                    start_index = i
                    tag_started = True

                if tag_started:
                    current_tag += run.text

                if has_close_tag:
                    end_index = i
                    tag_started = False

                    storage.append({
                        'text': current_tag,
                        'start': start_index,
                        'end': end_index,
                        'paragraph': paragraph,
                    })

                prev_run = run

        for element in storage:
            paragraph = element['paragraph']
            start = element['start']
            end = element['end']
            text = element['text']

            start_run = paragraph.runs[start]
            start_run.text = text

            for x in xrange(start + 1, end + 1):
                paragraph.runs[x].text = ''
