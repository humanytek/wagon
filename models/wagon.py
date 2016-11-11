from openerp import api, fields, models


class Wagon(models.AbstractModel):
    _inherit = 'vehicle'
    _name = 'wagon'

    wagon = fields.Char()
    order_num = fields.Char(string="Numero de pedido")

    zvp_id = fields.Many2one('zvp')
    zvp_partner = fields.Char(related="zvp_id.partner", readonly=True)

    seal_down_from = fields.Char()
    seal_down_to = fields.Char()
    seal_up_from = fields.Char()
    seal_up_to = fields.Char()

    weight_1 = fields.Float()
    weight_2 = fields.Float()
    weight_3 = fields.Float()
    weight_4 = fields.Float()

    @api.one
    @api.depends('weight_1', 'weight_2', 'weight_3', 'weight_4')
    def _compute_raw_kilos(self):
        self.raw_kilos = self.weight_1 + self.weight_2 + self.weight_3 + self.weight_4
