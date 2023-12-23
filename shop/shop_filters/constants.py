"""
Constant
"""

ERRORS = {
    "INVALID_FILTER_MODULE": "Invalid filter module"
}


class FilterTypes:
    SINGLE_SEL = "single-select"
    FLOAT_RANGE = "float-range"


class OptionTypes:
    URL = "url"


FILTER_COMPS = {
    "shop-item": [
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
    ]
}
