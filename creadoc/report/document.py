# coding: utf-8
import os
from creadoc.report.formats.wrapper_docx import DocxCreaDocFormatWrapper
from creadoc.exceptions import DocumentWrapperDoesNotExist

__author__ = 'damirazo <me@damirazo.ru>'


class CreaDocWrapperFabric(object):
    u"""
    Фабрика, возвращающая готовую обертку для указанного типа файла
    """

    # Соответствие расширения файла и класса-обертки для данного файла
    _wrappers = {
        'docx': DocxCreaDocFormatWrapper,
    }

    @classmethod
    def register_wrapper(cls, extension, wrapper_cls):
        u"""
        Регистрация новой обертки для указанного расширения
        При использовании уже зарегистрированного расширения
        существует возможность перезаписать обертку
        """
        cls._wrappers[extension] = wrapper_cls

    @classmethod
    def wrapper(cls, path):
        u"""
        Возвращает инстанцированный объект класса-обертки
        """
        if not isinstance(path, basestring):
            extension = os.path.splitext(path.name)[-1].replace('.', '')
        else:
            extension = os.path.splitext(path)[-1].replace('.', '')

        if extension in cls._wrappers:
            wrapper_cls = cls._wrappers[extension]

            return wrapper_cls(path)

        raise DocumentWrapperDoesNotExist


class CreaDoc(object):
    u"""
    Объектное представление шаблона печатной формы
    """

    def __init__(self, path_or_file):
        u"""
        :param path_or_file: Путь до шаблона или файловый дескриптор
        """
        self.path = path_or_file
        self.wrapper = CreaDocWrapperFabric.wrapper(self.path)

    def save(self, path=None):
        return self.wrapper.save(path or self.path)
