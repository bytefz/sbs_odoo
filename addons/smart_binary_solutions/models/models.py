# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields, api
from datetime import date

# date.today()

class ProductsIn(models.Model):
    _name = "products.sbs.db"  # Nombre en base de datos: products_sbs_db
    _description = "Productos de Smart Binary Solutions"
    _inherit = "mail.thread"  # Para que se pueda usar el método de seguimiento de Odoo

    # Valores del Cliente
    name_client = fields.Char(string="Razón Social", required=True)
    ruc_dni = fields.Char(string="RUC/DNI", required=True)
    contact = fields.Char(string="Contacto")
    address = fields.Char(string="Dirección", required=True)
    number_phone = fields.Char(string="Número de Teléfono")
    email = fields.Char(string="Correo Electrónico")

    # Etiqueta de Producto Activo
    tag = fields.Selection([
        ("Recibido", "Recibido"),
        ("Entregado", "Entregado"),
    ], string="Estado", default="Recibido")

    # Valores del Producto
    name = fields.Char(string="Modelo", required=True)
    brand = fields.Selection(
        [
            ('Acer', 'Acer'),
            ('Apple', 'Apple'),
            ('Asus', 'Asus'),
            ('Dell', 'Dell'),
            ('HP', 'HP'),
            ('Lenovo', 'Lenovo'),
            ('MSI', 'MSI'),
            ('Samsung', 'Samsung'),
            ('Sony', 'Sony'),
            ('Toshiba', 'Toshiba'),
            ('Epson', 'Epson'),
            ('Canon', 'Canon'),
            ('Wester Digital', 'Wester Digital'),
            ('Segeate', 'Segeate'),
            ('Philips', 'Philips'),
            ('AOC', 'AOC'),
            ('Varios', 'Varios'),
        ], string="Marca", required=True)
    serie = fields.Char(string="Serie", required=True)
    date = fields.Date(string="Fecha", required=True, default=lambda self: fields.datetime.now())
    producto_flaw = fields.Html(string="Fallas")
    observation = fields.Html(string="Observaciones")
    solution = fields.Html(string="Solución")
    
    # Referencias
    user_id = fields.Many2one(
        'res.users', string="Usuario", default=lambda self: self.env.user.id)
    category_id = fields.Many2one("sa.category", string="Categoría")


    def tag_entregado(self):
        if self.tag=="Recibido":
            self.tag = "Entregado"
            
        
        

    # def create_analytic(self,rec):
    #     dic = {
    #         "name": rec.name,
    #         "brand": rec.brand,
    #         "serie": rec.serie,
    #         "date": rec.date,
    #         "producto_flaw": rec.producto_flaw,
    #         "observation": rec.observation,
    #         "name_client": rec.name_client,
    #         "ruc_dni": rec.ruc_dni,
    #         "contact": rec.contact,
    #         "address": rec.address,
    #         "number_phone": rec.number_phone,
    #         "email": rec.email
    #     }
    #     self.env["products.sbs.db"].create(dic)

    #     @api.model
    #     def create(self, vals):
    #         rec = super(ProductOut, self).create(vals)
    #         self.create_analytic(rec)
    #         return rec


class Users(models.Model):
    _inherit = "res.users"

    products_id_user = fields.One2many("products.sbs.db", "user_id")

    def mi_cuenta(self):
        return{
            "type": "ir.actions.act_window",
            "name": "Mi Cuenta",
            "res_model": "res.users",
            "res_id": self.env.user.id,
            "target": "self",
            "views": [(False, "form")]
        }


class Category(models.Model):
    _name = "sa.category"
    _description = "Categoria"

    name = fields.Char("Nombre")
