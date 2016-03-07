# coding: utf-8
from m3_ext.ui.app_ui import (
    DesktopShortcut, DesktopLaunchGroup,
    DesktopLoader)
from m3_users import metaroles, GENERIC_USER

from creadoc.creator.actions import CreadocDesignerActionPack
from demo.app.helpers import find_pack
from demo.app import controller

__author__ = 'damirazo <me@damirazo.ru>'


def register_actions():
    controller.action_controller.extend_packs([

    ])


def register_desktop_menu():
    generic_metarole = metaroles.get_metarole(GENERIC_USER)

    functions_root = DesktopLaunchGroup(name=u'Функции', index=20)

    functions_root.subitems.extend([
        DesktopShortcut(
            name=CreadocDesignerActionPack.title,
            pack=find_pack(CreadocDesignerActionPack),
            index=10
        ),
    ])

    DesktopLoader.add(
        metarole=generic_metarole,
        place=DesktopLoader.TOPTOOLBAR,
        element=functions_root,
    )
