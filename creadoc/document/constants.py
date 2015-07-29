# coding: utf-8
import re

__author__ = 'damirazo <me@damirazo.ru>'


# Паттерн для поиска тегов в шаблоне
RE_TAGS = re.compile('{{\s*([\w\d\.а-яА-ЯйЙёЁ]+?)\s*}}', re.I | re.U)
