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

    def __init__(self, mulg0, mulg1, addg0, addg1, sigg0):
        self.mulg0 = mulg0
        self.mulg1 = mulg1
        self.addg0 = addg0
        self.addg1 = addg1
        self.sigg0 = sigg0
        self.ax = 0
        self.by = 0
        self.axpby = 0
        self.axpbypc = 0
        self.sig = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.x = 0
        self.y = 0

    def forward(self, a, b, c, x, y):
        self.a = a
        self.b = b
        self.c = c
        self.x = x
        self.y = y
        self.ax = self.mulg0.forward(a, x)
        self.by = self.mulg1.forward(b, y)
        self.axpby = self.addg0.forward(self.ax, self.by)
        self.axpbypc = self.addg1.forward(self.axpby, c)
        self.sig = self.sigg0.forward(self.axpbypc)
        return self.sig

    def backward(self, gradient=1.0, step_size=0.01):
        """
        Gradient
        """
        self.sig.gradient = gradient
        self.sigg0.backward()
        self.addg1.backward()
        self.addg0.backward()
        self.mulg1.backward()
        self.mulg0.backward()
        self.a.value += step_size * self.a.grad
        self.b.value += step_size * self.b.grad
        self.c.value += step_size * self.c.grad
        self.x.value += step_size * self.x.grad
        self.y.value += step_size * self.y.grad


def ComputeForward():
    a = Unit(1.0, 0.0)
    b = Unit(2.0, 0.0)
    c = Unit(-3.0, 0.0)
    x = Unit(-1.0, 0.0)
    y = Unit(3.0, 0.0)
    mulg0 = MultiplyGate()
    mulg1 = MultiplyGate()
    addg0 = AddGate()
    addg1 = AddGate()
    sigg0 = SigmoidGate()
    neuron = ForwardNeuron(mulg0, mulg1, addg0, addg1, sigg0)
    neuron.forward(a, b, c, x, y)
    response = 'Circuit output: {0}'.format(neuron.sig.value)
    return response


if __name__ == '__main__':
    computed_sigmoid_value = ComputeForward()
    print(computed_sigmoid_value)
