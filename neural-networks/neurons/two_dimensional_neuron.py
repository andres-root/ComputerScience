#!/usr/bin/python3

import math


class Unit(object):

    def __init__(self, value, gradient):
        self.value = value
        self.gradient = gradient


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


class SigmoidGate(object):

    def __init__(self, u0):
        self.u0 = u0
        self.utop = 0
        self.sigmoid = 0

    def sigmoid(self, x):
        """
        Computes the sigmoid function wrt x.
        Reference: http://en.wikipedia.org/wiki/Sigmoid_function
        """
        self.sigmoid = 1 / (1 + math.exp(-x))

    def forward(self):
        self.utop = Unit(self.sigmoid(self.u0.value), 0.0)

    def backward(self):
        """
        Computes the local derivative with respect to its input,
        then multiplies on the gradient from the unit above.
        """
        sig = self.sigmoid(self.u0.value)
        self.u0.gradient += (sig * (1 - sig)) * self.utop.gradient


class ForwardNeuron(object):

    def __init__(self, *args, **kwargs):
        self.values = kwargs
        self.ax =
        self.by =


a = Unit(1.0, 0.0)
b = Unit(2.0, 0.0)
c = Unit(-3.0, 0.0)
x = Unit(-1.0, 0.0)
y = Unit(3.0, 0.0)
