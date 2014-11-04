#!/usr/bin/python3


def forward_multiply_gate(x, y):
    return x * y


def get_derivative(new_out, out, h):
    return (new_out - out) / h


x = -2
y = 3
h = 0.001
out = forward_multiply_gate(x, y)
xph = x + h
out1 = forward_multiply_gate(xph, y)
x_derivative = get_derivative(out1, out, h)

ypy = y + h
out2 = forward_multiply_gate(x, ypy)
y_derivative = get_derivative(out2, out, h)
