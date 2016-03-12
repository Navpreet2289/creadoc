var iframe = Ext.get('creadoc-iframe');


win.on('beforeclose', onCloseWindow, win, {'single': true});


function onCloseWindow() {
    var templateSaveEvent = new CustomEvent(
        'templatesave', {
            bubbles : true,
            cancelable : true,
            parentWindow: win
        }
    );

    Ext.Msg.confirm(
        'Внимание!',
        'Сохранить изменения перед выходом?',
        function(result) {
            if (result == 'yes') {
                win.on('beforeclose', onCloseWindow, win, {'single': true});
                iframe.dom.contentWindow.dispatchEvent(templateSaveEvent);
            } else {
                win.close(true);
            }
        }
    );

    return false;
}