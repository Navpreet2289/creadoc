# coding: utf-8
from m3_ext.ui.containers import ExtPanel
from m3_ext.ui.panels import ExtObjectGrid
from m3_ext.ui.windows import ExtEditWindow, ExtWindow

__author__ = 'damirazo <me@damirazo.ru>'


class DesignerIframeWindow(ExtEditWindow):
    u"""
    Окно с фреймом дизайнера
    """

    def __init__(self, url):
        super(DesignerIframeWindow, self).__init__()

        self.title = u'Дизайнер отчетов'
        self.maximized = True
        self.modal = True
        self.template_globals = 'scripts/DesignerIframeWindow.js'

        panel = ExtPanel()
        panel.html = (
            u'<iframe id="creadoc-iframe" src="{}" width="99%" height="99%">'
            u'Фреймы не поддерживаются'
            u'</iframe>'
        ).format(url)

        self.layout = 'border'
        panel.region = 'center'
        panel.layout = 'fit'
        self.items.append(panel)


class DesignerReportsListWindow(ExtWindow):
    u"""
    Окно со списком печатных форм
    """

    columns = (
        {
            'header': u'Идентификатор',
            'data_index': 'guid',
            'hidden': True,
        },
        {
            'header': u'Наименование',
            'data_index': 'name',
            'sortable': True,
        },
    )

    def __init__(self):
        super(DesignerReportsListWindow, self).__init__()

        self.title = u'Список печатных форм'
        self.width = 400
        self.height = 300
        self.layout = 'border'
        self.maximizable = True
        self.minimizable = True

        self.grid = self.create_grid()
        grid_panel = ExtPanel()
        grid_panel.region = 'center'
        grid_panel.items.append(self.grid)

        self.items.append(self.grid)

    def create_grid(self):
        grid = ExtObjectGrid()

        for column in self.columns:
            grid.add_column(**column)

        grid.force_fit = True
        grid.layout = 'fit'
        grid.region = 'center'
        grid.allow_paging = False
        grid.row_id_name = 'guid'
        grid.store.id_property = 'guid'

        return grid
