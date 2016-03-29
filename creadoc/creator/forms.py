# coding: utf-8
from m3_ext.ui.containers import ExtPanel, ExtContainer, ExtForm
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
        self.closable = False
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

        # Кнопка закратия окна с подтверждением потери изменений
        self.btn_close = ExtButton()
        self.btn_close.handler = 'closeWindow'
        self.btn_close.style = {'float': 'right', 'margin': '4px 10px 0 0'}
        self.btn_close.text = u'Закрыть окно'

        # Кнопка сохранения текущего состояния шаблона без закрытия окна
        self.btn_save = ExtButton()
        self.btn_save.handler = 'saveTemplate'
        self.btn_save.style = {'float': 'right', 'margin': '4px 10px 0 0'}
        self.btn_save.text = u'Сохранить'

        # Кнопка сохранения шаблона с изменением его имени
        self.btn_save_as = ExtButton()
        self.btn_save_as.handler = 'saveTemplateAs'
        self.btn_save_as.style = {'float': 'right', 'margin': '4px 10px 0 0'}
        self.btn_save_as.text = u'Сохранить как...'

        self.btn_data_sources = ExtButton()
        self.btn_data_sources.handler = 'openDataSourceWindow'
        self.btn_data_sources.style = {
            'float': 'left',
            'margin': '4px 0 0 10px',
        }
        self.btn_data_sources.text = u'Источники данных'

        # Кнопка загрузки пользовательского шаблона
        self.btn_import = ExtButton()
        self.btn_import.handler = 'Ext.emptyFn'
        self.btn_import.style = {'float': 'left', 'margin': '4px 0 0 10px'}
        self.btn_import.disabled = True
        self.btn_import.text = u'Импорт шаблона'

        # Кнопка выгрузки шаблона
        self.btn_export = ExtButton()
        self.btn_export.handler = 'Ext.emptyFn'
        self.btn_export.style = {'float': 'left', 'margin': '4px 0 0 10px'}
        self.btn_export.disabled = True
        self.btn_export.text = u'Экспорт шаблона'

        self.bottom_bar = ExtContainer()
        self.bottom_bar.height = 30
        self.bottom_bar.items.extend([
            self.btn_import,
            self.btn_export,
            self.btn_data_sources,
            self.btn_close,
            self.btn_save,
            self.btn_save_as,
        ])


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
        {
            'header': u'Дата создания',
            'data_index': 'created_at',
            'sortable': True,
        }
    )

    def __init__(self):
        super(DesignerReportsListWindow, self).__init__()

        self.title = u'Список печатных форм'
        self.width = 400
        self.height = 300
        self.layout = 'border'
        self.maximizable = True
        self.minimizable = True
        self.template_globals = 'scripts/DesignerReportsListWindow.js'

        self.grid = self.create_grid()

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


class DesignerDataSourcesWindow(ExtEditWindow):

    columns = (
        {
            'header': u'Идентификатор',
            'data_index': 'id',
            'hidden': True,
        },
        {
            'header': u'Наименование',
            'data_index': 'name',
            'sortable': True,
        },
        {
            'header': u'Путь',
            'data_index': 'url',
            'sortable': True,
            'hidden': True,
        }
    )

    def __init__(self):
        super(DesignerDataSourcesWindow, self).__init__()

        self.title = u'Список источников данных'
        self.width = 800
        self.height = 500
        self.modal = True
        self.layout = 'border'

        self.form = form = ExtForm()
        form.layout = 'fit'
        form.region = 'center'

        self.grid = grid = ExtObjectGrid()
        grid.force_fit = True
        grid.layout = 'fit'
        grid.allow_paging = False

        for column in self.columns:
            grid.add_column(**column)

        self.form.items.append(grid)
