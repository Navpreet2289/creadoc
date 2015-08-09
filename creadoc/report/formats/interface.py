# coding: utf-8
import abc

__author__ = 'damirazo <me@damirazo.ru>'


class CreaDocFormatWrapper(object):
    u"""
    Интерфейс для класса-обертки документа
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

    def sources(self):
        u"""
        Список всех источников данных верхнего уровня, доступных в документе
        """
        pass

    def save(self, path):
        u"""
        Сохранение документа
        """
        raise NotImplementedError
