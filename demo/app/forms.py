# coding: utf-8
from m3_ext.ui.containers import (
    ExtForm, ExtToolBar)
from m3_ext.ui.controls import ExtButton
from m3_ext.ui.panels import ExtObjectGrid
from m3_ext.ui.windows import ExtEditWindow, ExtWindow

from creadoc.helper.form import bind_reports_to_grid

__author__ = 'damirazo <me@damirazo.ru>'


class BaseListWindow(ExtWindow):
    u"""
    Базовое окно списка записей
    """

    columns = []

    def __init__(self):
        super(BaseListWindow, self).__init__()

        self.grid = self.create_base_grid()
        self.items.append(self.grid)

    def create_base_grid(self):
        grid = ExtObjectGrid(region='center')
        grid.width = 400
        grid.allow_paging = False

        for column in self.columns:
            grid.add_column(**column)

        return grid

    def bind_reports(self, pack):
        bind_reports_to_grid(self.grid, pack)


class BaseEditWindow(ExtEditWindow):
    u"""
    Базовое окно формы редактирования
    """

    def __init__(self, *args, **kwargs):
        super(BaseEditWindow, self).__init__(*args, **kwargs)

        self.template_globals = 'scripts/BaseEditWindow.js'

        self.form = ExtForm()

        self.footer_bar = ExtToolBar()
        self.footer_bar.add_fill()
        self.button_align = self.align_left

        self.button_submit = ExtButton()
        self.button_submit.text = u'Сохранить'
        self.button_submit.handler = 'submitForm'

        self.footer_bar.items.append(self.button_submit)
