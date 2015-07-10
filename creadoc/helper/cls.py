# coding: utf-8
__author__ = 'damirazo <me@damirazo.ru>'


class Singletone(object):
    u"""
    Класс-помощник, облегчающий создание классов-одиночек
    """

    def __init__(self, cls):
        self._cls = cls

    def instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self, *args, **kwargs):
        raise TypeError(
            u'Запрещено прямое создание экземпляра, '
            u'используйте метод instance!'
        )

    def __instancecheck__(self, instance):
        return isinstance(instance, self._cls)
