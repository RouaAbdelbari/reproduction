# -*- coding: utf-8 -*-

from odoo import api, fields, models, _, tools
import logging
from odoo.exceptions import ValidationError
import datetime

logger = logging.getLogger(__name__)


class PhysicianSpecialty(models.Model):
    _name = 'clinic.physician.specialty'
    _rec_name = 'name'
    _description = 'Physician Specialty'

    code = fields.Char(string="Code",
                       required=True,
                       store=True,
                       readonly=False,
                       copy=False,
                       help="Physician Specialty Code", )
    name = fields.Char(string="Name",
                       required=True,
                       store=True,
                       readonly=False,
                       copy=False,
                       translate=True,
                       help="Physician Specialty Name", )

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Name must be unique!'),
    ]



    @api.model_create_multi
    def create(self, vals):
        try:
            obj = super(PhysicianSpecialty, self).create(vals)
        except Exception as e:
            logger.exception("create Method")
            raise ValidationError(e)
        return obj

    def write(self, vals):
        try:
            obj = super(PhysicianSpecialty, self).write(vals)
        except Exception as e:
            logger.exception("Write Method")
            raise ValidationError(e)
        return obj

    def unlink(self):
        try:
            return super(PhysicianSpecialty, self).unlink()
        except Exception as e:
            logger.exception("unlink Method")
            raise ValidationError(e)
