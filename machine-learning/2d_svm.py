#!/usr/bin/python3


def cost(X, y, w, alpha):
    total_cost = 0  # L in the SVM function
    N = len(X)
    # Computing score
    for i in range(N):
        xi = X[i]
        score = w[0] * xi[0] + w[1] * xi[1] + w[2]
        # accumulate cost based on how compatible the score is with the label
        yi = y[i]  # label
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
    X = [[1.2, 0.7], [-0.3, 0.5], [3, 2.5]]  # 2-dimensional data
    y = [1, -1, 1]  # Labels
    w = [0.1, 0.2, 0.3]  # Random numbers
    alpha = 0.1  # Regularization strenght
    print(cost(X, y, w, alpha))
