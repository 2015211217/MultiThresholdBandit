import numpy as np

M = 4
K = 10
bmmu_1 = [0.1, 0.1, 0.1, 0.35, 0.45, 0.55, 0.65, 0.2, 0.2, 0.2]
bmmu_2 = [0.2, 0.4 - np.power(0.2, 2), 0.4 - np.power(0.2, 3), 0.4 - np.power(0.2, 4), 0.45, 0.55, 0.6 + np.power(0.1, 5), 0.6 + np.power(0.1, 4), 0.6 + np.power(0.1, 3), 0.6 + np.power(0.1, 2), 0.6 + np.power(0.1, 1)]
bmmu_3 = [0.05, 0.1, 0.15, 0.2, 0.45, 0.55, 0.65, 0.7, 0.75, 0.8]
bmmu_4 = [0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6]
simga = np.random.rand()

###form the input matrix
input_matrix = [bmmu_1, bmmu_2, bmmu_3, bmmu_4]
print(input_matrix)

# if __name__ == '__main__':
