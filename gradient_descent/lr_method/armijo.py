import numpy as np

from gradient_descent.lr_method import LRMethod
from gradient_descent.objective_function import ObjectiveFunction


class Armijo(LRMethod):
    """Armijo method for finding Learning Rate.

    This method successively reduces the learning rate until it finds the
    resulting change to be as good as a linear approximation of the function.
    """

    def __init__(
        self,
        initial_lr: float,
        tolerance: float,
        decrease_factor: float,
        max_iters: int = 10,
    ):
        self.initial_lr = initial_lr
        self.tolerance = tolerance
        self.decrease_factor = decrease_factor
        self.max_iters = max_iters

    def __call__(
        self,
        parameters: np.ndarray,
        function_value: float,
        gradient: np.ndarray,
        direction: np.ndarray,
        step: int,
        objective_function: ObjectiveFunction,
    ) -> float:
        lr = self.initial_lr
        while function_value - objective_function(
            parameters - lr * direction
        ) >= -self.tolerance * lr * np.dot(gradient, direction):
            lr *= self.decrease_factor
        return lr
