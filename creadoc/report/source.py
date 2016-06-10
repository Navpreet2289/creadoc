# coding: utf-8
from m3.actions import ControllerCache
from creadoc.report.actions import CreadocDataSourceActionPack

__author__ = 'damirazo'


class DataSource(object):
    u"""
    Базовый класс для источника данных
    """
    guid = None
    u"""
    Уникальный идентификатор источника данных
    :type: None or str
    """

    name = None
    u"""
    Название источника данных
    :type: None or unicode
    """

    alias = None
    u"""
    Псевдоним источника данных, используется в шаблонах
    :type: None or str
    """

    def load(self, request, context):
        u"""
        Загрузка данных из источника.
        В случае отсутствия данных используется значение по умолчанию.
        """
        return (
            self.data(request, context) or self.default_value(request, context)
        )

    def data(self, request, context):
        u"""
        Формирование набора данных для заполнения источника
        """
        raise NotImplementedError

    def default_value(self, request, context):
        u"""
        Значение источника данных по умолчанию.
        Используется в случае отсутствия данных.
        """
        raise NotImplementedError

    @property
    def url(self):
        u"""
        URL для загрузки источника данных
        """
        pack = ControllerCache.find_pack(CreadocDataSourceActionPack)

        return '{}?source_guid={}'.format(
            pack.action_router.get_absolute_url(),
            self.guid,
        )
