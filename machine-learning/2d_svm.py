#!/usr/bin/python3


def cost(X, y, w):
    total_cost = 0
    N = len(X)
    for i in range(N):
        xi = X[i]
        score = w[0] * xi[0] + w[1] * xi[1] + w[2]

        yi = y[i]
        costi = max(0, -yi * score + 1)


if __name__ == '__main__':
    X = [[1.2, 0.7], [-0.3, 0.5], [3, 2.5]]
    y = [1, -1, 1]
    w = [0.1, 0.2, 0.3]
    alpha = 0.1
    print(cost())
