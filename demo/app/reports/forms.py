# coding: utf-8
from m3_ext.ui.containers import ExtToolbarMenu
from m3_ext.ui.containers.context_menu import ExtContextMenu, ExtContextMenuItem
from m3_ext.ui.panels import ExtObjectGrid
from m3_ext.ui.windows import ExtWindow

from creadoc.api import all_reports


class RegistryListWindow(ExtWindow):

    columns = (
        {
            'header': 'id',
            'data_index': 'id',
            'hidden': True,
        },
        {
            'header': u'Наименование',
            'data_index': 'name',
            'sortable': True,
        },
        {
            'header': u'Код',
            'data_index': 'code',
            'sortable': True,
        }
    )

    def __init__(self):
        super(RegistryListWindow, self).__init__()

        self.title = u'Список тестовых записей'
        self.width = 800
        self.height = 500
        self.layout = 'border'
        self.maximizable = True
        self.minimizable = True

        self.grid = self.create_grid()

        menu = ExtContextMenu()

        reports = all_reports()

        for report in reports:
            pass

        menu.items.append(
            ExtContextMenuItem(
                text=u'Тестовый отчет',
                icon_cls='doc-print',
                handler='Ext.emptyFn',
            )
        )

        button_report = ExtToolbarMenu(
            icon_cls='icon-printer',
            menu=menu,
            tooltip_text=u'Печать',
        )

        self.grid.top_bar.items.append(button_report)

        self.items.append(self.grid)

    def create_grid(self):
        grid = ExtObjectGrid()

        for column in self.columns:
            grid.add_column(**column)

        grid.force_fit = True
        grid.layout = 'fit'
        grid.region = 'center'
        grid.allow_paging = False

        return grid