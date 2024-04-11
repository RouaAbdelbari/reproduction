from odoo import _, models, fields, api
class reproduction(models.Model):
    _name = 'reproduction.vache'
    _description = 'reproduction.vache'
    _inherit = ['mail.thread','mail.activity.mixin']

    reference = fields.Char(string="Reference", required=True, copy=False, readonly=True, default=lambda 
                            self: _('New'))
    sexe = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Sexe')
    poids = fields.Float(string='Poids')
    race = fields.Char(string='Race')
    couleur = fields.Char(string='Couleur')
    date_naissance = fields.Date(string='Date de naissance')
    mere_id = fields.Many2one('reproduction.vache', string='Mére')
    pere_id = fields.Many2one('reproduction.vache', string='Pére')
    statut_reproduction = fields.Selection([
    ('en_cours', 'En cours d\'élevage'),
    ('disponible_vente', 'Disponible pour la vente'),
        ], string='Reproduction Status')
    poids_ids = fields.One2many('reproduction.poids_vache', 'vache_id', string='Poids')
    date_achat = fields.Date(string='Date d\'achat') 
    age_achat = fields.Integer(string='Âge à l\'achat')
    active = fields.Boolean(string='Active', default=True)
    date_poids = fields.Date(string='Date du poids')
    image = fields.Binary(string='Image')
    status = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), ('done', 'Done'), ('cancel', 'Cancelled')],
                              string='Status', default='draft', track_visibility='onchange')
    veaux_count = fields.Integer(string='Number of Calves', compute='_compute_veau_count', store=True)
    ordonnance = fields.Text(string='Prescription vétérinaire')
    note = fields.Text(string='Other Information')
    message_follower_ids = fields.One2many('mail.followers', 'res_id', string="Suiveurs")
    activity_ids = fields.One2many('mail.activity', 'res_id', string="ActivitÃ©s")
    message_ids = fields.One2many('mail.message', 'res_id', string="Messages")


    quantite_lait = fields.Float(string='Quantité de lait')
    @api.model 
    def create(self, vals):
        if not vals.get('note'):
            vals['note']='New Vache'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('reproduction.vache') or _('New')
        res = super(reproduction, self).create(vals)
        return res   
    def action_confirm(self):
        self.status='confirm'
    def action_add_poids(self):
        self.ensure_one()
        self.poids_ids.create({
            'vache_id': self.id,
        })
class PoidsVache(models.Model):
    _name = 'reproduction.poids_vache'
    _description = 'Poids de la vache'
    vache_id = fields.Many2one('reproduction.vache', string='Vache')
    poids = fields.Float(string='Poids')
    date = fields.Date(string='Date', default=fields.Date.today())
class Technicien(models.Model):
    _name = 'reproduction.technicien'
    _description = 'Technicien Agricole'
    _inherit = ['mail.thread','mail.activity.mixin']
    reference = fields.Char(string="Reference", required=True, copy=False, readonly=True, default=lambda self: _('New'))    
    name = fields.Char(string='Nom')
    technicien_id = fields.Many2one('res.partner', string='Technicien ID')
    adresse = fields.Text(string='Adresse')
    telephone = fields.Char(string='Téléphone')
    date_embauche = fields.Date(string='Date d\'embauche')
    specialite = fields.Char(string='Spécialité')
    active = fields.Boolean(string='Actif', default=True)
    email = fields.Char(string='Email')
    note = fields.Text(string='Note')
    competences = fields.Text(string='Compétences')
    compte_bancaire_id = fields.Many2one('res.partner.bank', string='Compte Bancaire')
    numero_secu_sociale = fields.Char(string='Numéro Sécurité Sociale')
    numero_passeport = fields.Char(string='Numéro Passeport')
    etat_civil = fields.Selection([
        ('celibataire', 'Célibataire'),
        ('marie', 'Marié(e)'),
        ('divorce', 'Divorcé(e)'),
        ('veuf', 'Veuf/Veuve')
    ], string='État Civil')
    specialite = fields.Selection([
    ('agriculture_generale', 'Agriculture générale'),
    ('elevage', 'Élevage'),
    ('horticulture', 'Horticulture'),
    ('agroalimentaire', 'Agroalimentaire'),
    ('agriculture_biologique', 'Agriculture biologique'),
    ('agriculture_durable', 'Agriculture durable'),
    ('agriculture_integree', 'Agriculture intégrée'),
      ], string="Spécialité")  
    telephone_urgence = fields.Char(string='Téléphone d\'urgence')
    distance_travail_domicile = fields.Float(string='Distance Travail-Domicile')
    image = fields.Binary(string='Image')
    lieu_naissance = fields.Char(string='Lieu de Naissance')
    pays_naissance = fields.Many2one('res.country', string='Pays de Naissance')
    status = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), ('done', 'Done'), ('cancel', 'Cancelled')],
                              string='Status', default='draft', track_visibility='onchange')
    message_follower_ids = fields.One2many('mail.followers', 'res_id', string="Suiveurs")
    activity_ids = fields.One2many('mail.activity', 'res_id', string="ActivitÃ©s")
    message_ids = fields.One2many('mail.message', 'res_id', string="Messages")
    @api.model 
    def create(self, vals):
        if not vals.get('note'):
            vals['note']='New Vache'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('reproduction.technicien') or _('New')
        res = super(Technicien, self).create(vals)
        return res  
    def action_confirm(self):
        self.status='confirm'
        

class Insemination(models.Model):
    _name = 'reproduction.insemination'
    _description = 'Model for managing inseminations'

    reference = fields.Char(string="Reference", required=True, copy=False, readonly=True, default=lambda self: _('New'))    
    cow_id = fields.Many2one('reproduction.vache', string='Vache')
    date = fields.Date(string='Date')
    insemination_type = fields.Selection([('naturelle', 'Naturelle'), ('artificielle', 'Artificielle')], string='Type d\'insémination')
    active = fields.Boolean(string='Active')
    montant = fields.Float(string='Montant')
    note = fields.Text(string='Note')
    successful = fields.Boolean(string='Successful')
    def action_confirm(self):
        self.status='confirm'
    @api.model 
    def create(self, vals):
        if not vals.get('note'):
            vals['note']='New Vache'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('reproduction.insemination') or _('New')
        res = super(Insemination, self).create(vals)
        return res  
   


class Farm(models.Model):
    _name = 'company.form'
    _description = 'Model for managing farms'

    nom = fields.Char(string='Nom')
    rue = fields.Char(string='Adresse - Rue')
    rue2 = fields.Char(string='Adresse - Rue 2')
    ville = fields.Char(string='Ville')
    vat = fields.Char(string='TVA')
    responsable = fields.Char(string='Responsable')
    mobile = fields.Char(string='Mobile')
    email = fields.Char(string='Email')
    site_internet = fields.Char(string='Site Internet', widget='url')
    image = fields.Binary(string='Image')
    social_media = fields.Many2many('social.media', 'farm_social_media_rel', 'farm_id', 'social_media_id', string='Réseaux sociaux')
class Ecurie(models.Model):
    _name = 'reproduction.ecurie'
    _description = 'Model for managing stables'
    _inherit = ['mail.thread','mail.activity.mixin']


    reference = fields.Char(string="Reference", required=True, copy=False, readonly=True, default=lambda self: _('New'))    
    image = fields.Binary(string='Image')
    reference = fields.Char(string='Reference', readonly=True)
    responsable_id = fields.Many2one('reproduction.technicien', string='Responsible')
    capacite = fields.Integer(string='Capacity')
    active = fields.Boolean(string='Active', default=True)
    animaux_ids = fields.Many2many('reproduction.vache', string='Animals')
    note = fields.Text(string='Note')
    ecurie_id = fields.Many2one('reproduction.ecurie', string='Ecurie')
    message_follower_ids = fields.One2many('mail.followers', 'res_id', string="Suiveurs")
    activity_ids = fields.One2many('mail.activity', 'res_id', string="ActivitÃ©s")
    message_ids = fields.One2many('mail.message', 'res_id', string="Messages")
    categorie = fields.Selection([
    ('chevaux', 'Chevaux'),
    ('vaches', 'Vaches'),
    ('moutons', 'Moutons'),
    ('autres', 'Animaux')
     ], string='Catégorie')
    status = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), ('done', 'Done'), ('cancel', 'Cancelled')],
                              string='Status', default='draft', track_visibility='onchange')
    def action_confirm(self):
        self.status='confirm'
    @api.model 
    def create(self, vals):
        if not vals.get('note'):
            vals['note']='New Vache'
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('reproduction.ecurie') or _('New')
        res = super(Ecurie, self).create(vals)
        return res  
   
class Veaux(models.Model):
    _name = 'reproduction.veaux'
    _description = 'Model for managing calves'

    poids = fields.Float(string='Poids')
    race = fields.Char(string='Race')
    couleur = fields.Char(string='Couleur')
    sexe = fields.Selection([('male', 'Mâle'), ('female', 'Femelle')], string='Sexe')
    date_naissance = fields.Date(string='Date de naissance')
    mere_id = fields.Many2one('reproduction.animal', string='Mère')
    pere_id = fields.Many2one('reproduction.animal', string='Père')
    statut_reproduction = fields.Selection([('gestation', 'Gestation'), ('allaitement', 'Allaitement'), ('croissance', 'Croissance')], string='Statut de reproduction')
    image = fields.Binary(string='Image')
    ecurie_id = fields.Many2one('reproduction.ecurie', string='Écurie')
class HeatPeriod(models.Model):
    _name = 'reproduction.period'
    _description = 'Heat Period'

    reference = fields.Char(string="Reference", required=True, copy=False, readonly=True, default=lambda self: _('New'))
    start_date = fields.Date(string='Date de début')
    temperature = fields.Float(string='Temperature')
    vache_id = fields.Many2one('reproduction.vache', string='Vache')
    message_follower_ids = fields.One2many('mail.followers', 'res_id', string="Suiveurs")
    activity_ids = fields.One2many('mail.activity', 'res_id', string="Activités")
    message_ids = fields.One2many('mail.message', 'res_id', string="Messages")
    def action_confirm(self):
        self.status = 'confirm'

    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('reproduction.period') or _('New')
        res = super(HeatPeriod, self).create(vals)
        return res
