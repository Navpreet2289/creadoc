# coding: utf-8
import random
import string

from m3.actions import ActionPack, Action, OperationResult, PreJsonResult

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
        self.action_test_data = ReportTestDataAction()

        self.actions.extend([
            self.action_rows,
            self.action_test_data,
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


class ReportTestDataAction(Action):
    url = '/data.json'

    def run(self, request, context):
        result = []

        for x in xrange(1, 5001):
            result.append({
                'name': u''.join(map(
                    lambda x: random.choice(string.ascii_lowercase),
                    xrange(random.randint(3, 10)),
                )),
                'value': random.randint(0, 1000),
            })

        return PreJsonResult({
            u'Полный список сотрудников': result,
        })
