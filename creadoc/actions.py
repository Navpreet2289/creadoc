# coding: utf-8
from m3.actions import ActionPack, ACD
from recordpack.helpers import make_action

__author__ = 'damirazo <me@damirazo.ru>'


class CreaDocActionPack(ActionPack):
    u"""
    Формирование печатной формы
    """
    url = '/creadoc'

    def __init__(self):
        super(CreaDocActionPack, self).__init__()

        self.action_build = make_action(
            url='/build',
            run_method=self.request_build,
            acd=self._action_context_build,
        )

    def _action_context_build(self):
        return [
            ACD(name='shortname', type=unicode, required=True),
        ]

    def request_build(self, request, context):
        pass
