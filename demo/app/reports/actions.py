# coding: utf-8
from m3.actions import ActionPack, Action, OperationResult
from m3.actions.results import PreJsonResult
from m3_ext.ui.results import ExtUIScriptResult
from demo.app.reports.forms import RegistryListWindow

__author__ = 'damirazo <me@damirazo.ru>'


class ReportListActionPack(ActionPack):
    u"""
    Базовый пак для списка отчетов
    """
    url = '/reports'
    title = title_plural = u'Список отчетов'

    def __init__(self):
        super(ReportListActionPack, self).__init__()

        self.action_list = ReportListWindowAction()
        self.action_rows = ReportListRowsAction()

        self.actions.extend([
            self.action_list,
            self.action_rows,
        ])

    def get_list_url(self):
        return self.action_list.get_absolute_url()


class ReportListWindowAction(Action):
    url = '/list'

    def run(self, request, context):
        win = RegistryListWindow()
        win.grid.action_data = self.parent.action_rows

        return ExtUIScriptResult(win, context)


class ReportListRowsAction(Action):
    u"""
    Формирование списка отчетов
    """
    url = '/rows'

    def run(self, request, context):
        result = []

        for x in xrange(1, 101):
            result.append({
                'code': x,
                'name': u'Запись #{}'.format(x),
            })

        return PreJsonResult({'rows': result, 'count': len(result)})
