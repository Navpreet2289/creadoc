(function() {
    // ******************************************************
    // Формирование запроса на сборку печатной формы
    // ******************************************************

    // url экшена сборки ПФ
    var reportBuildUrl = '{{ url }}';
    // Идентификатор ПФ
    var reportId = '{{ report_id }}';
    // Требуется ли выделение записи в гриде для сборки ПФ
    var needSelection = Ext.decode('{{ need_selected|lower }}');
    // Объект грида
    var grid = Ext.getCmp('{{ grid_id }}');

    // Параметры сборки
    var params = {
        'report_id': reportId
    };

    if (needSelection) {
        var sm = grid.getSelectionModel();

        if (!sm.hasSelection()) {
            return Ext.Msg.alert('Внимание!', 'Требуется выделить запись!');
        }

        params['row_id'] = sm.getSelected().get('id');
    }

    var request = {
        url: reportBuildUrl,
        params: params,
        success: function(response) {
            debugger;
        },
        failure: uiAjaxFailMessage
    };

    Ext.Ajax.request(request);

})