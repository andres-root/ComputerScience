#!/usr/bin/python3


def forward_multiply_gate(x, y):
    return x * y


def get_derivative(new_out, out, h):
    return (new_out - out) / h


x = -2
y = 3
out = forward_multiply_gate()
x_gradient = y
y_gradient = x

step_size = 0.01
x += step_size * x_gradient
y += step_size * y_gradient
new_out = forward_multiply_gate(x, y)
