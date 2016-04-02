var gridSource = Ext.getCmp('{{ component.source_grid.client_id }}');
var gridDestination = Ext.getCmp('{{ component.destination_grid.client_id }}');


/**
 * Подключение выбранного источника данных к шаблону
 */
function plugSource() {
    var record = getSelectedRecord(gridSource);

    if (record) {
        moveRecordToOtherGrid(record, gridSource, gridDestination);
    }
}


/**
 * Отключение выбранного источника данных от шаблона
 */
function unplugSource() {
    var record = getSelectedRecord(gridDestination);

    if (record) {
        moveRecordToOtherGrid(record, gridDestination, gridSource);
    }
}


/**
 * Получение текущей выделенной записи из указанного грида
 * В случае, если запись не выделена - выводим окно с предупреждением
 */
function getSelectedRecord(grid) {
    var selectionModel = grid.getSelectionModel();
    if (selectionModel.hasSelection()) {
        return selectionModel.getSelected();
    } else {
        showWarning('Не выбрана запись!', 'Внимание!');
    }
}


/**
 * Перенос указанной записи из sourceGrid в destinationGrid
 */
function moveRecordToOtherGrid(record, sourceGrid, destinationGrid) {
    var newRecord = new Ext.data.Record(record.data);

    destinationGrid.getStore().add(newRecord);
    sourceGrid.getStore().remove(record);

    win.changesCount += 1
}


/**
 * Отправка запроса на сохранение изменений в списке источников данных
 */
function saveSources() {
    var mask = new Ext.LoadMask(win.body);
    mask.show();

    var request = {
        'url': '',
        'params': {},
        'success': function(response) {
            mask.hide();
            debugger;
        },
        'failure': function() {
            mask.hide();
            uiAjaxFailMessage.apply(this, arguments);
        }
    };

    Ext.Ajax.request(request);
}


/**
 * Закрытие окна
 */
function closeWindow() {
    win.close();
}