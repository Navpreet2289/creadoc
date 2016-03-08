# coding: utf-8
from m3.actions import ActionPack, Action, OperationResult

__author__ = 'damirazo <me@damirazo.ru>'


class ReportListActionPack(ActionPack):
    u"""
    Базовый пак для списка отчетов
    """
    url = '/reports'
    title = title_plural = u'Список отчетов'

    def __init__(self):
        super(ReportListActionPack, self).__init__()

        self.action_rows = ReportListRowsAction()

        self.actions.extend([
            self.action_rows,
        ])

    def get_list_url(self):
        return self.action_rows.get_absolute_url()


class ReportListRowsAction(Action):
    u"""
    Формирование списка отчетов
    """
    url = '/rows'

    def run(self, request, context):
        return OperationResult(message=u'Окно со списком отчетов')
