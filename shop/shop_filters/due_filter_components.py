from shop_filters.constants import FilterTypes, OptionTypes, SEARCH_COMPONENT
from shop_filters.due_filter_options import get_total_due_range


def get_due_filter_components():
    """
    Get filter components for due module
    """
    comps = [{
            "label": "Total Due Range",  # This is what the filter will appear as in UI
            "qp_key": ["total_money__gte", "total_money__lte"],  # Query parameter keys
            "filter_type": FilterTypes.INT_RANGE,
            "get_options": OptionTypes.STATIC_RANGE,
            "options": get_total_due_range(),
        }, SEARCH_COMPONENT]
    return comps
