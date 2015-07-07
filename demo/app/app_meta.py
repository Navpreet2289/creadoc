# coding: utf-8
from django.conf.urls import patterns
from demo.app import controller

__author__ = 'damirazo <me@damirazo.ru>'


def register_urlpatterns():
    return patterns(
        '',
        ('^', controller.action_controller.process_request),
    )
