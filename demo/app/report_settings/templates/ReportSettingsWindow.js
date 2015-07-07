var grid = Ext.getCmp('{{ component.grid.client_id }}'),
    gridStore = grid.getStore(),
    reportGrid = Ext.getCmp('{{ component.report_grid.client_id }}'),
    reportGridStore = reportGrid.getStore();


grid.on('rowclick', function(cmp, rowIndex, event) {
    var record = gridStore.getAt(rowIndex);

    reportGridStore.baseParams['shortname'] = record.get('shortname');
    reportGridStore.reload();
});


reportGrid.on('beforenewrequest', function(cmp, request) {
    setShortName(request);
});


reportGrid.on('beforeeditrequest', function(cmp, request) {
    setShortName(request);
});


reportGrid.on('beforedeleterequest', function(cmp, request) {
    setShortName(request);
});


function setShortName(request) {
    var record = grid.getSelectionModel().getSelected();

    if (record === undefined) {
        Ext.MessageBox.alert('Внимание!', 'Выберите реестр!');
        return false;
    } else {
        request.params['shortname'] = record.get('shortname');
    }
}