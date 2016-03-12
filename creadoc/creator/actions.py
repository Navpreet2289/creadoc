# coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from m3.actions import ActionPack, Action, PreJsonResult
from m3_ext.ui.results import ExtUIScriptResult
from creadoc.creator.forms import (
    DesignerIframeWindow, DesignerReportsListWindow)
from creadoc.creator.helpers import redirect_to_action
from creadoc.source.registry import DSR

__author__ = 'damirazo <me@damirazo.ru>'


class CreadocDesignerActionPack(ActionPack):
    u"""
    Базовый пак дизайнера отчетов
    """
    url = '/designer'
    title = title_plural = u'Дизайнер отчетов'

    def __init__(self):
        super(CreadocDesignerActionPack, self).__init__()

        self.action_show = CreadocDesignerShowAction()
        self.action_iframe = CreadocDesignerIframeAction()
        self.action_report_list_window = CreadocDesignerReportListAction()
        self.action_report_rows = CreadocDesignerReportRowsAction()
        self.action_report_new = CreadocDesignerReportNewAction()
        self.action_report_edit = CreadocDesignerReportEditAction()

        self.actions.extend([
            self.action_show,
            self.action_iframe,
            self.action_report_list_window,
            self.action_report_rows,
            self.action_report_new,
            self.action_report_edit,
        ])

    def get_list_url(self):
        return self.action_report_list_window.get_absolute_url()


class CreadocDesignerShowAction(Action):
    u"""
    Формирование окна, содержащего фрейм с дизайнером
    """
    url = '/show'

    def context_declaration(self):
        return {
            'template': {'type': 'str', 'required': True, 'default': None},
        }

    def run(self, request, context):
        url = u'{}?template={}'.format(
            self.parent.action_iframe.get_absolute_url(),
            context.template or 'EmptyReport'
        )
        win = DesignerIframeWindow(url=url)

        return ExtUIScriptResult(win, context)


class CreadocDesignerIframeAction(Action):
    u"""
    Формирование фрейма, содержащего страницу с дизайнером
    Заполнение дизайнера зарегистрированными источниками данных
    """
    url = '/iframe'

    def context_declaration(self):
        return {
            'template': {'type': 'str', 'required': True, 'default': None},
        }

    def run(self, request, context):
        # Если передано наименование шаблона,
        # то это редактирование и мы грузим готовый шаблон.
        # В противном случае загружаем пустой шаблон.
        if context.template is None:
            template_name = 'EmptyReport'
        else:
            template_name = context.template

        t = loader.get_template('creadoc_designer.html')

        ctx = Context()
        ctx['template_name'] = template_name
        ctx['variables'] = DSR.variables()
        ctx['sources'] = DSR.sources()

        return HttpResponse(t.render(ctx))


class CreadocDesignerReportListAction(Action):
    u"""
    Формирование окна со списком доступных печатных форм
    """
    url = '/list-window'

    def run(self, request, context):
        win = DesignerReportsListWindow()
        win.grid.action_data = self.parent.action_report_rows
        win.grid.action_new = self.parent.action_report_new
        win.grid.action_edit = self.parent.action_report_edit

        return ExtUIScriptResult(win, context)


class CreadocDesignerReportRowsAction(Action):
    url = '/rows'

    def run(self, request, context):
        # FIXME: Тестовые данные
        rows = [
            {'name': u'Простой список', 'guid': 'SimpleList'},
            {'name': u'График продаж', 'guid': 'OnlineStoreSales'},
        ]

        return PreJsonResult({'rows': rows, 'count': len(rows)})


class CreadocDesignerReportNewAction(Action):
    url = '/new'

    def run(self, request, context):
        return redirect_to_action(request, self.parent.action_show)


class CreadocDesignerReportEditAction(Action):
    url = '/edit'

    def context_declaration(self):
        return {
            'guid': {'type': 'str', 'required': True},
        }

    def run(self, request, context):
        return redirect_to_action(
            request, self.parent.action_show,
            {'template': context.guid}
        )
