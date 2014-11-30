#!/usr/bin/python3

import math
from random import random

# Neuron 1
a1 = random() - 0.5
b1 = random() - 0.5
c1 = random() - 0.5

# Neuron 2
a2 = random() - 0.5
b2 = random() - 0.5
c2 = random() - 0.5

# Neuron 3
a3 = random() - 0.5
b3 = random() - 0.5
c3 = random() - 0.5

# Neuron 4
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
