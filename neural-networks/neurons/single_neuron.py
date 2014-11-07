#!/usr/bin/python3


from .components import Unit


class MultiplyGate(object):

    def __init__(self, u0, u1):
        self.u0 = u0
        self.u1 = u1
        self.utop = 0

    def forward(self):
        self.utop = Unit(self.u0.value * self.u1.gradient, 0.0)
        return self.utop

    def backward(self):
        self.u0.gradient += self.u1.value * self.utop.gradient
        self.u1.gradient += self.u0.value * self.utop.gradient


class AddGate(object):

    def __init__(self, u0, u1):
        self.u0 = u0
        self.u1 = u1
        self.utop = 0

    def forward(self):
        self.utop = Unit(self.u0.value + self.u1.gradient, 0.0)
        return self.utop

    def backward(self):
        self.u0.gradient += 1 * self.utop.gradient
        self.u1.gradient += 1 * self.utop.gradient
