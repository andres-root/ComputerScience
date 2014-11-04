#!/usr/bin/python3


def forward_add_gate(a, b):
    return a + b


def forward_multiply_gate(a, b):
    return a * b


def forward_circuit(x, y, z):
    q = forward_add_gate(x, y)
    f = forward_multiply_gate(q, z)
    print(f)
    derivative_f_wrt_z = q
    derivative_f_wrt_q = z
    derivative_q_wrt_x = 1.0
    derivative_q_wrt_y = 1.0
    derivative_f_wrt_x = derivative_q_wrt_x * derivative_f_wrt_q
    derivative_f_wrt_y = derivative_q_wrt_y * derivative_f_wrt_q
    gradient_f_wrt_xyz = [derivative_f_wrt_x,
                          derivative_f_wrt_y,
                          derivative_f_wrt_z]
    step_size = 0.01
    x = x + step_size * gradient_f_wrt_xyz[0]
    y = y + step_size * gradient_f_wrt_xyz[1]
    z = z + step_size * gradient_f_wrt_xyz[2]
    q = forward_add_gate(x, y)
    f = forward_multiply_gate(q, z)
    return f

x = -2
y = 5
z = -4
f = forward_circuit(x, y, z)
print(f)
