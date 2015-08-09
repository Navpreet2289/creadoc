# coding: utf-8
from m3.actions import OperationResult

__author__ = 'damirazo <me@damirazo.ru>'


class IFrameDownloadResult(OperationResult):
    u"""
    Генерация iframe с ссылкой на скачивание файла
    """

    def __init__(self, file_url):
        self.url = file_url
        safe_js_handler = '''function() {
            var iframe = document.createElement("iframe");
            iframe.src = '%s';
            iframe.style.display = "none";
            document.body.appendChild(iframe);
        }'''
        super(IFrameDownloadResult, self).__init__(
            code=safe_js_handler % file_url)
