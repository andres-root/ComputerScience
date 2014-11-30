#!/usr/bin/python3

import math
from random import random

a1 = random() - 0.5
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
