# coding: utf-8
from django.db.models import Q
from creadoc.models import CreadocReport


def all_reports(on_date=None):
    u"""
    Список всех доступных отчетов
    :param on_date: Дата, на которую ищутся актуальные отчеты
    :return:
    """
    q = Q(state=True)

    if on_date is not None:
        q &= Q(created_at=on_date)

    return CreadocReport.objects.filter(q)


def show_viewer_handler():
    pass


def print_report_handler():
    pass
