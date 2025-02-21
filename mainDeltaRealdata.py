import numpy as np
from TrivialSolver import TrivialSolver
from MultiAPTG import MultiAPTG
from MultiHDoC import MultiHDoC
from MultiTUCB import MultiTUCB
from MultiAPE import MultiAPE
import copy

M = 2
K = 7
bmmu_1 = [0.36, 0.34, 0.469, 0.465, 0.537, 0.537, 0.537]
bmmu_2 = [0.5, 0.7, 1.6, 1.8, 1.2, 1.0, 0.6]

thresholds = [0.5, 1.2]
#for simplicity, we assume sigma is the same for every objective
sigma = 1.2
repetation = 1000
plotpoint = 10
epsilon = 0.005
delta = 0.005
# hatmu[i][m] = feedbackMatrix[t][i][m]
T0 = 100000
# 10 个数据点
GoodArmTrivialSolver = np.zeros((repetation, plotpoint))
GoodArmAPTG = np.zeros((repetation, plotpoint))
GoodArmHDoC = np.zeros((repetation, plotpoint))
GoodArmOurs = np.zeros((repetation, plotpoint))
GoodArmAPE = np.zeros((repetation, plotpoint))

deviationTrivialSolver = np.zeros(plotpoint)
deviationAPTG = np.zeros(plotpoint)
deviationHDoC = np.zeros(plotpoint)
deviationOurs = np.zeros(plotpoint)
deviationAPE = np.zeros(plotpoint)
stoppingtimeTrivialSolver = np.zeros((repetation, plotpoint))
stoppingtimeAPTG = np.zeros((repetation, plotpoint))
stoppingtimeHDoC = np.zeros((repetation, plotpoint))
stoppingtimeOurs = np.zeros((repetation, plotpoint))
stoppingtimeAPE = np.zeros((repetation, plotpoint))

feedbackMatrix = np.random.random(size=[T0, K, M])

#每个算法十个点， 横轴是delta，纵轴是
for DeltaMultipler in range(plotpoint):
    delta = 0.005 * (DeltaMultipler + 1)
    for round in range(repetation):
        ###form the input matrix
        input_matrix = [bmmu_1, bmmu_2]
    # print(input_matrix)
        feedbackMatrix_copy1 = copy.deepcopy(feedbackMatrix)
        feedbackMatrix_copy2 = copy.deepcopy(feedbackMatrix)
        feedbackMatrix_copy3 = copy.deepcopy(feedbackMatrix)
        feedbackMatrix_copy4 = copy.deepcopy(feedbackMatrix)
        feedbackMatrix_copy5 = copy.deepcopy(feedbackMatrix)

        stoppingtimeTrivialSolver[round][DeltaMultipler], GoodArmTrivialSolver[round][DeltaMultipler] = TrivialSolver(K, M, T0, sigma, epsilon, delta, feedbackMatrix_copy1, thresholds)
        stoppingtimeAPTG[round][DeltaMultipler], GoodArmAPTG[round][DeltaMultipler] = MultiAPTG(K, M, T0, sigma, epsilon, delta, feedbackMatrix_copy2, thresholds)
        stoppingtimeHDoC[round][DeltaMultipler], GoodArmHDoC[round][DeltaMultipler] = MultiHDoC(K, M, T0, sigma, epsilon, delta, feedbackMatrix_copy3, thresholds)
        stoppingtimeOurs[round][DeltaMultipler], GoodArmOurs[round][DeltaMultipler] = MultiTUCB(K, M, T0, sigma, epsilon, delta, feedbackMatrix_copy4, thresholds)
        stoppingtimeAPE[round][DeltaMultipler], GoodArmAPE[round][DeltaMultipler] = MultiAPE(K, M, T0, sigma, epsilon, delta, feedbackMatrix_copy5, thresholds)

        print('round', round, 'with delta',  delta, 'completed')
    #feedback is the round that first good arm is found

deviationTrivialSolver = np.max(stoppingtimeTrivialSolver, axis=0) - np.min(stoppingtimeTrivialSolver, axis=0)
deviationAPTG = np.max(stoppingtimeAPTG, axis=0) - np.min(stoppingtimeAPTG, axis=0)
deviationHDoC = np.max(stoppingtimeHDoC, axis=0) - np.min(stoppingtimeHDoC, axis=0)
deviationOurs = np.max(stoppingtimeOurs, axis=0) - np.min(stoppingtimeOurs, axis=0)
deviationAPE = np.max(stoppingtimeAPE, axis=0) - np.min(stoppingtimeAPE, axis=0)

#calculate the deviations
#check the presentation of deviation, should the upper bound and lower bound be the same number?
#计算错误率
print("Algorithm Finished")
np.savez('../GoodArmAuthenticData', GoodArmTrivialSolver, GoodArmAPTG, GoodArmHDoC, GoodArmOurs)

print(stoppingtimeTrivialSolver, GoodArmTrivialSolver)
print(stoppingtimeAPTG, GoodArmAPTG)
print(stoppingtimeHDoC, GoodArmHDoC)
print(stoppingtimeAPE, GoodArmAPE)
print(stoppingtimeOurs, GoodArmOurs)
print("Deviation part")
print(np.max(stoppingtimeTrivialSolver, axis=0), np.min(stoppingtimeTrivialSolver, axis=0))
print(np.max(stoppingtimeAPTG, axis=0), np.min(stoppingtimeAPTG, axis=0))
print(np.max(stoppingtimeHDoC, axis=0), np.min(stoppingtimeHDoC, axis=0))
print(np.max(stoppingtimeAPE, axis=0), np.min(stoppingtimeAPE, axis=0))
print(np.max(stoppingtimeOurs, axis=0), np.min(stoppingtimeOurs, axis=0))
