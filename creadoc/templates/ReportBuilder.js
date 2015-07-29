(function() {
    // ******************************************************
    // Формирование запроса на сборку печатной формы
    // ******************************************************

    var request = {
        url: '{{ url }}',
        params: {
            report_id: '{{ report_id }}'
        },
        success: function(response) {
            debugger;
        },
        failure: uiAjaxFailMessage
    };

    Ext.Ajax.request(request);

})