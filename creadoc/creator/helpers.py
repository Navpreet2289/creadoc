# coding: utf-8
from copy import copy
from m3.actions import urls

__author__ = 'damirazo <me@damirazo.ru>'


def redirect_to_action(request, action, params=None):
    controller = action.controller
    request.path = urls.get_url(action)
    new_post = copy(request.POST)

    if params:
        new_post.update(params)

    request.POST = new_post
    # важно! т.к. там еще старые значения
    del request._request

    return controller.process_request(request)
