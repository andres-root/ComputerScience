#!/usr/bin/python3


class Unit(object):

    def __init__(self, value, grad):
        self.value = value
        self.grad = grad


class MultiplyGate(object):

    def __init__(self, u0, u1):
        self.u0 = u0
        self.u1 = u1
        self.utop = Unit(u0 * u1, 0.0)

    def forward(self):
        return self.utop

    def backward(self):
        pass
