import numpy as np
import copy

def TrivialSolver(K, M, T0, sigma, epsilon, delta, feedbackMatrix, thresholds):
    feedbackMatrix_copy = copy.deepcopy(feedbackMatrix)
    hatmu = np.zeros((K, M))
    goodarmset = []
    TMediate = np.ceil((8 * np.power(sigma, 2) * np.log(M / delta)) / np.power(epsilon, 2))
    if TMediate < T0:
        T0 = TMediate
    t = 0
    for i in range(K):
        for t in range(int(T0)):
            # at here handle the update of hat bmmu
            for m in range(M):
                hatmu[i][m] += feedbackMatrix_copy[t][i][m]
        for m in range(M):
            hatmu[i][m] /= T0

        flag = True
        for m in range(M):
            if hatmu[i][m] < thresholds[m] - epsilon / 2:
                flag = False
        if flag:
            # goodarmset.append(i)
            return t, i
    return T0, -1


