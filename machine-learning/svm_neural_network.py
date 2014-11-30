#!/usr/bin/python3

import math
from random import random

# Neuron 1 values
a1 = random() - 0.5
b1 = random() - 0.5
c1 = random() - 0.5

# Neuron 2 values
a2 = random() - 0.5
b2 = random() - 0.5
c2 = random() - 0.5

# Neuron 3 values
a3 = random() - 0.5
b3 = random() - 0.5
c3 = random() - 0.5

# Neuron 4 values
a4 = random() - 0.5
b4 = random() - 0.5
c4 = random() - 0.5
d4 = random() - 0.5

dataset = [{'data': (1.2, 0.7), 'label': 1},
           {'data': (-0.3, -0.5), 'label': -1},
           {'data': (3.0, 0.1), 'label': 1},
           {'data': (-0.1, -1.0), 'label': -1},
           {'data': (-1.0, 1.1), 'label': -1},
           {'data': (-1.0, 1.1), 'label': 1}]
for iteration in range(0, 400):
    i = math.floor(random() * len(dataset))
    x = dataset[i]['data'][0]
    y = dataset[i]['data'][1]
    label = dataset[i]['label']

    n1 = max(0, a1 * x + b1 * y + c1)
    n2 = max(0, a2 * x + b2 * y + c2)
    n3 = max(0, a3 * x + b3 * y + c3)
    score = a4 * n1 + b4 * n2 + c4 * n3 + d4

    pull = 0.0
    if label == 1 and score < 1:
        pull = 1
    if label == -1 and score > -1:
        pull = -1

    # now compute backward pass to all parameters of the model
    # backprop through the last "score" neuron
    dscore = pull
    da4 = n1 * dscore
    dn1 = a4 * dscore
    db4 = n2 * dscore
    dn2 = b4 * dscore
    dc4 = n3 * dscore
    dn3 = c4 * dscore
    dd4 = 1.0 * dscore

    # backprop the ReLU non-linearities, in place
    # i.e. just set gradients to zero if the neurons did not "fire"
    dn3 = 0 if n3 == 0 else dn3
    dn2 = 0 if n2 == 0 else dn2
    dn1 = 0 if n1 == 0 else dn1

    # backprop to parameters of neuron 1
    da1 = x * dn1
    db1 = y * dn1
    dc1 = 1.0 * dn1

    # backprop to parameters of neuron 2
    da2 = x * dn2
    db2 = y * dn2
    dc2 = 1.0 * dn2

    # backprop to parameters of neuron 3
    da3 = x * dn3
    db3 = y * dn3
    dc3 = 1.0 * dn3

    # phew! End of backprop!

    # add the pulls from the regularization, tugging all multiplicative
    # parameters (i.e. not the biases) downward, proportional to their value
    da1 += -a1
    da2 += -a2
    da3 += -a3
    db1 += -b1
    db2 += -b2
    db3 += -b3
    da4 += -a4
    db4 += -b4
    dc4 += -c4

    # finally, do the parameter update
    step_size = 0.01
    a1 += step_size * da1
    b1 += step_size * db1
    c1 += step_size * dc1
    a2 += step_size * da2
    b2 += step_size * db2
    c2 += step_size * dc2
    a3 += step_size * da3
    b3 += step_size * db3
    c3 += step_size * dc3
    a4 += step_size * da4
    b4 += step_size * db4
    c4 += step_size * dc4
    d4 += step_size * dd4










