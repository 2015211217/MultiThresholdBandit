import numpy as np
from TrivialSolver import TrivialSolver
M = 4
K = 10
bmmu_1 = [0.1, 0.1, 0.1, 0.35, 0.45, 0.55, 0.65, 0.2, 0.2, 0.2]
bmmu_2 = [0.2, round(0.4 - np.power(0.2, 2), 6), round(0.4 - np.power(0.2, 3), 6),round(0.4 - np.power(0.2, 4), 6)
    , 0.45, 0.55, round(0.6 + np.power(0.1, 5), 6), round(0.6 + np.power(0.1, 4), 6), 0.6 + round(np.power(0.1, 3), 6), round(0.6 + np.power(0.1, 2), 6), round(0.6 + np.power(0.1, 1), 6)]
bmmu_3 = [0.05, 0.1, 0.15, 0.2, 0.45, 0.55, 0.65, 0.7, 0.75, 0.8]
bmmu_4 = [0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6]
sigma = round(np.random.rand(), 6)

###form the input matrix
input_matrix = [bmmu_1, bmmu_2, bmmu_3, bmmu_4]
print(input_matrix)
if __name__ == '__main__':
    TrivialSolver(K, M, input_matrix)