"""
Constants
"""
SHOP_ITEM_TSV_SEARCH_Q = "select * from shop_inventory_shopitem where tsv @@ plainto_tsquery('%s') order by created " \
                         "desc "
