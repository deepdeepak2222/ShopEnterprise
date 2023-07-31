"""
Enum classes used for shop inventory
"""


class PriceType:
    """
    Any type of shop items can be sold by any of these measures:
        per kg
        per litre
        per items
    """
    L = "L"  # Litre
    KG = "KG"  # Kilogram
    QUANT = "QUANT"  # Quantity
