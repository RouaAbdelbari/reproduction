# -*- coding: utf-8 -*-

from odoo import api, fields, models, _, tools
import logging
from odoo.exceptions import ValidationError
import datetime

logger = logging.getLogger(__name__)


class PhysicianDegree(models.Model):
    _name = 'clinic.physician.degree'
    _rec_name = 'name'
    _description = 'Store Physician Degrees'

    name = fields.Char()
    # physician_ids = fields.One2many(comodel_name='clinic.physician', inverse_name='user_id', string='Related Physician')

    @api.model_create_multi
    def create(self, vals):
        try:
            obj = super(PhysicianDegree, self).create(vals)
        except Exception as e:
            logger.exception("create Method")
            raise ValidationError(e)
        return obj

    def write(self, vals):
        try:
            obj = super(PhysicianDegree, self).write(vals)
        except Exception as e:
            logger.exception("Write Method")
            raise ValidationError(e)
        return obj

    def unlink(self):
        try:
            return super(PhysicianDegree, self).unlink()
        except Exception as e:
            logger.exception("unlink Method")
            raise ValidationError(e)
