import math
from random import random

a = 1
b = -2
c = -1
dataset = [{'data': (1.2, 0.7), 'label': 1},
           {'data': (-0.3, -0.5), 'label': -1},
           {'data': (3.0, 0.1), 'label': 1},
           {'data': (-0.1, -1.0), 'label': -1},
           {'data': (-1.0, 1.1), 'label': -1},
           {'data': (-1.0, 1.1), 'label': 1}]
for iter in range(1, 401):
    i = math.floor(random() * dataset.length)
    x = dataset[i]['data'][0]
    y = dataset[i]['data'][1]
    label = dataset[i]['label']

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
    print(score)
