# coding: utf-8
from creadoc import controller
from creadoc.actions import CreaDocActionPack

__author__ = 'damirazo <me@damirazo.ru>'


def register_actions():
    controller.action_controller.extend_packs([
        CreaDocActionPack(),
    ])
