# coding: utf-8
import datetime
from operator import itemgetter
from m3.actions import ACD, OperationResult
from recordpack.be import BE
from recordpack.provider import ObjectListProvider, DjangoModelProvider
from recordpack.recordpack import BaseRecordListPack
from creadoc.document.preprocessor import DocumentPreprocessor
from creadoc.models import CreadocReport
from creadoc.registry.pack import PackRegistry
from demo.app.report_settings.forms import (
    ReportSettingsWindow, ReportSettingsEditWindow)

__author__ = 'damirazo <me@damirazo.ru>'


class ReportSettingsPack(BaseRecordListPack):
    url = '/report_registers'

    list_window = ReportSettingsWindow

    provider = ObjectListProvider(
        data_source=None,
        object_class=None)

    allow_add = False
    allow_delete = False
    allow_edit = False

    def __init__(self):
        super(ReportSettingsPack, self).__init__()

        self.report_pack = ReportSettingsRegisterPack()

        self.subpacks.append(self.report_pack)

    def get_rows(self, request, context, query_object):
        result = []

        for shortname, registry_item in PackRegistry.instance().items():
            result.append({
                'shortname': registry_item.shortname,
                'name': registry_item.name,
            })

        return {
            'rows': result,
        }

    def get_list_window(self, request, context, is_select):
        win = super(ReportSettingsPack, self).get_list_window(
            request, context, is_select)

        self.report_pack.bind_to_grid(request, context, win.report_grid)

        return win


class ReportSettingsRegisterPack(BaseRecordListPack):
    url = '/reports'

    provider = DjangoModelProvider(data_source=CreadocReport)

    edit_window = new_window = ReportSettingsEditWindow

    master_id = 'shortname'
    master_is_foreignkey = False
    context_master_id = 'shortname'
    context_master_type = str

    def _get_save_action_context_declaration(self):
        return [
            ACD(name='id', type=int, required=True),
            ACD(name='name', type=unicode, required=True),
            ACD(name='shortname', type=unicode, required=True),
            ACD(name='begin', type=datetime.date, required=False),
            ACD(name='end', type=datetime.date, required=False),
        ]

    def request_save(self, request, context):
        preprocessor = DocumentPreprocessor(request.FILES.get('file_template'))
        finded_tags = preprocessor.prepare()

        has_errors = any(map(itemgetter(1), finded_tags.iteritems()))

        if not has_errors:
            return super(ReportSettingsRegisterPack, self).request_save(
                request, context)
        else:
            error_tags = filter(
                None,
                map(lambda x: not x[1] and x[0] or None, finded_tags.iteritems())
            )

            return OperationResult.by_message(
                u'Шаблон содержит несуществующие теги: <br>{}'.format(
                    u'<br>'.join(error_tags),
                )
            )

    def get_query_object(self, request, context):
        query_object = super(
            ReportSettingsRegisterPack, self
        ).get_query_object(request, context)

        query_object.filter &= BE('shortname', BE.EQ, context.shortname)

        return query_object
