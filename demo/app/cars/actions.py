# coding: utf-8
from recordpack.provider import ObjectListProvider, DjangoModelProvider
from recordpack.recordpack import BaseRecordListPack
from demo.app.cars.models import Car
from demo.app.cars.forms import CarListWindow


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

    allow_add = allow_edit = allow_delete = False

    list_window = CarListWindow
    context_id = 'car_id'

    provider = DjangoModelProvider(
        data_source=Car,
    )

    def get_list_window(self, request, context, is_select):
        win = super(CarActionPack, self).get_list_window(
            request, context, is_select)

        win.bind_reports(self)

        return win


class CarActionPack2(BaseRecordListPack):
    u"""
    Пак для реестра со списком автомобилей
    """
    url = '/car2'

    allow_add = allow_edit = allow_delete = False

    list_window = CarListWindow

    provider = ObjectListProvider(
        data_source=lambda: CAR_DATA,
        object_class=None,
    )

    def get_list_window(self, request, context, is_select):
        win = super(CarActionPack2, self).get_list_window(
            request, context, is_select)

        win.bind_reports(self)

        return win
