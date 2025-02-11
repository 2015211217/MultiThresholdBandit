import numpy as np
import copy

def MultiAPTG(K, M, T0, sigma, epsilon, delta, feedbackMatrix, thresholds):
    feedbackMatrix_copy = copy.deepcopy(feedbackMatrix)
    #pull each arm once
    bmmu = np.zeros((K, M))
    bmg = np.zeros(K)
    TiT = np.zeros(K)
    for t in range(K):
        for m in range(M):
            bmmu[t][m] += feedbackMatrix_copy[t][t][m]
            TiT[t] += 1
    #calculate the estimator
    
    for t in range(K, T0):
        #algorithm
        hati = np.argmax()

        #receive and update

        #stopping criteria
        for i in range(K):
            if bmg[i] - np.sqrt(np.log(4 * K * np.power(TiT[i], 2) / delta) / ( 2 * TiT[i])) >= epsilon:
                return i
        flag = False
        for i in range(K):
            if bmg[i] + np.sqrt(np.log(4 * K * np.power(TiT[i], 2) / delta) / ( 2 * TiT[i])) >= epsilon:
                flag = True
                break
        #use -1 to indicate bottom
        if flag:
            return -1