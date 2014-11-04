#!/usr/bin/python3


def forward_multiply_gate(x, y):
    return x * y

x = -2
y = 3
out = forward_multiply_gate(x, y)
h = 0.001
xph = x + h
out1 = forward_multiply_gate(xph, y)
x_derivative = (out1 - out) / h

ypy = y + h
out2 = forward_multiply_gate(x, ypy)
y_derivative = (out2 - out) / h
