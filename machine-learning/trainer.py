#!/usr/bin/python3

import math
from random import random

a = 1
b = -2
c = -1
for iter in range(0, 400):
    i = math.floor(random() * data.length)
    x = data[i][0]
    y = data[i][1]
    label = labels[i]

    score = a*x + b*y + c
    pull = 0.0
    if label == 1 and score < 1:
        pull = 1
    if label == -1 and score > -1:
        pull = -1

    step_size = 0.01
    a += step_size * (x * pull - a)
    b += step_size * (y * pull - b)
    c += step_size * (1 * pull)
