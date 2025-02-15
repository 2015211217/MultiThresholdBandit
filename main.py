import numpy as np
from TrivialSolver import TrivialSolver
from MultiAPTG import MultiAPTG
from MultiHDoC import MultiHDoC
from MultiTUCB import MultiTUCB
from MultiLUCB import MultiLUCB
import copy
M = 4
K = 10

# -1 tester
bmmu_1 = [0.1, 0.1, 0.1, 0.35, 0.45, 0.55, 0.65, 0.2, 0.2, 0.2]
bmmu_2 = [0.2, round(0.4 - np.power(0.2, 2), 6), round(0.4 - np.power(0.2, 3), 6),round(0.4 - np.power(0.2, 4), 6)
    , 0.45, 0.55, round(0.6 + np.power(0.1, 4), 6), 0.6 + round(np.power(0.1, 3), 6), round(0.6 + np.power(0.1, 2), 6), round(0.6 + np.power(0.1, 1), 6)]
bmmu_3 = [0.05, 0.1, 0.15, 0.2, 0.45, 0.55, 0.65, 0.7, 0.75, 0.8]
bmmu_4 = [0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6]

thresholds = [0.5, 0.7, 0.6, 0.5]
plotpoint = 10
repetation = 1
#注意修改
sigma = 1
epsilon = 0.005
# hatmu[i][m] = feedbackMatrix[t][i][m]
T0 = 10000
# 10 个数据点

GoodArmTrivialSolver = np.zeros((repetation, plotpoint))
GoodArmAPTG = np.zeros((repetation, plotpoint))
GoodArmHDoC = np.zeros((repetation, plotpoint))
GoodArmOurs = np.zeros((repetation, plotpoint))
GoodArmLUCB = np.zeros((repetation, plotpoint))

deviationTrivialSolver = np.zeros(plotpoint)
deviationAPTG = np.zeros(plotpoint)
deviationHDoC = np.zeros(plotpoint)
deviationOurs = np.zeros(plotpoint)
deviationLUCB = np.zeros(plotpoint)
stoppingtimeTrivialSolver = np.zeros((repetation, plotpoint))
stoppingtimeAPTG = np.zeros((repetation, plotpoint))
stoppingtimeHDoC = np.zeros((repetation, plotpoint))
stoppingtimeOurs = np.zeros((repetation, plotpoint))
stoppingtimeLUCB = np.zeros((repetation, plotpoint))

feedbackMatrix = np.random.random(size=[T0, K, M])

#每个算法十个点， 横轴是delta，纵轴是
for DeltaMultipler in range(plotpoint):
    delta = 0.005 * (DeltaMultipler + 1)
    for round in range(repetation):
        ###form the input matrix
        input_matrix = [bmmu_1, bmmu_2, bmmu_3, bmmu_4]
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
        stoppingtimeLUCB[round][DeltaMultipler], GoodArmLUCB[round][DeltaMultipler] = MultiLUCB(K, M, T0, sigma, epsilon, delta, feedbackMatrix_copy5, thresholds)

        print('round', round, 'with delta',  delta, 'completed')
    #feedback is the round that first good arm is found

deviationTrivialSolver = np.max(stoppingtimeTrivialSolver, axis=0) - np.min(stoppingtimeTrivialSolver, axis=0)
deviationAPTG = np.max(stoppingtimeAPTG, axis=0) - np.min(stoppingtimeAPTG, axis=0)
deviationHDoC = np.max(stoppingtimeHDoC, axis=0) - np.min(stoppingtimeHDoC, axis=0)
deviationOurs = np.max(stoppingtimeOurs, axis=0) - np.min(stoppingtimeOurs, axis=0)
deviationLUCB = np.max(stoppingtimeLUCB, axis=0) - np.min(stoppingtimeLUCB, axis=0)

#calculate the deviations
#check the presentation of deviation, should the upper bound and lower bound be the same number?
#计算错误率
print("Algorithm Finished")
np.savez('../GoodArmAuthenticData', GoodArmTrivialSolver, GoodArmAPTG, GoodArmHDoC, GoodArmOurs)

print(stoppingtimeTrivialSolver, GoodArmTrivialSolver)
print(stoppingtimeAPTG, GoodArmAPTG)
print(stoppingtimeHDoC, GoodArmHDoC)
print(stoppingtimeLUCB, GoodArmLUCB)
print(stoppingtimeOurs, GoodArmOurs)
# print(np.max(stoppingtimeTrivialSolver, axis=0), np.min(stoppingtimeTrivialSolver, axis=0))
# print(np.max(stoppingtimeAPTG, axis=0), np.min(stoppingtimeAPTG, axis=0))
# print(np.max(stoppingtimeHDoC, axis=0), np.min(stoppingtimeHDoC, axis=0))
# print(np.max(stoppingtimeLUCB, axis=0), np.min(stoppingtimeLUCB, axis=0))
# print(np.max(stoppingtimeOurs, axis=0), np.min(stoppingtimeOurs, axis=0))
