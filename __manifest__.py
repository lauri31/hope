{
    'name' : 'Andika',
    'version' : '1.0',
    'summary': 'Andika',
    'sequence': 10,
    'description': """
Andika
    """,
    'category': 'Project',
    'depends' : [
        'l10n_generic_coa',
        'stock',
        'purchase',
        'mrp',
        'sale_management',
        'account',
    ],
    'data': [
        'data/user.xml',
        'data/company.xml',
        'data/uom.xml',
        'views/partner.xml',
        'views/account.xml',
        'views/purchase.xml',
        'views/mrp.xml',
        'views/menu.xml',
    ],
    'demo': [
        # 'demo/account_demo.xml',
    ],
    'installable': True,
    # 'application': True,
    'post_init_hook': '_andika_init',
    'license': 'LGPL-3',
}
#SDG
