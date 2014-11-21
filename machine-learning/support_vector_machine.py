#!/usr/bin/python3

# App Modules
from .gates import Unit, AddGate, MultiplyGate


class Circuit(object):

    def __init__(self):
        self.mulg0 = MultiplyGate()
        self.mulg1 = MultiplyGate()
        self.addg0 = AddGate()
        self.addg1 = AddGate()

    def forward(self, x, y, a, b, c):
        self.ax = self.mulg0.forward(a, x)
        self.by = self.mulg1.forward(b, y)
        self.axpby = self.addg0.forward(self.ax, self.by)
        self.axpbypc = self.addg1.forward(self.axpby, c)
        return self.axpbypc

    def backward(self, gradient_top):
        self.axpbypc.gradient = gradient_top
        self.addg1.backward()
        self.addg0.backward()
        self.mulg1.backward()
        self.mulg0.backward()


class Svm(object):
    """Support Vector Machine
    """

    def __init__(self):
        self.a = Unit(1.0, 0.0)
        self.b = Unit(-2.0, 0.0)
        self.c = Unit(-1.0, 0.0)
        self.circuit = Circuit()

    def forward(self, x, y):
        self.unit_out = self.circuit.forward(x, y, self.a, self.b, self.c)
        return self.unit_out

    def backward(self, label):
        self.a.gradient = 0.0
        self.b.gradient = 0.0
        self.c.gradient = 0.0
        pull = 0.0
        if label == 1 and self.unit_out.value < 1:
            pull = 1
        elif label == -1 and self.unit_out.value > -1:
            pull = -1
        self.circuit.backward(pull)

        # Making regularization
        self.a.gradient += -self.a.value
        self.b.gradient += -self.b.value

    def lean_from(self, x, y, label):
        self.forward(x, y)
        self.backward(label)
        self.parameter_update()

    def parameter_update(self):
        step_size = 0.01
        self.a.value += step_size * self.a.gradient
        self.b.value += step_size * self.b.gradient
        self.c.value += step_size * self.c.gradient


if __name__ == '__main__':
    data = [(1.2, 0.7),
            (-0.3, -0.5),
            (3.0, 0.1),
            (-0.1, -1.0),
            (-1.0, 1.1),
            (-1.0, 1.1)]
