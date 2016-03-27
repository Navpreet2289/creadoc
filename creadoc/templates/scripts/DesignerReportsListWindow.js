var grid = Ext.getCmp('{{ component.grid.client_id }}');

grid.on('aftereditrequest', refreshStoreHandler);
grid.on('afternewrequest', refreshStoreHandler);


/**
 * Обновление стора грида после закрытия окна создания/редактирование записи
 */
function refreshStoreHandler(cmp, response, request) {
    var editWin = smart_eval(response.responseText);

    if (editWin) {
        editWin.on('close', function() {
            grid.refreshStore();
        });
    }

    return false;
}