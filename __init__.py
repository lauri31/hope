# SDG
from . import models



from odoo import api, SUPERUSER_ID

def _andika_init(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    # env.ref('stock.warehouse0').write({'manufacture_steps': 'pbm'})
    env.ref('product.product_category_all').write({
        'property_cost_method': 'fifo',
        'property_valuation': 'real_time',
        'removal_strategy_id': env.ref('stock.removal_fifo').id
    })