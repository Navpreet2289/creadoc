# coding: utf-8
from m3_ext.ui.containers import ExtContainer, ExtPanel
from m3_ext.ui.windows import ExtEditWindow

__author__ = 'damirazo <me@damirazo.ru>'


class DesignerIframeWindow(ExtEditWindow):

    def __init__(self, url):
        super(DesignerIframeWindow, self).__init__()

        self.title = u'Дизайнер отчетов'
        self.maximized = True
        self.modal = True

        panel = ExtPanel()
        panel.html = (
            u'<iframe src="{}" width="99%" height="99%">'
            u'Фреймы не поддерживаются'
            u'</iframe>'
        ).format(url)

        self.layout = 'border'
        panel.region = 'center'
        panel.layout = 'fit'
        self.items.append(panel)
