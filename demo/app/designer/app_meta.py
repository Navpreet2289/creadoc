# coding: utf-8
from m3_ext.ui.app_ui import (
    DesktopShortcut, DesktopLoader)
from m3_users import metaroles, GENERIC_USER
from creadoc.creator.actions import CreadocDesignerActionPack
from creadoc.source.helpers import variable_creator
from creadoc.source.registry import DSR
from demo.app.helpers import find_pack

__author__ = 'damirazo <me@damirazo.ru>'


def register_desktop_menu():
    generic_metarole = metaroles.get_metarole(GENERIC_USER)

    designer_root = DesktopShortcut(
        name=CreadocDesignerActionPack.title,
        pack=find_pack(CreadocDesignerActionPack),
        index=10
    )

    DesktopLoader.add(
        metarole=generic_metarole,
        place=DesktopLoader.TOPTOOLBAR,
        element=designer_root,
    )


DSR.register(
    variable_creator(u'Приветствие', u'Привет, Мир!', description=u'Тестовое описание переменной'),
    variable_creator(u'НаименованиеУчреждения', u'Касатка', category=u'ЗиК'),
    variable_creator(u'РабочаяДата', u'01.01.2012', category=u'ЗиК'),
)
