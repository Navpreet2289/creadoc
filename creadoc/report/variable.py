# coding: utf-8

__author__ = 'damirazo <me@damirazo.ru>'


class VariableType(object):
    u"""
    Перечисление типов переменных
    В качестве значения используется наименование типа из javascript
    """
    STRING = 'String'
    INT = 'Stimulsoft.System.Int32'
    DECIMAL = 'Stimulsoft.System.Decimal'
    DATETIME = 'Stimulsoft.System.DateTime'
    BOOL = 'Boolean'


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
