"""
Utils
"""
from shop_filters.shop_items_filter_options import get_shop_items_categories, get_shop_items_category_types

# Filter option functions
filter_option_functions = {
    "shop-item": {
        "category": get_shop_items_categories,
        "category-type": get_shop_items_category_types,
    }
}


def get_filter_options(**kwargs):
    """
    Get filter options
    params:
        module->str : Module
        key->str : Key
    """
    func = filter_option_functions.get(kwargs.get("module"), {}).get(kwargs.get("key"))
    if not func:
        return {}
    return func(**kwargs)
