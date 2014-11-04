#!/usr/bin/python3


def forward_add_gate(a, b):
    return a + b


def forward_multiply_gate(a, b):
    return a * b


def forward_circuit(x, y, z):
    q = forward_add_gate(x, y)
    f = forward_multiply_gate(q, z)
    return f

x = -1
y = 5
z = -4
f = forward_circuit(x, y, z)
print(f)
