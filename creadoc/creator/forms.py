# coding: utf-8
from m3_ext.ui.containers import ExtPanel, ExtContainer
from m3_ext.ui.controls import ExtButton
from m3_ext.ui.panels import ExtObjectGrid
from m3_ext.ui.windows import ExtEditWindow, ExtWindow

__author__ = 'damirazo <me@damirazo.ru>'


class DesignerIframeWindow(ExtEditWindow):
    u"""
    Окно с фреймом дизайнера
    """

    def __init__(self, frame_url, report_id):
        super(DesignerIframeWindow, self).__init__()

        self.title = u'Дизайнер отчетов'
        self.maximized = True
        self.modal = True
        self.template_globals = 'scripts/DesignerIframeWindow.js'

        self.report_id = report_id

        panel = ExtPanel()
        panel.html = (
            u'<iframe id="creadoc-iframe" src="{}" width="99%" height="99%">'
            u'Фреймы не поддерживаются'
            u'</iframe>'
        ).format(frame_url)

        self.layout = 'border'
        panel.region = 'center'
        panel.layout = 'fit'
        self.items.append(panel)

        self.bottom_bar = ExtContainer()
        self.bottom_bar.height = 30
        self.bottom_bar.items.append(
            ExtButton(
                text=u'Сохранить шаблон',
                handler='saveReport',
                style={'float': 'right', 'margin': '4px 30px 0 0'},
            )
        )


class DesignerReportsListWindow(ExtWindow):
    u"""
    Окно со списком печатных форм
    """

    columns = (
        {
            'header': 'id',
            'data_index': 'id',
            'hidden': True,
        },
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

        return grid
