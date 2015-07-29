# coding: utf-8
from m3.actions import ActionPack, ACD, OperationResult
from recordpack.helpers import make_action
from creadoc.api import get_report_by_id
from creadoc.document.builder import CreaDocBuilder
from creadoc.document.filler import CreaDocFiller

__author__ = 'damirazo <me@damirazo.ru>'


class CreaDocActionPack(ActionPack):
    u"""
    Формирование печатной формы
    """
    url = '/report'

    def __init__(self):
        super(CreaDocActionPack, self).__init__()

        self.action_build = make_action(
            url='/build',
            run_method=self.request_build,
            acd=self._action_context_build,
        )

        self.actions.extend([
            self.action_build,
        ])

    def _action_context_build(self):
        return [
            ACD(name='report_id', type=int, required=True,
                verbose_name=u'Идентификатор ПФ'),
        ]

    def request_build(self, request, context):
        report = get_report_by_id(context.report_id)

        builder = CreaDocBuilder(report)
        filler = CreaDocFiller(context)
        document = builder.build(filler)
        result = document.save()

        return OperationResult(result)
