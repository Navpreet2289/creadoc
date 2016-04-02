var iframe = Ext.get('creadoc-iframe');
var iframeWindow = iframe.dom.contentWindow;
var reportId = Ext.decode('{{ component.report_id }}');

// url для сохранения шаблона
var reportSaveUrl = '{{ component.save_report_url }}';
// url для снятия блокировки с шаблона
var reportReleaseUrl = '{{ component.release_report_url }}';
// url для открытия окна со списком доступных и подключенных источников данных
var reportSourcesWindowUrl = '{{ component.sources_window_url }}';

// Код клавиши "S"
var CharCodeS = 19;

// Сохранение шаблона при использовании комбинации клавиш ctrl + S
iframeWindow.addEventListener('keydown', function(e) {
    if (e.ctrlKey || e.metaKey) {
        e.preventDefault();

        if (e.charCode == CharCodeS) {
            saveTemplate();
        }
    }
});


/**
 * Проверка является ли текущий шаблон новым и еще не сохраненным
 * @returns {boolean}
 */
function isNewReport() {
    return reportId == 0;
}


/**
 * Формирование объекта события
 * @returns {CustomEvent}
 */
function getTemplateEvent(callback) {
    return new CustomEvent(
        'getTemplate', {
            bubbles : true,
            cancelable : true,
            detail: {'callback': callback}
        }
    );
}


/**
 * Формирование события на обновление списка источников данных
 * @param callback
 * @param rows
 * @returns {CustomEvent}
 */
function getDataSourceEvent(rows, callback) {
    return new CustomEvent('refreshSources', {
        bubbles : true,
        cancelable : true,
        detail: {'callback': callback, 'rows': rows}
    });
}


/**
 * Обработка диалога подтверждения закрытия окна
 * @returns {boolean}
 */
function closeWindow() {
    Ext.Msg.confirm(
        'Внимание!',
        'Все несохраненные изменения будут утеряны. Закрыть окно?',
        function(result) {
            if (result == 'yes') {
                requestReleaseReport(function() {
                    win.close(true);
                });
            }
        }
    );

    return false;
}


/**
 * Отправка запроса на освобождение мьютекса
 * @param callback Функция, вызываемая по окончанию запроса
 */
function requestReleaseReport(callback) {
    var request = {
        'url': reportReleaseUrl,
        'params': {
            'report_id': reportId
        },
        success: callback,
        failure: function() {
            uiAjaxFailMessage.apply(this, arguments);
        }
    };

    Ext.Ajax.request(request);
}


/**
 * Отправка запроса на сохранение шаблона
 * @param id
 * @param reportName
 * @param template
 */
function saveRequest(id, reportName, template) {
    var mask = new Ext.LoadMask(win.body, {msg: 'Сохранение...'});
    mask.show();

    var request = {
        url: reportSaveUrl,
        params: {
            'id': id || 0,
            'name': reportName || '',
            'report': template
        },
        success: function(response) {
            mask.hide();
            var result = Ext.decode(response.responseText);

            if (result['success'] && result['report_id']) {
                reportId = result['report_id'];
            }

            win.fireEvent('afterSaveReport', reportId, reportName, template);
        },
        failure: function() {
            mask.hide();
            uiAjaxFailMessage.apply(this, arguments);
        }
    };

    Ext.Ajax.request(request);
}


/**
 * Обертка над сохранением шаблона. Перед сохранением посылает событие на получение объекта шаблона.
 * @param reportId Идентификатор шаблона
 * @param reportName Наименование шаблона
 */
function saveRequestWrapper(reportId, reportName) {
    iframeWindow.dispatchEvent(getTemplateEvent(function(template) {
        saveRequest(reportId, reportName, template);
    }));
}


/**
 * Сохранение шаблона
 */
function saveTemplate() {
    if (isNewReport()) {
        showNameChangeDialog(function(name) {
            saveRequestWrapper(reportId, name, true);
        });
    } else {
        saveRequestWrapper(reportId, '');
    }
}


/**
 * Сохранение шаблона под новым наименованием
 */
function saveTemplateAs() {
    showNameChangeDialog(function(name) {
        // Освобождаем предыдущий шаблон перед тем,
        // как сохранить его под новым именем.
        requestReleaseReport(function() {
            saveRequestWrapper(0, name, true);
        });
    });
}


/**
 * Диалоговое окно с вводом наименования шаблона
 * @param callback Функция обратного вызова, срабатывающая после ввода наименования.
 *  На вход первым параметром получает введенное наименование.
 * @param message Кастомное сообщение в окне ввода наименования шаблона
 */
function showNameChangeDialog(callback, message) {
    if (!message) {
        message = 'Введите наименование шаблона';
    }

    Ext.Msg.prompt(
        'Сохранение шаблона',
        message,
        function(result, name) {
            if (result == 'ok' && name) {
                callback(name);
            }
        }
    );
}


/**
 * Отображение окна со списком доступных и подключенных источников данных
 */
function openDataSourceWindow() {
    // Чтобы привязать источник данных к шаблону нам нужно его вначале сохранить
    if (isNewReport()) {
        var message = 'Для подключения источника данных сначала требуется сохранить шаблон.' +
            '<br> Введите наименование шаблона.';

        showNameChangeDialog(function(name) {
            saveRequestWrapper(reportId, name);
        }, message);

        // При получении события об окончании сохранения шаблона
        // формируем запрос на получение окна со списком источников
        win.on('afterSaveReport', openDataSourceWindowRequest, win, {'single': true});
    } else {
        openDataSourceWindowRequest(reportId);
    }
}

/**
 * Запрос на формирование окна
 */
function openDataSourceWindowRequest(reportId) {
    var request = {
        url: reportSourcesWindowUrl,
        params: {'report_id': reportId},
        success: function(response) {
            var editWindow = smart_eval(response.responseText);
            editWindow.on('afterSaveSources', function(rows, callback) {
                iframeWindow.dispatchEvent(getDataSourceEvent(rows, callback));
                return true;
            });
        },
        failure: function() {
            uiAjaxFailMessage.apply(this, arguments);
        }
    };

    Ext.Ajax.request(request);
}