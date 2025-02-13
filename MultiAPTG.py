import numpy as np
import copy

def MultiAPTG(K, M, T0, sigma, epsilon, delta, feedbackMatrix, thresholds):
    feedbackMatrix_copy = copy.deepcopy(feedbackMatrix)
    #pull each arm once
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
            mediate[m] = bmmz[i][m] / thresholds[m]
        bmg[i] = np.max(mediate)

    #start the algorithm
    for t in range(K, T0):
        #algorithm
        mediate = np.zeros(K)
        for i in range(K):
            mediate[i] = np.sqrt(TiT[i]) * np.abs(bmg[i])
        hati = np.argmin(mediate)

        #receive and update
        for m in range(M):
            bmmz[hati][m] += feedbackMatrix_copy[t][hati][m]
        TiT[hati] += 1
        #only a little update
        mediate = np.zeros(M)
        for m in range(M):
            mediate[m] = bmmz[hati][m] / thresholds[m]
        bmg[hati] = np.max(mediate)

        #stopping criteria
        for i in range(K):
            if bmg[i] - np.sqrt(np.log(4 * K * np.power(TiT[i], 2) / delta) / (2 * TiT[i])) >= epsilon:
                return t, i
        flag = False
        for i in range(K):
            if bmg[i] + np.sqrt(np.log(4 * K * np.power(TiT[i], 2) / delta) / (2 * TiT[i])) >= epsilon:
                flag = True
                break
        #use -1 to indicate bottom
        if flag:
            return t, -1
    return T0, -1