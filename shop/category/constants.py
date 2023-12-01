"""
Constants for category app
"""


class CategoryType:
    PER_PIECE = "PER_PIECE"
    PER_KG = "PER_KG"
    PER_LTR = "PER_LTR"

    CAT_LABELS = [
        {
            "id": PER_PIECE,
            "label": "Per Piece",
        },
        {
            "id": PER_KG,
            "label": "Per Kilogram",
        },
        {
            "id": PER_LTR,
            "label": "Per Litre",
        }
    ]
