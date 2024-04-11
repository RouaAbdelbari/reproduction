from odoo import models, fields, api, _
from odoo.exceptions import UserError
class Production_laitiere(models.Model):
    _name = 'production_laitiere.production_laitiere'
    _description = 'production_laitiere.production_laitiere'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    name = fields.Text('Name')
    reference = fields.Char(string="Reference", required=True, copy=False, readonly=True, default=lambda self: _('New'))
    quantite = fields.Float('Quantité (L)', help='Quantité en litres')
    date = fields.Date(string='Date de prodction', required=True , tracking=True)
    vache_id= fields.Many2one('reproduction.reproduction', string='Vache')
    commentaire = fields.Text('Commentaire')
    type_lait = fields.Selection([('vache', 'Lait de vache'), ('chèvre', 'Lait de chèvre')], string='Type de lait')
    teneur_mat_grasse = fields.Float('Teneur en matière grasse (%)')
    teneur_proteine = fields.Float('Teneur en protéines (%)')
    technicien_id = fields.Many2one('reproduction.technicien', string='Technicien')
    note=  fields.Text(string="Note")
    remarque=  fields.Text(string="Remarque")
    status = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled')], string='Status', default='draft', tracking=True)
    image = fields.Binary(string='Image')
    message_follower_ids = fields.One2many('mail.followers', 'res_id', string="Suiveurs")
    activity_ids = fields.One2many('mail.activity', 'res_id', string="ActivitÃ©s")
    message_ids = fields.One2many('mail.message', 'res_id', string="Messages")
    def action_confirm(self):
        self.status='confirm'
    def action_done(self):
        self.status='done'
    def action_draft(self):
        self.status='draft'
    def action_cancel(self):
        self.status='cancel'
    @api.model
    def create(self, vals):
        if not vals.get('reference') or vals.get('reference') == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('production_laitiere') or _('New')
        return super(Production_laitiere, self).create(vals)
class PlanificationProduction(models.Model):
    _name = 'production_laitiere.planning'
    _description = "Planification de la production"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    
    reference = fields.Char(string="Reference", required=True, copy=False, readonly=True, default=lambda self: _('New'))
    technicien_id = fields.Many2one('reproduction.technicien', string='Technicien')
    date_planifiee = fields.Date('Date planifiée', required=True)
    vache_id= fields.Many2one('reproduction.reproduction', string='Vache')
    notes = fields.Text('Notes')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled')], string='Status', default='draft', tracking=True)
    message_follower_ids = fields.One2many('mail.followers', 'res_id', string="Suiveurs")
    activity_ids = fields.One2many('mail.activity', 'res_id', string="ActivitÃ©s")
    message_ids = fields.One2many('mail.message', 'res_id', string="Messages")
    @api.model
    def create(self, vals):
        record = super(PlanificationProduction, self).create(vals)
        if record.technicien_id:
            record.technicien_id.message_post(body="Vous avez une nouvelle planification de production.")
        return record
    def action_confirm(self):
        self.status='confirm'
    def action_done(self):
        self.status='done'
    def action_draft(self):
        self.status='draft'
    def action_cancel(self):
        self.status='cancel'

class NiveauStock(models.Model):
    _name = 'production_laitiere.level'
    _description = 'Niveaux de stock'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    produit_reference = fields.Many2one('production_laitiere.production_laitiere', string='Produit', required=True)
    type_lait = fields.Selection([('vache', 'Lait de vache'), ('chèvre', 'Lait de chèvre')], string='Type de lait', related='produit_reference.type_lait', store=True)
    quantite_en_stock = fields.Float('Quantité en stock', compute='_compute_quantite_en_stock', store=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled')], string='Status', default='draft', tracking=True)
    message_follower_ids = fields.One2many('mail.followers', 'res_id', string="Suiveurs")
    activity_ids = fields.One2many('mail.activity', 'res_id', string="Activités")
    message_ids = fields.One2many('mail.message', 'res_id', string="Messages")
    product_document_count = fields.Integer(string='Nombre de documents')
    
    @api.depends('produit_reference', 'produit_reference.type_lait', 'produit_reference.quantite')
    def _compute_quantite_en_stock(self):
        for record in self:
            total_quantity = sum(record.filtered(lambda r: r.produit_reference.type_lait == record.type_lait).mapped('produit_reference.quantite'))   
            record.quantite_en_stock = total_quantity

    def action_confirm(self):
        self.status='confirm'

    def action_done(self):
        self.status='done'

    def action_draft(self):
        self.status='draft'

    def action_cancel(self):
        self.status='cancel'
    @api.depends('produit_reference', 'produit_reference.type_lait', 'produit_reference.quantite')
    def _compute_quantite_en_stock(self):
      for record in self:
        total_quantity = sum(record.filtered(lambda r: r.produit_reference.type_lait == record.type_lait).mapped('produit_reference.quantite'))   
        record.quantite_en_stock = total_quantity
    @api.model
    def action_open_documents(self):
        # Récupérer l'enregistrement actuel
        current_record = self.ensure_one()

        # Ouvrir une vue pour afficher les documents liés à l'enregistrement actuel
        return {
            'name': 'Documents',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'production_laitiere.documents',  # Remplacer 'production_laitiere.documents' par votre modèle de documents
            'domain': [('level_id', '=', current_record.id)],  # Filtrer les documents liés à l'enregistrement actuel
        }
  
class StockMove(models.Model):
    _name = 'production_laitiere.mvt'
    _description = 'Niveaux de stock'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    reference = fields.Char(string="Reference", required=True, copy=False, readonly=True, default=lambda self: _('New'))
    client_id = fields.Many2one('production_laitiere.client', string='Client')
    type_lait = fields.Selection([('vache', 'Lait de vache'), ('chèvre', 'Lait de chèvre')], string='Type de lait', required=True)

    quantite_en_stock = fields.Float(string='Quantité en stock (litre)', compute='_compute_quantite_en_stock', store=True)
    quantite_saisie = fields.Float(string='Quantité saisie (litre)', required=True)
    date_mouvement = fields.Date(string="Date de mouvement", default=fields.Date.today)
    type_mouvement = fields.Selection([
    ('livraison', 'Livraison'),
    ('importation', 'Importation'),
    ('transfert', 'Transfert')], 
    string='Type de mouvement', required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled')], string='Status', default='draft', tracking=True)
    message_follower_ids = fields.One2many('mail.followers', 'res_id', string="Suiveurs")
    activity_ids = fields.One2many('mail.activity', 'res_id', string="Activités")
    message_ids = fields.One2many('mail.message', 'res_id', string="Messages")
    methode_paiement = fields.Selection([
    ('espece', 'Espèces'),
    ('carte', 'Carte de crédit'),
    ('virement', 'Virement bancaire'),
    ('cheque', 'Chèque')], 
    string='Méthode de paiement')
    prix = fields.Float(string='Prix', compute='_compute_prix', store=True)
   
    @api.constrains('quantite_saisie')
    def _check_quantite_disponible(self):
        for record in self:
            if record.quantite_saisie > record.quantite_en_stock:
                raise UserError("La quantité saisie n'est pas disponible en stock pour le type de lait sélectionné !")

    def action_confirm(self):
        self._check_quantite_disponible()
        self.status = 'confirm'

    def action_done(self):
        self.status = 'done'

    def action_draft(self):
        self.status = 'draft'

    def action_cancel(self):
        self.status = 'cancel'
    @api.depends('type_lait')
    def _compute_quantite_en_stock(self):
      for record in self:
        total_quantity = sum(self.env['production_laitiere.level'].search([('type_lait', '=', record.type_lait)]).mapped('quantite_en_stock'))
        record.quantite_en_stock = total_quantity
    @api.model
    def create(self, vals):
        if not vals.get('reference') or vals.get('reference') == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('mvt') or _('New')
        return super(StockMove, self).create(vals)
    def action_confirm(self):
        for record in self:
            if record.quantite_saisie > record.quantite_en_stock:
                raise UserError("La quantité saisie n'est pas disponible en stock pour le type de lait sélectionné !")
            level_records = self.env['production_laitiere.level'].search([('type_lait', '=', record.type_lait)])
            for level_record in level_records:
                if level_record.quantite_en_stock >= record.quantite_saisie:
                    level_record.quantite_en_stock -= record.quantite_saisie
                    break
            else:
                raise UserError("La quantité saisie n'est pas disponible en stock pour le type de lait sélectionné !")
    @api.depends('quantite_saisie')
    def _compute_prix(self):
        for record in self:
          if record.quantite_saisie < 0:
            raise ValidationError("La quantité saisie ne peut pas être négative.")
        # Définir le prix unitaire directement dans la méthode
        prix_unitaire = 5  # Prix unitaire en euros
        record.prix = record.quantite_saisie * prix_unitaire
    @api.model
    def action_compute_prix(self):
     for record in self:
        record._compute_prix()
   


class Client(models.Model):
    _name = 'production_laitiere.client'
    _description = 'Client'
    _inherit = ['mail.thread', 'mail.activity.mixin']

   
    reference = fields.Char(string="Reference", required=True, copy=False, readonly=True, default=lambda self: _('New'))
    nom= fields.Char(string='Nom', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Téléphone')
    addresse = fields.Text(string='Adresse')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled')], string='Status', default='draft', tracking=True)
    partenaire_type = fields.Selection([
        ('client', 'Client'),
        ('fournisseur', 'Fournisseur'),
        ('partenaire', 'Partenaire'),
        ('autre', 'Autre'),
    ], string='Type de partenaire', default='client')
    message_follower_ids = fields.One2many('mail.followers', 'res_id', string="Suiveurs")
    activity_ids = fields.One2many('mail.activity', 'res_id', string="ActivitÃ©s")
    message_ids = fields.One2many('mail.message', 'res_id', string="Messages")
    def action_confirm(self):
        self.status='confirm'

    def action_done(self):
        self.status='done'

    def action_draft(self):
        self.status='draft'

    def action_cancel(self):
        self.status='cancel'
    @api.model
    def create(self, vals):
        if not vals.get('reference') or vals.get('reference') == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('client') or _('New')
        return super(Client, self).create(vals)
class TechnicienAgricole(models.Model):
    _inherit = 'reproduction.technicien'
    _description = 'Technicien Agricole'
