# coding: utf-8
from creadoc.report.constants import RE_TAG_TEMPLATE

__author__ = 'damirazo'


def tag_data(value):
    u"""
    Информация о наличие тега в указанном теге
    """
    full_tag = None
    tag_name = None
    modifier = None
    unknown = None

    result = RE_TAG_TEMPLATE.findall(value)

    if len(result):
        full_tag, tag_name, modifier, unknown = result[0]

    return {
        # Тег целиком, вместе с признаками начала и окончания тега
        'full_tag': full_tag,
        # Наименование тега
        'tag_name': tag_name,
        # Модификатор
        'modifier': modifier,
        'unknown': unknown,
    }
