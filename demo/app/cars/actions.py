# coding: utf-8
from recordpack.provider import ObjectListProvider
from recordpack.recordpack import BaseRecordListPack
from demo.app.cars.ui import CarListWindow


CAR_DATA = [
    {
        'marka': 'ВАЗ',
        'seria': '2109',
        'year': '2003',
    },
    {
        'marka': 'Ford',
        'seria': 'Focus II',
        'year': '2010',
    },
    {
        'marka': 'Subaru',
        'seria': 'Impreza',
        'year': '2008',
    },
]


class CarActionPack(BaseRecordListPack):
    u"""
    Пак для реестра со списком автомобилей
    """
    url = '/car'

    list_window = CarListWindow

    provider = ObjectListProvider(
        data_source=lambda: CAR_DATA,
        object_class=None,
    )


class CarActionPack2(BaseRecordListPack):
    u"""
    Пак для реестра со списком автомобилей
    """
    url = '/car2'

    list_window = CarListWindow

    provider = ObjectListProvider(
        data_source=lambda: CAR_DATA,
        object_class=None,
    )