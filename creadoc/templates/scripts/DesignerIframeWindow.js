var iframe = Ext.get('creadoc-iframe');
var iframeWindow = iframe.dom.contentWindow;
var reportId = Ext.decode('{{ component.report_id }}');

// url для сохранения шаблона
var reportSaveUrl = '{{ component.save_report_url }}';
// url для снятия блокировки с шаблона
var reportReleaseUrl = '{{ component.release_report_url }}';


// Код клавиши "S"
var CharCodeS = 19;

// Сохранение шаблона при использовании комбинации клавиш ctrl + shift + S
iframeWindow.addEventListener('keypress', saveKeyPressHandler);
win.getEl().dom.addEventListener('keypress', saveKeyPressHandler);

function saveKeyPressHandler(e) {
    if (e.ctrlKey && e.shiftKey && e.charCode == CharCodeS) {
        saveTemplate();
    }
}


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
 * Замена идентификатора текущего редактируемого шаблона
 * @param response
 */
function replaceReportId(response) {
    var result = Ext.decode(response.responseText);

    if (result['success'] && result['report_id']) {
        reportId = result['report_id'];
    }
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
 * @param reportId
 * @param reportName
 * @param template
 */
function saveRequest(reportId, reportName, template) {
    var mask = new Ext.LoadMask(win.body, {msg: 'Сохранение...'});
    mask.show();

    var request = {
        url: reportSaveUrl,
        params: {
            'id': reportId || 0,
            'name': reportName || '',
            'report': template
        },
        success: function(response) {
            mask.hide();
            replaceReportId(response);
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
 *  На вход первым параметров получает введенное наименование.
 */
function showNameChangeDialog(callback) {
    Ext.Msg.prompt(
        'Сохранение шаблона',
        'Введите наименование шаблона',
        function(result, name) {
            if (result == 'ok' && name) {
                callback(name);
            }
        }
    );
}