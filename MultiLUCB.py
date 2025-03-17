import numpy as np
import copy
import sys

def MultiLUCB(K, M, T0, sigma, epsilon, delta, feedbackMatrix, thresholds):
    feedbackMatrix_copy = copy.deepcopy(feedbackMatrix)
    # pull each arm once
    bmmz = np.zeros((K, M))
    bmg = np.zeros(K)
    TiT = np.zeros(K)
    for t in range(K):
        for m in range(M):
            bmmz[t][m] += feedbackMatrix_copy[t][t][m]
        TiT[t] += 1
    #calculate the estimator
    # bmmz[i][m] / thresholds[m]
    for i in range(K):
        mediate = np.zeros(M)
        for m in range(M):
            mediate[m] = thresholds[m] - (bmmz[i][m] / TiT[i])
        bmg[i] = np.max(mediate)

    # start the algorithm
    for t in range(K, T0):
        # algorithm
        mediate3 = np.ones(K) * sys.maxsize
        for i in range(K):
            if bmg[i] != int(100):
                mediate3[i] = bmg[i] - np.sqrt((2 * np.power(sigma, 2) * np.log((4 * K * M * np.power(TiT[i], 2)))/delta) / (2 * TiT[i]))
            # mediate3 = bmg[i] - np.sqrt((np.power(sigma, 2) * np.log(K * (4 + TiT[i] * TiT[i]))) / TiT[i])
        hati = np.argmin(mediate3)

        # receive and update
        for m in range(M):
            bmmz[hati][m] += feedbackMatrix_copy[t][hati][m]
        TiT[hati] += 1
        # update hatbmg for hati
        mediate2 = np.zeros(M)
        for m in range(M):
            mediate2[m] = thresholds[m] - (bmmz[hati][m] / TiT[hati])
        bmg[hati] = np.max(mediate2)

        # stopping criteria
        if bmg[hati] > np.sqrt((2 * np.power(sigma, 2) * np.log((np.power(np.pi, 2) * M * K * np.power(TiT[hati], 2))
                                                                / (3 * delta))) / TiT[hati]):
            bmg[hati] = int(100)

        if bmg[hati] + np.sqrt((2 * np.power(sigma, 2) * np.log((np.power(np.pi, 2) * M * K * np.power(TiT[hati], 2))
                                                                           / (3 * delta))) / TiT[hati]) <= epsilon:
            return t, hati
        flag = True
        for i in range(K):
            if bmg[i] < int(100):
                flag = False
                break
        # use -1 to indicate bottom
        if flag:
            return t, -1
    return T0, -1