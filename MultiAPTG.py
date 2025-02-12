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
    for i in range(K):
        bmg[i] = np.max(bmmz[i][m] / thresholds[m] for m in range(M))

    #start the algorithm
    for t in range(K, T0):
        #algorithm
        hati = np.argmin(np.sqrt(TiT[i]) * np.abs(bmg[i]) for i in range(K))

        #receive and update
        for m in range(M):
            bmmz[hati][m] += feedbackMatrix_copy[t][hati][m]
        TiT[hati] += 1
        #only a little update
        bmg[hati] = np.max(bmmz[hati][m] / thresholds[m] for m in range(M))

        #stopping criteria
        for i in range(K):
            if bmg[i] - np.sqrt(np.log(4 * K * np.power(TiT[i], 2) / delta) / (2 * TiT[i])) >= epsilon:
                return i
        flag = False
        for i in range(K):
            if bmg[i] + np.sqrt(np.log(4 * K * np.power(TiT[i], 2) / delta) / (2 * TiT[i])) >= epsilon:
                flag = True
                break
        #use -1 to indicate bottom
        if flag:
            return -1