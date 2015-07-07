# coding: utf-8
from m3_ext.ui.containers import ExtForm, ExtToolBar
from m3_ext.ui.controls import ExtButton
from m3_ext.ui.windows import ExtEditWindow

__author__ = 'damirazo <me@damirazo.ru>'


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
