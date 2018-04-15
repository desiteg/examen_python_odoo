# -*- coding: utf-8 -*-

import base64

from odoo import models, fields, api
from odoo import tools, _

class TipoEquipos(models.Model):
    _name = 'tipo.equipos'
    _rec_name = 'tipo_equipo'

    tipo_equipo = fields.Char(string='Tipo Equipos', size=50)

class SistemasOperativos(models.Model):
    _name = 'sistemas.operativos'
    _rec_name = 'nombre_sistema'

    nombre_sistema = fields.Char(string='Nombre Sistema', size=50)
    version  = fields.Char(string='Version', size=50)

class EquiposComputo(models.Model):
    _name = 'equipos.computo'
    _rec_name = 'nombre_equipo'
    _description = 'Equipos de Computo'

    nombre_equipo = fields.Char(string='Nombre Equipo',size=50)
    marca = fields.Char(string='Marca',size=50)
    tipo_equipo_id = fields.Many2one('tipo.equipos', string='Tipo de Equipo')
    sistema_operativo_id = fields.Many2one('sistemas.operativos', string='Sistema Operativo')
    memoria_ram = fields.Char(string='Memoria RAM',size=50)
    capacidad_disco_duro = fields.Char(string='Capacidad de Disco Duro',size=50)
    numero_de_serie = fields.Char(string='Numero de Serie',size=50)
    usuario_asignado_id = fields.Many2one('res.users', string='Usuario Asignado')
    image = fields.Binary(string='Imagen')

class ResUsers(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    numero_empleado = fields.Char(string='Numero Empleado', size=50)
    fecha_ingreso = fields.Char(string='Fecha de Ingreso', size=50)
    numero_imss = fields.Char(string='Numero IMSS', size=50)
    equipos_asignados_id = fields.One2many('equipos.computo', 'usuario_asignado_id', string='Equipos Asignados')
    numero_equipos_asignados = fields.Integer(string='Numero de Equipos Asignados', compute='_compute_device')
    
    @api.one
    def _compute_device(self):  
        count = self.env['equipos.computo'].search_count([('usuario_asignado_id','=',self.id)])
        self.numero_equipos_asignados = count

    @api.model
    def create(self, vals):
        if vals.get('name'):
            if 'name' in vals:
                vals['numero_empleado'] = self.env['ir.sequence'].next_by_code('res.users') or _('New')

        result = super(ResUsers, self).create(vals)
        return result

    

    
