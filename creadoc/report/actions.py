# coding: utf-8
from m3.actions import ActionPack


class CreadocDataSourceActionPack(ActionPack):
    u"""
    Пак для подвязывания источников данных, пополняется в рантайме
    """
    url = '/data'

    def add_action_in_runtime(self, action, attr_name=None):
        if attr_name is not None:
            setattr(self, attr_name, action)

        self.actions.append(action)
        # Единственный приемлимый способ добавить экшен к рантайме
        self.controller._build_pack_node(action, [self])
