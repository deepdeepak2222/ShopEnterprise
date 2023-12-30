from shop_filters.constants import FilterTypes, OptionTypes, SEARCH_COMPONENT
from shop_filters.shop_items_filter_options import get_shop_item_total_range, get_shop_item_price_range


def get_shop_items_filter_components():
    """
    Get filter components for shop-item module
    """
    return [
        {
            "label": "Categories",  # This is what the filter will appear as in UI
            "qp_key": "category",  # Query parameter key
            "filter_type": FilterTypes.SINGLE_SEL,
            "get_options": OptionTypes.URL,
            "options": "/filters/shop-item/category/",
        },
        {
            "label": "Category Types",  # This is what the filter will appear as in UI
            "qp_key": "category_type",  # Query parameter key
            "filter_type": FilterTypes.SINGLE_SEL,
            "get_options": OptionTypes.URL,
            "options": "/filters/shop-item/category-type/",
        },
        {
            "label": "Total Range",  # This is what the filter will appear as in UI
            "qp_key": ["total_from", "total_to"],  # Query parameter keys
            "filter_type": FilterTypes.INT_RANGE,
            "get_options": OptionTypes.STATIC_RANGE,
            "options": get_shop_item_total_range(),
        },
        {
            "label": "Price Range",  # This is what the filter will appear as in UI
            "qp_key": ["price_from", "price_to"],  # Query parameter keys
            "filter_type": FilterTypes.INT_RANGE,
            "get_options": OptionTypes.STATIC_RANGE,
            "options": get_shop_item_price_range(),
        },
        SEARCH_COMPONENT
    ]
