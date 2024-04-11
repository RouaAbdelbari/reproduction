# -*- coding: utf-8 -*-

from odoo import api, fields, models, _, tools
import logging
from odoo.exceptions import ValidationError
import datetime


logger = logging.getLogger(__name__)


class Physician(models.Model):
    _name = 'clinic.physician'
    _description = 'Physician'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name",
                       required=True,
                       store=True,
                       readonly=False,
                       copy=False,
                       help="Physician Name", )

    medical_license = fields.Char(string="Medical License",
                       required=False,
                       store=True,
                       readonly=False,
                       copy=False,
                       help="Medical License", )

    # partner_id = fields.Many2one(
    #         comodel_name='clinic.physician.specialty', # Linked Model
    #         string="Specialty", # Field Name
    #         tracking=1, # The changes will appear in oe_chatter
    #         copy=False,  # For duplicate record
    #         required=True, # must fill by end user
    #         index=True, # Index the data in the table
    #         change_default=True, # whether the field may trigger a "user-onchange"
    #         help="Customer Info",
    #         readonly=False, # if this vield editable or not
    #         compute="_compute_journal_id",  # name of a method that computes the field
    #         precompute=True, # whether the field should be computed before record insertion
    #         store=True, #whether the field is stored in database
    #         ondelete="set null", # null "default" / cascade / restrict / set VALUE /set default
    #         check_company=True, # it will filter the list of view based on currrent selected company, You have to add tag "_check_company_auto = True" on class level
    #         domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")



    @api.model_create_multi
    def create(self, vals):
        try:
            obj = super(Physician, self).create(vals)
        except Exception as e:
            logger.exception("create Method")
            raise ValidationError(e)
        return obj

    def write(self, vals):
        try:
            obj = super(Physician, self).write(vals)
        except Exception as e:
            logger.exception("Write Method")
            raise ValidationError(e)
        return obj

    def unlink(self):
        try:
            return super(Physician, self).unlink()
        except Exception as e:
            logger.exception("unlink Method")
            raise ValidationError(e)
