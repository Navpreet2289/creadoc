# coding: utf-8
import abc

__author__ = 'damirazo <me@damirazo.ru>'


class CreaDocFormatWrapper(object):
    u"""
    Интерфейс для класса-обертки документа

    "Цикл жизни" класса:
    wrapper = CustomCreaDocFormatWrapper(path='/some/path')

    """

    __metaclass__ = abc.ABCMeta

    def __init__(self, path):
        self.source_path = path
        self.document = None

        self.main()

    def main(self):
        u"""
        Кастомная инициализация класса
        """
        pass

    def tags(self):
        u"""
        Список всех тегов, доступных в рамках документа
        """
        raise NotImplementedError

    def replace_tags(self, params):
        u"""
        Замена всех тегов на доступные им значения
        """
        raise NotImplementedError

    def save(self, path):
        raise NotImplementedError
