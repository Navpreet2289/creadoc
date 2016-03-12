# coding: utf-8

__author__ = 'damirazo <me@damirazo.ru>'


class Variable(object):
    u"""
    Базовый класс для шаблонной переменной
    """

    name = None
    category = None
    description = None

    def __init__(self, name, category, description):
        assert name is not None, u'Требуется задать имя переменной!'

        self.name = name
        self.category = category
        self.description = description

    def value(self):
        raise NotImplementedError(u'Требуется реализовать метод value!')
