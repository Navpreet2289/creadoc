# coding: utf-8
from m3_ext.ui.fields import ExtStringField, ExtFileUploadField, ExtDateField
from m3_ext.ui.misc import ExtDataStore
from m3_ext.ui.misc.store import ExtJsonReader
from m3_ext.ui.panels import ExtObjectGrid
from m3_ext.ui.windows import ExtWindow
from demo.app.forms import BaseEditWindow

__author__ = 'damirazo <me@damirazo.ru>'


class ReportSettingsWindow(ExtWindow):
    u"""
    Окно списка доступных печатных форм
    """

    register_columns = [
        {
            'header': u'Имя реестра',
            'data_index': 'name',
            'sortable': True,
            'width': 100,
        },
        {
            'header': u'Ссылка на реестр',
            'data_index': 'shortname',
            'width': 50,
            'hidden': True,
        }
    ]

    report_columns = [
        {
            'header': u'Название',
            'data_index': 'name',
        },
        {
            'header': u'Действует с',
            'data_index': 'begin',
        },
        {
            'header': u'Действует по',
            'data_index': 'end',
        },
    ]

    def __init__(self):
        super(ReportSettingsWindow, self).__init__()

        self.template_globals = 'ReportSettingsWindow.js'

        self.title = u'Настройка печатных форм'
        self.maximized = True
        self.minimizable = True
        self.layout = 'border'

        self.grid = self.create_grid()
        self.report_grid = self.create_reports_grid()

        self.items.extend([
            self.grid,
            self.report_grid,
        ])

    def create_grid(self):
        grid = ExtObjectGrid(region='west')
        grid.width = 400
        grid.split = True
        grid.allow_paging = False

        for column in self.register_columns:
            grid.add_column(**column)

        return grid

    def create_reports_grid(self):
        grid = ExtObjectGrid(region='center')
        grid.allow_paging = False
        grid.store.auto_load = False

        for column in self.report_columns:
            grid.add_column(**column)

        return grid


class ReportSettingsEditWindow(BaseEditWindow):
    u"""
    Окно редактирования печатной формы
    """

    def __init__(self, create_new, *args, **kwargs):
        super(ReportSettingsEditWindow, self).__init__(*args, **kwargs)

        if create_new:
            self.title = u'Добавление печатной формы'
        else:
            self.title = u'Редактирование печатной формы'

        self.width = 360
        self.height = 200

        self.label_width = 130

        self.field_name = ExtStringField()
        self.field_name.name = 'name'
        self.field_name.label = u'Наименование'
        self.field_name.allow_blank = False
        self.field_name.anchor = '100%'

        self.field_template = ExtFileUploadField()
        self.field_template.possible_file_extensions = ('docx',)
        self.field_template.name = 'template'
        self.field_template.label = u'Шаблон'
        self.field_template.allow_blank = False
        self.field_template.anchor = '100%'

        self.field_begin = ExtDateField()
        self.field_begin.name = 'begin'
        self.field_begin.label = u'Действует с'
        self.field_begin.allow_blank = True
        self.field_begin.format = 'd.m.Y'
        self.field_begin.anchor = '100%'

        self.field_end = ExtDateField()
        self.field_end.name = 'end'
        self.field_end.label = u'Действует по'
        self.field_end.allow_blank = True
        self.field_end.format = 'd.m.Y'
        self.field_end.anchor = '100%'

        self.form.file_upload = True

        self.form.items.extend([
            self.field_name,
            self.field_template,
            self.field_begin,
            self.field_end,
        ])


class ReportSettingsTagsListWindow(BaseEditWindow):

    columns = [
        {
            'name': u'Наименование',
            'data_index': 'name',
        },
        {
            'name': u'Статус',
            'data_index': 'status_verbose',
        },
        {
            'data_index': 'status',
            'hidden': True,
        }
    ]

    def __init__(self):
        super(ReportSettingsTagsListWindow, self).__init__()

        self.title = u'Информация о печатной форме'
        self.maximized = False
        self.minimizable = True
        self.form.layout = 'border'

        self.width = 500
        self.height = 300

        self.grid = self.create_grid()

        self.form.items.append(self.grid)

    def create_grid(self):
        grid = ExtObjectGrid(region='center')
        grid.store = ExtDataStore()
        grid.store.reader = ExtJsonReader()
        grid.width = 400
        grid.allow_paging = False

        for column in self.columns:
            grid.add_column(**column)

        return grid
