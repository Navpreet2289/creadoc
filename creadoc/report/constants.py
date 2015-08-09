# coding: utf-8
import re

__author__ = 'damirazo <me@damirazo.ru>'


# Признак открытия тега
OPEN_TAG = '{{'
# Признак закрытия тега
CLOSE_TAG = '}}'
# Разделитель между тегом и модификатором
MODIEFIER_SPLIT_TAG = '|'

# Паттерн для поиска тегов в шаблоне
# Первый возвращаемый элемент - наименование тега
# Второй возвращаемый элемент - наименование модификатора
TAG_TEMPLATE = u'{}\s*([\w\d\.а-яА-Я_]+)(:?\{}(\w+))?\s*{}'.format(
    OPEN_TAG,
    MODIEFIER_SPLIT_TAG,
    CLOSE_TAG,
)
RE_TAG_TEMPLATE = re.compile(TAG_TEMPLATE, re.I | re.U)

# Признак открытия блочного тега
OPEN_BLOCK_TAG = '{%'
# Признак закрытия блочного тега
CLOSE_BLOCK_TAG = '%}'

# Текст обозначения начала цикла
# Синтаксис:
# {% НачалоЦикла СписокЗаписей Запись %}
# {{ Запись.Название }}
# {% КонецЦикла %}
# Где "СписокЗаписей" наименование списочного тега,
# "Запись" наименование тега внутри блока цикла
START_CYCLE_TEXT = u'НачалоЦикла'
START_CYCLE_TEMPLATE = (
    u'{}\s*{}\s+?([\w\d\а-яА-Я]+)\s+([\w\d\а-яА-Я]+)\s*{}'
).format(
    OPEN_BLOCK_TAG,
    START_CYCLE_TEXT,
    CLOSE_BLOCK_TAG,
)
RE_START_CYCLE_TEMPLATE = re.compile(START_CYCLE_TEMPLATE, re.I | re.U)

# Текст обозначения окончания цикла
END_CYCLE_TEXT = u'КонецЦикла'
END_CYCLE_TEMPLATE = u'{}\s*{}\s*{}'.format(
    OPEN_BLOCK_TAG,
    END_CYCLE_TEXT,
    CLOSE_BLOCK_TAG,
)
RE_END_CYCLE_TEMPLATE = re.compile(END_CYCLE_TEMPLATE, re.I | re.U)
