# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields, api

class LibreriaCategoria(models.Model):
    _name = "libreria.categoria"
    name = fields.Char(string="Nombre",required=True,help="Introduce el nombre de la categoria")
    description = fields.Text(string="Descripción")
    prueba = fields.Text(string="Mi prueba")
    libros_ids = fields.One2many("libreria.libro","categoria_id",string="Libros")

class LibreriaLibro(models.Model):
    _name = "libreria.libro"
    name = fields.Char(string="Título",required=True,help="Introduce el título del libro")
    precio = fields.Float(string="Precio")
    ejemplares = fields.Integer(string="Ejemplares")
    fecha_compra = fields.Date(string="Fecha de compra")
    segmano = fields.Boolean(string="Segunda mano")
    estado = fields.Selection([('0','Bueno'),('1','Regular'),('2','Malo')],string="Estado",default="0")
    categoria_id = fields.Many2one("libreria.categoria",string="Categoría",required=True,ondelete="cascade")
    importetotal = fields.Float(string="Total", compute="_importetotal",store=True)

    @api.depends('precio','ejemplares')
    def _importetotal(self):
        for r in self:
            r.importetotal = r.precio * r.ejemplares
    

class LibreriaClientes(models.Model):
    _name = "libreria.cliente"
    _description = "Clientes de mi libreria"
    name = fields.Char(string="Nombre",required=True,help="Introduce el nombre del cliente.")
    activo = fields.Boolean(string="¿Esta activo?",default=True)
    country_id = fields.Many2one("res.country",string="Pais")
    libros_ids = fields.Many2many("libreria.libro",string = "Libros")
