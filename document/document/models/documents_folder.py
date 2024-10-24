# -*- coding: utf-8 -*-
# © 2024 Sergio Martínez Meneses
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

import logging
from odoo import models, fields, exceptions

_logger = logging.getLogger(__name__)

class Folder(models.Model):
    _name = 'documents.folder'
    _description = 'Diferentes folders para gestionar los archivos'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción de la carpeta')
    parent_id = fields.Many2one('documents.folder', string='Carpeta padre', ondelete='cascade')
    child_ids = fields.One2many('documents.folder', 'parent_id', string='Carpetas hijas', readonly=True)
    document_ids = fields.One2many('documentos.documentos', 'folder_id', string='Documentos')
    create_date = fields.Datetime(string='Fecha de creación', readonly=True)
    write_date = fields.Datetime(string='Fecha de actualización', readonly=True)
    
    edit_groups_id = fields.Many2many(
    'res.groups',
    'documents_folder_edit_rel', 
    'folder_id', 'group_id',
    string='Grupos que pueden editar'
    )
    
    def check_access_rule(self, operation):
        if operation == 'write':
            if self.edit_groups_id:
                if not self.env.user.groups_id & self.edit_groups_id:
                    raise exceptions.AccessError("No tienes permiso para editar este registro")
            else:
                return True
        return super(Folder, self).check_access_rule(operation)