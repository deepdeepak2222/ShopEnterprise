"""
Constant
"""

ERRORS = {
    "INVALID_FILTER_MODULE": "Invalid filter module"
}


class FilterTypes:
    """
    If filter_type in [FLOAT_RANGE, INT_RANGE]:
        qp_key will be list of keys
            Example:
                [total_from, total_to]

    """
    SINGLE_SEL = "single-select"
    FLOAT_RANGE = "float-range"
    INT_RANGE = "int-range"
    SEARCH = "text-search"


class OptionTypes:
    URL = "url"
    STATIC_RANGE = "static-range"
