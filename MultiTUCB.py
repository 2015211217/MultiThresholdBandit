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
            mediate[m] = thresholds[m] - (bmmz[i][m] / TiT[i])
        bmg[i] = np.max(mediate)
    #start the main algorithm
    for t in range(K, T0):
        # algorithm
        mediate3 = np.zeros(K)
        for i in range(K):
            mediate3[i] = bmg[i] - np.sqrt((2 * np.power(sigma, 2) * np.log((np.power(np.pi, 2) * K * M * np.power(TiT[i], 2))
                                                                           / (3 * delta))) / TiT[i])
        hati = np.argmin(mediate3)
        # receive and update
        for m in range(M):
            bmmz[hati][m] += feedbackMatrix_copy[t][hati][m]
        TiT[hati] += 1
        # only a little update
        mediate2 = np.zeros(M)
        for m in range(M):
            mediate2[m] = thresholds[m] - (bmmz[hati][m] / TiT[hati])
        bmg[hati] = np.max(mediate2)

        # stopping criteria
        for i in range(K):
            if bmg[i] + np.sqrt((2 * np.power(sigma, 2) * np.log((np.power(np.pi, 2) * M * K * np.power(TiT[i], 2))
                                                                           /(3 * delta))) / TiT[i]) <= epsilon:
                return t, i
        flag = True
        for i in range(K):
            if bmg[i] <= np.sqrt((2 * np.power(sigma, 2) * np.log((np.power(np.pi, 2) * M * K * np.power(TiT[i], 2) )
                                                                           /(3 * delta))) / TiT[i]):
                flag = False
                break
        # use -1 to indicate bottom
        if flag:
            return t, -1
    return T0, -1