# coding: utf-8
from creadoc.models import CreadocReport

__author__ = 'damirazo <me@damirazo.ru>'


def get_report_by_id(report_id):
    try:
        report = CreadocReport.objects.get(pk=report_id)
    except CreadocReport.DoesNotExist:
        report = None

    return report
