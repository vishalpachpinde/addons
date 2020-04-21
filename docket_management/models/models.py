# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Project(models.Model):
    # _name = "project.project"
    _description = "Docket"
    _inherit = 'project.project'