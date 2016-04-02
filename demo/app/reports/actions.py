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
        # TODO: Тестовые данные
        self.action_test_data = ReportTestDataAction()
        self.action_test_data2 = ReportTestData2Action()
        self.action_test_data3 = ReportTestData3Action()

        self.actions.extend([
            self.action_rows,
            self.action_test_data,
            self.action_test_data2,
            self.action_test_data3,
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
    url = '/data1'

    def run(self, request, context):
        result = []

        for x in xrange(1, 5001):
            result.append({
                u'ФИО': u''.join(map(
                    lambda x: random.choice(string.ascii_lowercase),
                    xrange(random.randint(3, 10)),
                )),
                u'Зарплата': random.randint(0, 1000),
            })

        return PreJsonResult({
            u'Сотрудник2': result,
        })


class ReportTestData2Action(Action):
    url = '/data2'

    def run(self, request, context):
        result = []

        for x in xrange(1, 5001):
            result.append({
                u'ФИО': u''.join(map(
                    lambda x: random.choice(string.ascii_lowercase),
                    xrange(random.randint(3, 10)),
                )),
                u'Зарплата': random.randint(0, 1000),
            })

        return PreJsonResult({
            u'Сотрудник': result,
        })


class ReportTestData3Action(Action):
    url = '/data3'

    def run(self, request, context):
        result = []

        for x in xrange(1, 5001):
            result.append({
                u'ФИО': u''.join(map(
                    lambda x: random.choice(string.ascii_lowercase),
                    xrange(random.randint(3, 10)),
                )),
                u'Зарплата': random.randint(0, 1000),
            })

        return PreJsonResult({
            u'Сотрудник3': result,
        })
