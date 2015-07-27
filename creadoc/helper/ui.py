# coding: utf-8
import datetime
from django.template import Context
from django.template.loader import get_template
from m3.actions.urls import get_pack_instance
from m3_ext.ui.containers import (
    ExtContextMenu, ExtContextMenuItem,
    ExtToolbarMenu)
from creadoc.models import CreadocReport

__author__ = 'damirazo <me@damirazo.ru>'


# Имя шаблона для обработчика кнопки печати
BUILDER_TEMPLATE_NAME = 'ReportBuilder.js'


def create_reports_button(pack, date=None):
    u"""
    Формирование контекстного меню
    со списком доступных для указанного пака печатных форм.

    :param ActionPack pack: Инстанс пака, для которого осуществляется поиск ПФ
    :param date or None date: Дата, для которой производится поиск
        актуальных ПФ (по умолчанию текущая дата)
    :rtype: ExtToolbarMenu
    """
    if date is None:
        date = datetime.date.today()

    reports = CreadocReport.objects.filter(
        shortname=pack.get_short_name(),
        begin__lte=date,
        end__gte=date,
    ).order_by('name')

    report_menu = ExtContextMenu()
    report_menu.icon_cls = 'icon-print'

    for report in reports:
        report_element = ExtContextMenuItem()
        report_element.text = report.name
        report_element.handler = build_handler(report)

        report_menu.items.append(report_element)

    report_button = ExtToolbarMenu(
        icon_cls='icon-printer',
        tooltip_text=u'Печать',
        menu=report_menu,
    )

    return report_button


def bind_reports_to_grid(grid, pack, date=None):
    u"""
    Добавление в указанный грид выпадающего списка
    доступных для указанного пака печатных форм.

    :param grid: Грид, к которому будет осуществляться
        привязка выпадающего списка
    :param pack: Инстанс пака, для которого осуществляется поиск ПФ
    :param date: Дата, для которой осуществляется поиск актуальных ПФ
    """
    if date is None:
        date = datetime.date.today()

    button = create_reports_button(pack, date)

    top_bar = grid.top_bar
    top_bar.add_separator()
    top_bar.items.append(button)


def build_handler(report):
    u"""
    Формирование обработчика клика по кнопке печати
    """
    context = Context({
        'url': get_pack_instance(
            'CreaDocActionPack'
        ).action_build.get_absolute_url(),
        'report_id': report.id,
    })
    template = get_template(BUILDER_TEMPLATE_NAME)

    return template.render(context)
