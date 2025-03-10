from odoo import models, fields

class TripOdometerWizard(models.TransientModel):
    _name = 'trip.odometer.wizard'
    _description = 'Update Odometer and Attachment'

    trip_id = fields.Many2one('trip.trip', required=True)
    odometer_start = fields.Float(string="Odometer Start")
    odometer_end = fields.Float(string="Odometer End")
    attachment = fields.Binary(string="Attachment")

    def default_get(self, fields):
        res = super(TripOdometerWizard, self).default_get(fields)
        trip_id = self.env.context.get('active_id')
        if trip_id:
            res.update({'trip_id': trip_id})
        return res

    def update_trip_info(self):
        self.trip_id.write({
            'odometer_start': self.odometer_start,
            'odometer_end': self.odometer_end,
            'attachment': self.attachment,
        })
