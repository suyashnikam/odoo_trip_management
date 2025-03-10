from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    weight = fields.Float(string="Weight", help="Total weight of this picking")

class Trip(models.Model):
    _name = 'trip.trip'
    _description = 'Trip Management'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Trip Name", required=True, copy=False, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('trip.trip'))
    operation_type_ids = fields.Many2many('stock.picking.type', string="Operation Types")
    picking_ids = fields.Many2many('stock.picking', string="Pickings", domain="[('state', 'in', ['assigned', 'waiting'])]")
    license_plate = fields.Many2one('fleet.vehicle', string="License Plate")
    vehicle_model = fields.Char(string="Vehicle Model", related="license_plate.model_id.name", readonly=True)
    driver_id = fields.Many2one('hr.employee', string="Driver")
    odometer_start = fields.Float(string="Odometer Start", readonly=True)
    odometer_end = fields.Float(string="Odometer End", readonly=True)
    attachment = fields.Binary(string="Attachment", readonly=True)
    weight_capacity = fields.Float(string="Weight Capacity", compute="_compute_weight_capacity", readonly=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string="Status", default="draft", tracking=True)
    batch_id = fields.Many2one('stock.picking.batch', string="Batch")

    @api.depends('picking_ids')
    def _compute_weight_capacity(self):
        for record in self:
            record.weight_capacity = sum(record.picking_ids.mapped('weight'))

    def action_confirm_trip(self):
        batch = self.env['stock.picking.batch'].create({
            'name': f'Batch for {self.name}',
            'picking_ids': [(6, 0, self.picking_ids.ids)],
        })
        self.write({'state': 'in_progress', 'batch_id': batch.id})

    @api.model
    def action_open_odometer_wizard(self):
        return {
            'name': 'Update Trip Odometer',
            'type': 'ir.actions.act_window',
            'res_model': 'trip.odometer.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'active_id': self.id},
        }




