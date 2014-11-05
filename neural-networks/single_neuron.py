#!/usr/bin/python3


class Unit(object):

    def __init__(self, value, grad):
        self.value = value
        self.grad = grad

    def get(self):
        return self


class MultiplyGate(object):

    def __init__(self, u0, u1):
        self.u0 = u0
        self.u1 = u1
        self.utop = Unit(u0.value * u1.grad, 0.0)

    def forward(self):
        return self.utop

    def backward(self):
        self.u0.grad += self.u1.value * self.utop.grad
        self.u1.grad += self.u0.value * self.utop.grad
