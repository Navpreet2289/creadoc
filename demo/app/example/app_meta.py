# coding: utf-8
from creadoc.source.helpers import source_creator, variable_creator
from creadoc.source.registry import DSR
from creadoc.source.variable import VariableType
from demo.app import controller
from demo.app.example.actions import ExampleDataSourceActionPack
from demo.app.helpers import get_action_url


def register_actions():
    controller.action_controller.extend_packs([
        ExampleDataSourceActionPack(),
    ])


def get_url(action_name):
    return get_action_url(ExampleDataSourceActionPack, action_name)


# Регистрация источников данных
DSR.add_sources(
    source_creator(
        guid='36346',
        group=u'Список сотрудников',
        url=get_url('action_test_data')),
    source_creator(
        guid='23633',
        group=u'Список сотрудников (новый)',
        url=get_url('action_test_data2')),
    source_creator(
        guid='62626',
        group=u'Работающие сотрудники',
        url=get_url('action_test_data3'))
)


# Регистрация шаблонных переменных
DSR.add_variables(
    variable_creator(
        'Hello',
        u'Привет, Мир!',
        description=u'Тестовое описание переменной'),
    variable_creator(
        'EnterpriseName',
        u'Касатка',
        category=u'ЗиК',
        description=u'Наименование учреждения'),
    variable_creator(
        'OperationDate',
        '01.01.2012',
        category=u'ЗиК',
        v_type=VariableType.DATETIME,
        description=u'Рабочая дата учреждения'),
)
