odoo.define('web_download_action.ActWindowActionManager', function (require) {
    "use strict";

    var ActionManager = require('web.ActionManager');

    ActionManager.include({

        base64toBlob: function (base64, type = 'application/octet-stream') {
            const fileDataInBase64 = base64;
            const fileDataInArray = atob(fileDataInBase64);
            const fileDataInUint8Array = new Uint8Array(fileDataInArray.length);
            for (let i = 0; i < fileDataInArray.length; i++) {
                fileDataInUint8Array[i] = fileDataInArray.charCodeAt(i);
            }
            return new Blob([fileDataInUint8Array], {type: type});
        },

        _downloadFile: function (action) {
            const blob = this.base64toBlob(action.file_data, action.file_type)
            const url = URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.download = action.file_name;
            document.body.appendChild(link);
            link.click();
            URL.revokeObjectURL(url);
        },

        _executeDownloadAction: function (action, options) {
            this._downloadFile(action);
            this._executeCloseAction(action, options);
        },

        _handleAction: function (action, options) {
            if (action.type === 'ir.actions.act_download') {
                return this._executeDownloadAction(action, options);
            }
            return this._super.apply(this, arguments);
        },

    });

});
