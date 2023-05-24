from typing import List, Union, Tuple
from flask import Flask, request
from math_controller import QuadraticSolve, LesserThanZeroException
from square_equation_in_flask.models_controller import dicts_to_models

app = Flask(__name__)


@app.route('/compute', methods=['POST'])
def api_compute() -> List[Union[float, Tuple[float, float]]]:
    result = []
    for obj in dicts_to_models(request.json):
        ms = QuadraticSolve(obj)
        try:
            result.append(ms.solving_quadrating())
        except LesserThanZeroException as err:
            result.append(str(err))

    return result


if __name__ == '__main__':
    app.run()
