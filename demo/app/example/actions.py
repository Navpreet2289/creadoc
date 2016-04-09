# coding: utf-8
from m3.actions import Action
from creadoc.report.decorators import data_source


@data_source('Ololo', 'a068d26b', u'Список сотрудников')
class ReportTestData4Action(Action):

    def context_declaration(self):
        return {
            'params': {'type': 'json', 'required': True, 'default': {}},
        }

    def run(self, request, context):
        result = []

        for x in xrange(1, context.params.get('row_id', 10)):
            result.append({
                'code': str(x).zfill(5),
                'name': u'Строка номер {}'.format(x),
            })

        return result
