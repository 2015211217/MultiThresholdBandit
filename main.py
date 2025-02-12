import numpy as np
from TrivialSolver import TrivialSolver
from MultiAPTG import MultiAPTG
from MultiHDoC import MultiHDoC
from MultiTUCB import MultiTUCB

M = 4
K = 10
repetation = 1000
bmmu_1 = [0.1, 0.1, 0.1, 0.35, 0.45, 0.55, 0.65, 0.2, 0.2, 0.2]
bmmu_2 = [0.2, round(0.4 - np.power(0.2, 2), 6), round(0.4 - np.power(0.2, 3), 6),round(0.4 - np.power(0.2, 4), 6)
    , 0.45, 0.55, round(0.6 + np.power(0.1, 5), 6), round(0.6 + np.power(0.1, 4), 6), 0.6 + round(np.power(0.1, 3), 6), round(0.6 + np.power(0.1, 2), 6), round(0.6 + np.power(0.1, 1), 6)]
bmmu_3 = [0.05, 0.1, 0.15, 0.2, 0.45, 0.55, 0.65, 0.7, 0.75, 0.8]
bmmu_4 = [0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6]

thresholds = [0.5, 0.7, 0.6, 0.5]
plotpoint = 10
sigma = np.random.rand()
epsilon = 0.005
delta = 0.005
# hatmu[i][m] = feedbackMatrix[t][i][m]
T0 = 100000
# 10 个数据点
resultTrivialSolver = np.zeros((repetation, plotpoint))
resultAPTG = np.zeros((repetation, plotpoint))
resultHDoC = np.zeros((repetation, plotpoint))
resultOurs = np.zeros((repetation, plotpoint))

#每个算法十个点， 横轴是delta，纵轴是
for DeltaMultipler in range(plotpoint):
    for round in range(repetation):
        feedbackMatrix = np.random.random(size = [T0, K, M])
        ###form the input matrix
        delta *= (DeltaMultipler + 1)
        input_matrix = [bmmu_1, bmmu_2, bmmu_3, bmmu_4]
    # print(input_matrix)
        if __name__ == '__main__':
            resultTrivialSolver[round][repetation] = TrivialSolver(K, M, T0, sigma, epsilon, delta, feedbackMatrix, thresholds)
            resultAPTG[round][repetation] = MultiAPTG(K, M, T0, sigma, epsilon, delta, feedbackMatrix, thresholds)
            resultHDoC[round][repetation] = MultiHDoC(K, M, T0, sigma, epsilon, delta, feedbackMatrix, thresholds)
            resultOurs[round][repetation] = MultiTUCB(K, M, T0, sigma, epsilon, delta, feedbackMatrix, thresholds)

#calculate the deviations
#check the presentation of deviation, should the upper bound and lower bound be the same number?
deviationTrivialSolver = np.zeros(plotpoint)
deviationAPTG = np.zeros(plotpoint)