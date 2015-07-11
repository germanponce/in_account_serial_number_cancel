# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2015
#    All Rights Reserved.
#    info skype: german_442 email: (german.ponce@outlook.com)
############################################################################

{
    'name': 'Conservar Serie Cancelada Facturacion.',
    'version': '1',
    "author" : "German Ponce Dominguez",
    "category" : "Facturacion",
    'description': """

Este modulo modifica la Factura para mostrar si esta cancelada o no.
Este modulo tambien conserva el Consecutivo de las facturas canceladas.

    """,
    "website" : "http://integra.avalos.co",
    "license" : "AGPL-3",
    "depends" : ["account",],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
                    "report.xml",
                    ],
    "installable" : True,
    "active" : False,
}
