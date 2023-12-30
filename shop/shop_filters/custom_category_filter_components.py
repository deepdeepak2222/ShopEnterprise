from shop_filters.constants import FilterTypes, OptionTypes, SEARCH_COMPONENT


def get_custom_category_filter_components():
    """
    Get filter components for custom category module
    """
    comps = [{
        "label": "Category Types",  # This is what the filter will appear as in UI
        "qp_key": "category_type",  # Query parameter key
        "filter_type": FilterTypes.SINGLE_SEL,
        "get_options": OptionTypes.URL,
        "options": "/filters/custom-category/category-type/",
    }, SEARCH_COMPONENT]
    return comps
