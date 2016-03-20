var iframe = Ext.get('creadoc-iframe');
var reportId = Ext.decode('{{ component.report_id }}');
var isNew = reportId == 0;


win.on('beforeclose', onCloseWindow, win, {'single': true});


/**
 * Формирование объекта события
 * @returns {CustomEvent}
 */
function createEvent(name) {
    var params = {
        reportId: reportId,
        reportName: name || '',
        parentWindow: win
    };

    return new CustomEvent(
        'templatesave',
        {
            bubbles : true,
            cancelable : true,
            detail: params
        }
    );
}


/**
 * Обработчик, выполняемый при попытке закрытия окна с фреймом
 * @returns {boolean}
 */
function onCloseWindow() {
    Ext.Msg.confirm(
        'Внимание!',
        'Сохранить шаблон перед выходом?',
        function(result) {
            if (result == 'yes') {
                if (isNew) {
                    saveReport();
                } else {
                    iframe.dom.contentWindow.dispatchEvent(createEvent());
                    win.close(true);
                }
            }
        }
    );

    return false;
}


/**
 * Обработчик кнопки сохранения отчета
 */
function saveReport() {
    if (isNew) {
        Ext.Msg.prompt(
            'Сохранение шаблона',
            'Введите наименование шаблона',
            function(result, name) {
                if (result == 'ok' && name) {
                    // Отправляем событие о необходимости сохранения шаблона
                    iframe.dom.contentWindow.dispatchEvent(createEvent(name));
                    // Отписываемся от события при закрытии окна
                    win.un('beforeclose', onCloseWindow);
                    // Закрываем окно
                    win.close(true);
                }
            }
        );
    } else {
        Ext.Msg.confirm(
            'Внимание!',
            'Сохранить шаблон и закрыть окно?',
            function(result) {
                if (result == 'yes') {
                    // Отправляем событие о необходимости сохранения шаблона
                    iframe.dom.contentWindow.dispatchEvent(createEvent());
                    // Отписываемся от события при закрытии окна
                    win.un('beforeclose', onCloseWindow);
                    // Закрываем окно
                    win.close(true);
                }
            }
        );
    }

    return false;
}