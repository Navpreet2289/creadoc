# coding: utf-8
import os
import uuid
from django.db import transaction
from django.conf import settings
from django.http import HttpResponse
from django.template import loader, Context
from m3.actions import ActionPack, Action, PreJsonResult, OperationResult, \
    ApplicationLogicException
from m3_ext.ui.results import ExtUIScriptResult
from creadoc.creator.forms import (
    DesignerIframeWindow, DesignerReportsListWindow)
from creadoc.creator.helpers import redirect_to_action
from creadoc.models import CreadocReport
from creadoc.source.registry import DSR

__author__ = 'damirazo <me@damirazo.ru>'


class CreadocDesignerActionPack(ActionPack):
    u"""
    Базовый пак дизайнера отчетов
    """
    url = '/designer'
    title = title_plural = u'Дизайнер отчетов'

    def __init__(self):
        super(CreadocDesignerActionPack, self).__init__()

        self.action_show = CreadocDesignerShowAction()
        self.action_iframe = CreadocDesignerIframeAction()
        self.action_report_list_window = CreadocDesignerReportListAction()
        self.action_report_rows = CreadocDesignerReportRowsAction()
        self.action_report_new = CreadocDesignerReportNewAction()
        self.action_report_edit = CreadocDesignerReportEditAction()
        self.action_report_save = CreadocDesignerReportSaveAction()
        self.action_report_delete = CreadocDesignerReportDeleteAction()

        self.actions.extend([
            self.action_show,
            self.action_iframe,
            self.action_report_list_window,
            self.action_report_rows,
            self.action_report_new,
            self.action_report_edit,
            self.action_report_save,
            self.action_report_delete,
        ])

    def get_list_url(self):
        return self.action_report_list_window.get_absolute_url()


class CreadocDesignerShowAction(Action):
    u"""
    Формирование окна, содержащего фрейм с дизайнером
    """
    url = '/show'

    def context_declaration(self):
        return {
            'report_id': {'type': 'int', 'required': True, 'default': 0},
        }

    def run(self, request, context):
        url = u'{}?report_id={}'.format(
            self.parent.action_iframe.get_absolute_url(),
            context.report_id
        )
        win = DesignerIframeWindow(url=url)

        return ExtUIScriptResult(win, context)


class CreadocDesignerIframeAction(Action):
    u"""
    Формирование фрейма, содержащего страницу с дизайнером
    Заполнение дизайнера зарегистрированными источниками данных
    """
    url = '/iframe'

    def context_declaration(self):
        return {
            'report_id': {'type': 'int', 'required': True, 'default': None},
        }

    def run(self, request, context):
        # Если передано наименование шаблона,
        # то это редактирование и мы грузим готовый шаблон.
        # В противном случае загружаем пустой шаблон.
        if not context.report_id:
            template_url = '{}reports/EmptyReport.mrt'.format(
                settings.STATIC_URL)
        else:
            try:
                report = CreadocReport.objects.get(pk=context.report_id)
            except CreadocReport.DoesNotExist:
                raise ApplicationLogicException((
                    u'Шаблон отчетной формы с id={} отсутствует, '
                    u'возможно он был удален.'
                ).format(context.report_id))

            template_url = '{}{}/{}.mrt'.format(
                settings.MEDIA_URL,
                settings.CREADOC_REPORTS_DIR,
                report.guid)

        t = loader.get_template('creadoc_designer.html')

        ctx = Context()
        ctx['reports_url'] = settings.CREADOC_REPORTS_URL
        ctx['report_save_url'] = (
            self.parent.action_report_save.get_absolute_url())
        ctx['template_url'] = template_url
        ctx['variables'] = DSR.variables()
        ctx['sources'] = DSR.sources()

        return HttpResponse(t.render(ctx))


class CreadocDesignerReportListAction(Action):
    u"""
    Формирование окна со списком доступных печатных форм
    """
    url = '/list-window'

    def run(self, request, context):
        win = DesignerReportsListWindow()
        win.grid.action_data = self.parent.action_report_rows
        win.grid.action_new = self.parent.action_report_new
        win.grid.action_edit = self.parent.action_report_edit
        win.grid.action_delete = self.parent.action_report_delete

        return ExtUIScriptResult(win, context)


class CreadocDesignerReportRowsAction(Action):
    u"""
    Список существующий отчетных форм
    """
    url = '/rows'

    def run(self, request, context):
        rows = CreadocReport.objects.all()

        return PreJsonResult({'rows': list(rows), 'count': rows.count()})


class CreadocDesignerReportNewAction(Action):
    u"""
    Создание новой отчетной формы
    """
    url = '/new'

    def run(self, request, context):
        return redirect_to_action(request, self.parent.action_show)


class CreadocDesignerReportEditAction(Action):
    u"""
    Редактирование существующей отчетной формы
    """
    url = '/edit'

    def context_declaration(self):
        return {
            'row_id': {'type': 'int', 'required': True},
        }

    def run(self, request, context):
        return redirect_to_action(
            request,
            self.parent.action_show,
            {'report_id': context.row_id},
        )


class CreadocDesignerReportSaveAction(Action):
    u"""
    Сохранение отчетной формы
    """
    url = '/save'

    def context_declaration(self):
        return {
            'report': {
                'type': 'unicode',
                'required': True,
            }
        }

    @transaction.atomic
    def run(self, request, context):
        report_data = context.report
        report_guid = str(uuid.uuid4())

        report = CreadocReport()
        report.name = report_guid
        report.guid = report_guid
        report.save()

        with open(os.path.join(settings.CREADOC_REPORTS_ROOT, report_guid + '.mrt'), 'w+') as f:  # noqa
            f.write(report_data.encode('utf-8'))

        return OperationResult()


class CreadocDesignerReportDeleteAction(Action):
    u"""
    Удаление отчетной формы
    """
    url = '/delete'

    def run(self, request, context):
        pass
