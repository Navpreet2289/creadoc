var grid = Ext.getCmp('{{ component.grid.client_id }}');
var viewerUrl = '{{ component.viewer_url }}';


/**
 * Печать отчета в "фоновом" режиме, без запуска просмотрщика
 * @param reportId Идентификатор отчета
 */
function printReport(reportId) {
    return function() {
        loadViewerRequest(reportId, true);
        if (console && console.log) {
            console.log('Функция не реализована, используется стандартный функционал вьювера');
        }
    }
}


/**
 * Запуск просмотрщика с возможностью просмотра и печати отчета
 * @param reportId Идентификатор отчета
 */
function showReport(reportId) {
    return function() {
        loadViewerRequest(reportId, false);
    }
}


/**
 * Запрос на запуск "просмотрщика" отчетных форм
 * @param reportId Идентификатор отчета
 * @param backgroundMode Режим фоновой работы.
 *  В данном режиме окно просмотрщика не запускается,
 *  а используется прямая генерация отчета.
 *  На текущий момент данный функционал не реализован.
 */
function loadViewerRequest(reportId, backgroundMode) {
    var record = getSelectedRecord();
    if (!record) {
        return;
    }

    var request = {
        url: viewerUrl,
        params: {
            'report_id': reportId,
            'background_mode': backgroundMode,
            'params': Ext.encode({'row_id': record.get('id')})
        },
        success: function(response) {
            smart_eval(response.responseText);
        },
        failure: function() {
            uiAjaxFailMessage.apply(this, arguments);
        }
    };

    Ext.Ajax.request(request);
}


/**
 * Получение выделенной записи грида. В случае отсутствия выводится предупреждение.
 * @returns {*}
 */
function getSelectedRecord() {
    var sm = grid.getSelectionModel();
    if (!sm.hasSelection()) {
        return showWarning('Не выбрана запись!')
    }

    return sm.getSelected();
}