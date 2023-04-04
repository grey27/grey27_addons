from odoo import api, fields, models


class IrActionsActDownload(models.Model):
    _name = 'ir.actions.act_download'
    _description = 'Action Download'
    _table = 'ir_act_download'
    _inherit = 'ir.actions.actions'
    _sequence = 'ir_actions_id_seq'
    _order = 'name'

    name = fields.Char(string='Action Name', translate=True)
    type = fields.Char(default='ir.actions.act_download')
    file_name = fields.Char('File Name', required=True)
    file_type = fields.Char('File Type', required=True)
    file_data = fields.Text('File Data', required=True)

    def _get_readable_fields(self):
        return super()._get_readable_fields() | {
            "file_name", "file_type", "file_data",
        }
