# coding: utf-8
from django.conf.urls import patterns
from creadoc import controller
from creadoc.actions import CreaDocActionPack

__author__ = 'damirazo <me@damirazo.ru>'


def register_actions():
    controller.action_controller.extend_packs([
        CreaDocActionPack(),
    ])


def register_urlpatterns():
    return patterns(
        '',
        ('^creadoc', controller.action_controller.process_request),
    )
