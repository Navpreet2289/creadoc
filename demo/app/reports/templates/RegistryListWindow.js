var grid = Ext.getCmp('{{ component.grid.client_id }}');
var printUrl = '{{ component.print_url }}';
var viewerUrl = '{{ component.viewer_url }}';


function printReport(reportId) {
    // pass
}


function showReport(reportId) {
    return function() {
        var record = getSelectedRecord();
        if (!record) {
            return;
        }

        var request = {
            url: viewerUrl,
            params: {
                'report_id': reportId, 
                'params': Ext.encode({'row_id': record.get('id')})
            },
            success: function(response) {
                var viewerWin = smart_eval(response.responseText);
            },
            failure: function() {
                uiAjaxFailMessage.apply(this, arguments);
            }
        };

        Ext.Ajax.request(request);
    }
}


function getSelectedRecord() {
    var sm = grid.getSelectionModel();
    if (!sm.hasSelection()) {
        return showWarning('Не выбрана запись!')
    }

    return sm.getSelected();
}