# coding: utf-8
import os
import uuid
from django.conf import settings
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
    def wrapper(cls, path, extension):
        u"""
        Возвращает инстанцированный объект класса-обертки
        """
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
        self._base_path = path_or_file

        self.path = self.file_path()
        self.name = self.file_name()
        self.extension = self.file_extension()

        self.wrapper = CreaDocWrapperFabric.wrapper(
            self._base_path, self.extension)

    def file_path(self):
        u"""
        Путь до файла
        """
        path = self._base_path

        return isinstance(path, basestring) and path or path.name

    def file_name(self):
        u"""
        Наименование файла
        """
        return os.path.basename(self.path).split('.')[0]

    def file_extension(self):
        u"""
        Расширение файла
        """
        return os.path.splitext(self.path)[-1].replace('.', '')

    def download_url(self, name):
        u"""
        Генерация пути для скачивания файла
        """
        return os.path.join(
            settings.MEDIA_URL,
            name,
        )

    def uniq_name(self):
        u"""
        Генерация уникального наименования файла
        """
        return u'{}_{}.{}'.format(
            self.name,
            uuid.uuid4().get_hex(),
            self.extension)

    def save(self):
        u"""
        Сохранение шаблона
        Возвращает путь до сгенерированного шаблона
        """
        uniq_name = self.uniq_name()

        path = os.path.join(
            settings.MEDIA_ROOT,
            uniq_name,
        )

        self.wrapper.save(path)

        return self.download_url(uniq_name)
