# coding: utf-8
from django.conf import settings
from m3.actions import ActionController

__author__ = 'damirazo <me@damirazo.ru>'


creadoc_controller = ActionController(
    url='/' + settings.CREADOC_URL,
)
