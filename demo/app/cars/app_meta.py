# coding: utf-8
from m3.actions import ControllerCache
from m3_ext.ui.app_ui import (
    DesktopLaunchGroup, DesktopShortcut,
    GENERIC_USER, DesktopLoader)
from creadoc.registry.registry import PackRegistry, SourceRegistry
from demo.app import controller
from demo.app.cars.actions import CarActionPack, CarActionPack2
from demo.app.cars.sources import CarSource


def register_actions():
    controller.action_controller.extend_packs([
        CarActionPack(),
        CarActionPack2(),
    ])


def register_desktop_menu():
    metarole = GENERIC_USER
    registers = DesktopLaunchGroup(name=u'Список реестров', index=10)

    registers.subitems.extend([
        DesktopShortcut(
            name=u'Список автомобилей',
            pack=ControllerCache.find_pack(CarActionPack),
            index=10
        ),
    ])

    DesktopLoader.add(
        metarole=metarole,
        place=DesktopLoader.TOPTOOLBAR,
        element=registers,
    )


PackRegistry.add(
    (CarActionPack, u'Реестр автомобилей'),
    (CarActionPack2, u'Второй реестр автомобилей'),
)

SourceRegistry.register(CarSource)
