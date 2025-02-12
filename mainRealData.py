import numpy as np
from TrivialSolver import TrivialSolver
from MultiAPTG import MultiAPTG
from MultiHDoC import MultiHDoC
from MultiTUCB import MultiTUCB

M = 2
K = 7
bmmu_1 = [0.36, 0.34, 0.469, 0.465, 0.537, 0.537, 0.537]
bmmu_2 = [0.5, 0.7, 1.6, 1.8, 1.2, 1.0, 0.6]

thresholds = [0.5, 1.2]

sigma = 1.2
epsilon = 0.005
delta = 0.005
# hatmu[i][m] = feedbackMatrix[t][i][m]
T0 = 1000
feedbackMatrix = np.random.random(size = [T0, K, M])
###form the input matrix
input_matrix = [bmmu_1, bmmu_2]
# print(input_matrix)
if __name__ == '__main__':
    resultTrivialSolver = TrivialSolver(K, M, T0, sigma, epsilon, delta, feedbackMatrix, thresholds)
    resultAPTG = MultiAPTG(K, M, T0, sigma, epsilon, delta, feedbackMatrix, thresholds)
    resultHDoC = MultiHDoC(K, M, T0, sigma, epsilon, delta, feedbackMatrix, thresholds)
    resultOurs = MultiTUCB(K, M, T0, sigma, epsilon, delta, feedbackMatrix, thresholds)
