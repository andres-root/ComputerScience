#!/usr/bin/python3

# App Modules
from .gates import Unit, AddGate, MultiplyGate


class Circuit(object):

    def __init__(self):
        self.mulg0 = MultiplyGate()
        self.mulg1 = MultiplyGate()
        self.addg0 = AddGate()
        self.addg1 = AddGate()

    def forward(self, a, b, c, x, y):
        self.ax = self.mulg0.forward(a, x)
        self.by = self.mulg1.forward(b, y)
        self.axpby = self.addg0.forward(self.ax, self.by)
        self.axpbypc = self.addg1.forward(self.axpby, c)
        return self.axpbypc

    def backward(self, gradient_top):
        self.axpbypc.grad = gradient_top
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
        pass
