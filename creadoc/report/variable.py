# coding: utf-8

__author__ = 'damirazo <me@damirazo.ru>'


class Variable(object):
    u"""
    Базовый класс для шаблонной переменной
    """

    def __init__(self, name, category, description, v_type):
        self.name = name
        self.category = category
        self.description = description
        self.type = v_type

    def value(self):
        raise NotImplementedError(u'Требуется реализовать метод value!')
