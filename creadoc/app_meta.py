# coding: utf-8
from django.conf.urls import patterns
from creadoc import controller
from creadoc.designer.actions import CreadocDesignerActionPack

__author__ = 'damirazo <me@damirazo.ru>'


def register_actions():
    controller.action_controller.extend_packs([
        CreadocDesignerActionPack(),
    ])


def register_urlpatterns():
    return patterns(
        '',
        ('^creadoc', controller.action_controller.process_request),
    )
