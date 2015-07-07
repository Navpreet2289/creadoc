# coding: utf-8
__author__ = 'damirazo <me@damirazo.ru>'


class CreaDocException(Exception):
    u"""
    Базовое исключение
    """


class SourceTagDuplicateException(CreaDocException):
    u"""
    Обнаружено несколько источников данных с одинаковым тегом
    """


class SourceValidationException(CreaDocException):
    u"""
    Ошибка при валидации источника данных
    """