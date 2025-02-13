import numpy as np
import copy

def MultiTUCB(K, M, T0, sigma, epsilon, delta, feedbackMatrix, thresholds):
    feedbackMatrix_copy = copy.deepcopy(feedbackMatrix)
    # pull each arm once
    bmmz = np.zeros((K, M))
    bmg = np.zeros(K)
    TiT = np.zeros(K)
    for t in range(K):
        for m in range(M):
            bmmz[t][m] += feedbackMatrix_copy[t][t][m]
            TiT[t] += 1
    # calculate the estimator
    for i in range(K):
        mediate = np.zeros(M)
        for m in range(M):
            mediate[m] = bmmz[i][m] / thresholds[m]
        bmg[i] = np.max(mediate)

    for t in range(K, T0):
        # algorithm
        hati = np.argmin(bmg[i] - np.sqrt( 2 * np.power(sigma, 2) * np.log((np.power(np.pi, 2) * K * M * np.power(TiT[i], 2) )
                                                                           / (3 * delta)) / TiT[i])  for i in range(K))
        # receive and update
        for m in range(M):
            bmmz[hati][m] += feedbackMatrix_copy[t][hati][m]
        TiT[hati] += 1
        # only a little update
        mediate = np.zeros(M)
        for m in range(M):
            mediate[m] = bmmz[hati][m] / thresholds[m]
        bmg[hati] = np.max(mediate)

        # stopping criteria
        for i in range(K):
            if bmg[i] + bmg[i] - np.sqrt( 2 * np.power(sigma, 2) * np.log((np.power(np.pi, 2) * K * M * np.power(TiT[i], 2) )
                                                                           / (3 * delta)) / TiT[i]) <= epsilon:
                return t, i
        flag = False
        for i in range(K):
            if bmg[i] > bmg[i] + bmg[i] - np.sqrt( 2 * np.power(sigma, 2) * np.log((np.power(np.pi, 2) * K * M * np.power(TiT[i], 2) )
                                                                           / (3 * delta)) / TiT[i]) <= epsilon:
                flag = True
                break
        # use -1 to indicate bottom
        if flag:
            return t, -1
    return T0, -1