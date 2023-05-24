from typing import Dict, List
from square_equation_in_flask.models import QuadraticModel


def dict_to_model(d: Dict) -> QuadraticModel:
    return QuadraticModel(
        a=d["a"],
        b=d["b"],
        c=d["c"],
    )


def dicts_to_models(list_of_dicts: List[Dict]) -> List[QuadraticModel]:
    return [dict_to_model(d) for d in list_of_dicts]
