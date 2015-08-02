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
TAG_TEMPLATE = '{}\s*([\w\d\.а-яА-Я_]+)(:?\{}(\w+))?\s*{}'.format(
    OPEN_TAG,
    MODIEFIER_SPLIT_TAG,
    CLOSE_TAG,
)
RE_TAG_TEMPLATE = re.compile(TAG_TEMPLATE, re.I | re.U)
