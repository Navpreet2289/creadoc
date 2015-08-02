# coding: utf-8
from m3.actions import ControllerCache
from m3_ext.ui.app_ui import (
    DesktopShortcut, DesktopLaunchGroup,
    DesktopLoader)
from m3_users import metaroles, GENERIC_USER
from demo.app import controller
from demo.app.report_settings.actions import (
    ReportSettingsPack, ReportSettingsRegisterPack)

__author__ = 'damirazo <me@damirazo.ru>'


def register_actions():
    controller.action_controller.extend_packs([
        ReportSettingsPack(),
        ReportSettingsRegisterPack(),
    ])


def register_desktop_menu():
    generic_metarole = metaroles.get_metarole(GENERIC_USER)

    administrations = DesktopLaunchGroup(name=u'Администрирование', index=20)

    administrations.subitems.extend([
        DesktopShortcut(
            name=u'Настройки печатных форм',
            pack=ControllerCache.find_pack(ReportSettingsPack),
            index=10
        ),
    ])

    DesktopLoader.add(
        metarole=generic_metarole,
        place=DesktopLoader.TOPTOOLBAR,
        element=administrations,
    )
