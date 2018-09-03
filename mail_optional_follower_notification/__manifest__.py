# -*- coding: utf-8 -*-
# Copyright 2018 IT IS (<http://itis.de>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "Mail optional follower notification",

    'summary': """
        Choose if you want to automatically notify followers
        on mail.compose.message.
        Migrated module by IT IS AG from V10 to V11""",
    'author': 'Odoo Community Association (OCA), Acsone, IT IS AG',
    'website': "http://acsone.eu",
    'category': 'Social Network',
    'version': '11.0.1.0.1',
    'license': 'AGPL-3',
    'depends': [
        'mail',
    ],
    'data': [
        'wizard/mail_compose_message_view.xml',
    ],
}
