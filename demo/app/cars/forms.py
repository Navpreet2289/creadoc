# coding: utf-8
from m3_ext.ui.windows.edit_window import ExtEditWindow
from demo.app.forms import BaseListWindow


class CarEditWindow(ExtEditWindow):
    def __init__(self, *args, **kwargs):
        super(CarEditWindow, self).__init__(*args, **kwargs)


class CarListWindow(BaseListWindow):
    u"""
    """

    columns = {
        'header': u'Марка',
        'data_index': 'marka',
        'sortable': True,
    }, {
        'header': u'Серия',
        'data_index': 'seria',
        'sortable': True,
    }, {
        'header': u'Год выпуска',
        'data_index': 'year',
        'sortable': True,
    },

    def __init__(self):
        super(CarListWindow, self).__init__()

        self.title = u'Список автомобилей'
        self.icon_cls = 'icon-application-view-list'
        self.layout = 'border'
        self.width, self.height = 800, 600
        self.maximized = False
        self.maximizable = False
        self.minimizable = True
