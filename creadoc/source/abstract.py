# coding: utf-8
import abc

__author__ = 'damirazo <me@damirazo.ru>'


class AbstractDataSource(object):
    __metaclass__ = abc.ABCMeta

    type = None
    name = None
    category = None
    description = None

    @abc.abstractmethod
    def data(self):
        raise NotImplementedError
