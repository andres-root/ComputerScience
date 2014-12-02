#!/usr/bin/python3


def cost(X, y, w, alpha):
    total_cost = 0
    N = len(X)
    for i in range(N):
        xi = X[i]
        score = w[0] * xi[0] + w[1] * xi[1] + w[2]

        yi = y[i]
        costi = max(0, -yi * score + 1)
        print('example {0} : xi = ( {1} ) and label = {2}'.format(i, xi, yi))
        print('  score computed to be {0:.3f}'.format(score))
        print('  => cost computed to be {0:.3f}'.format(costi))
        total_cost += costi

    # Regularizing cost: we want small weights
    reg_cost = alpha * (w[0] ** 2 + w[1] ** 2)
    print('regularization cost for current model is {0:.3f}'.format(reg_cost))
    total_cost += reg_cost

    print('Total cost is: {0:.3f}'.format(total_cost))
    return total_cost


if __name__ == '__main__':
    X = [[1.2, 0.7], [-0.3, 0.5], [3, 2.5]]
    y = [1, -1, 1]
    w = [0.1, 0.2, 0.3]
    alpha = 0.1
    print(cost(X, y, w, alpha))
