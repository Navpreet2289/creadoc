# coding: utf-8
from m3.actions import ControllerCache


def find_pack(pack_cls):
    u"""
    Поиск инстанса пака в кэше
    :param pack_cls:
    :return:
    """
    return ControllerCache.find_pack(pack_cls)
