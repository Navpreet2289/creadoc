# coding: utf-8
from m3_ext.ui.app_ui import (
    DesktopShortcut, DesktopLoader)
from m3_users import metaroles, GENERIC_USER
from creadoc.source.helpers import source_creator
from creadoc.source.registry import DSR
from demo.app.helpers import find_pack, get_action_url
from demo.app import controller
from demo.app.reports.actions import (
    ReportListActionPack, ExampleDataSourceActionPack)

__author__ = 'damirazo <me@damirazo.ru>'


def register_actions():
    controller.action_controller.extend_packs([
        ReportListActionPack(),
        ExampleDataSourceActionPack(),
    ])


def register_desktop_menu():
    generic_metarole = metaroles.get_metarole(GENERIC_USER)

    reports_root = DesktopShortcut(
        name=ReportListActionPack.title,
        pack=find_pack(ReportListActionPack),
        index=20
    )

    DesktopLoader.add(
        metarole=generic_metarole,
        place=DesktopLoader.TOPTOOLBAR,
        element=reports_root,
    )


DSR.add_sources(
    source_creator(
        guid='36346',
        group=u'Список сотрудников',
        url=get_action_url(ExampleDataSourceActionPack, 'action_test_data'),
    ),
    source_creator(
        guid='23633',
        group=u'Список сотрудников (новый)',
        url=get_action_url(ExampleDataSourceActionPack, 'action_test_data2'),
    ),
    source_creator(
        guid='62626',
        group=u'Работающие сотрудники',
        url=get_action_url(ExampleDataSourceActionPack, 'action_test_data3'),
    )
)
