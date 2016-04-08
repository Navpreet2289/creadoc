# coding: utf-8
import random
import string
from decimal import Decimal
from m3.actions import ActionPack, Action
from m3.actions.results import PreJsonResult
from creadoc.source.variable import VariableType


DEFAULT_FIELDS = (
    ('fullname', VariableType.STRING),
    ('salary', VariableType.DECIMAL),
)


class ExampleDataSourceActionPack(ActionPack):
    u"""
    Пак с демонстрационными источниками данных
    """
    url = '/data-sources'

    def __init__(self):
        super(ExampleDataSourceActionPack, self).__init__()

        self.action_test_data = ReportTestDataAction()
        self.action_test_data2 = ReportTestData2Action()
        self.action_test_data3 = ReportTestData3Action()

        self.actions.extend([
            self.action_test_data,
            self.action_test_data2,
            self.action_test_data3,
        ])


def generate_data(name, count, fields=None):
    if fields is None:
        fields = DEFAULT_FIELDS

    conformity = {
        VariableType.STRING: lambda: (
            ''.join(map(
                lambda x: random.choice(string.ascii_lowercase),
                xrange(random.randint(3, 10))
            ))
        ),
        VariableType.DECIMAL: lambda: Decimal(random.randint(0, 1000)),
    }

    def outer(cls):
        def run(self, *args, **kwargs):
            result = []

            for x in xrange(1, count + 1):
                result.append(
                    dict(map(
                        lambda x: (x[0], conformity.get(x[1])()),
                        fields
                    ))
                )

            return PreJsonResult({name: result})

        cls.run = run

        return cls

    return outer


@generate_data('Employee1', 24)
class ReportTestDataAction(Action):
    url = '/employee-middle'


@generate_data('Employee2', 2)
class ReportTestData2Action(Action):
    url = '/employee-small'


@generate_data('Employee3', 200)
class ReportTestData3Action(Action):
    url = '/employee-large'
