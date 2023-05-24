import math
from square_equation_in_flask.models import QuadraticModel


class LesserThanZeroException(Exception):
    def __str__(self):
        return 'No solution'

    def __repr__(self):
        return 'No solution'


class QuadraticSolve:
    def __init__(self, quadratic_model: QuadraticModel):
        self.quadratic_model = quadratic_model

    def solving_quadrating(self):
        d = (self.quadratic_model.b ** 2) - (4 * self.quadratic_model.a * self.quadratic_model.c)
        if d > 0:
            x1 = (-self.quadratic_model.b - math.sqrt(d)) / (2 * self.quadratic_model.a)
            x2 = (-self.quadratic_model.b + math.sqrt(d)) / (2 * self.quadratic_model.a)
            return x1, x2
        elif d == 0:
            x = -self.quadratic_model.b / (2 * self.quadratic_model.a)
            return x
        else:
            raise LesserThanZeroException('No solution')
