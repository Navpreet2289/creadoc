# coding: utf-8
from m3_ext.ui.windows.edit_window import ExtEditWindow
from m3_ext.ui.controls.buttons import ExtButton
from m3_ext.ui.windows.window import ExtWindow
from m3_ext.ui.panels.grids import ExtObjectGrid


class CarEditWindow(ExtEditWindow):
    def __init__(self, *args, **kwargs):
        super(CarEditWindow, self).__init__(*args, **kwargs)


class CarListWindow(ExtWindow):
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

        self.grid = self._create_grid()

        self.items.append(self.grid)

    def _create_grid(self):
        grid = ExtObjectGrid(region='center')

        for column in self.columns:
            grid.add_column(**column)

        return grid
