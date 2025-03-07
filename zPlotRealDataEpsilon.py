import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

epsilon_block = 0.002
plot_x_number = 10

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
fig, ax = plt.subplots()
timearray = np.zeros(plot_x_number)
for i in range(plot_x_number):
    timearray[i] = (i+1) * epsilon_block


MultiAPT = [131837.971, 189177.667, -1.00000000e+00, -1.00000000e+00, -1.00000000e+00, -1.00000000e+00, -1.00000000e+00, -1.00000000e+00, -1.00000000e+00, -1.00000000e+00]
MultiHDoC = [77731.56818182, 72144.11363636, 68102.63636364, 63852.40909091, 60526.70454545, 58767.63636364, 56171.81818182, 54200.22727273, 52529.11363636, 51035.15909091]
MultiLUCB = [132270.42857143, 118795.5, 108644.76,  99548.98, 92850.06,  85611.04, 80354.2, 74724.3, 69439.22, 64501.92]
MultiOurs = [45568.66, 41282.56, 37040.96, 33362.08, 30328.18, 27537.26, 24944.5,  23448.36, 22043.88, 20803.88]

APTDeviation = [28738.60309591, 86699.53090811, 0,  0,  0,  0,  0,  0,  0,  0]
HDoCDeviation = [51305.62127152, 50598.73379773, 50971.70043627, 50672.64194078, 51264.38908832, 51353.08657769, 51437.37430073, 51548.53523006, 51801.54086298, 52102.40228022]
LUCBDeviation = [29813.09463322, 29263.20515613, 28107.38714471, 25958.90307582, 24866.48135335, 23856.56078731, 22650.88517034, 22021.29396766, 20045.84832457, 18514.72235475]
OursDeviation = [12653.77923248, 11493.87632465, 10155.159461,  8967.8072188,  8936.4669701, 8752.67271594,  7510.34543347,  7045.0471191,  6845.2543726, 6635.4827274, ]


APTLower = np.zeros(plot_x_number)
HDoCLower = np.zeros(plot_x_number)
LUCBLower = np.zeros(plot_x_number)
OursLower = np.zeros(plot_x_number)
APTUpper = np.zeros(plot_x_number)
HDoCUpper = np.zeros(plot_x_number)
LUCBUpper = np.zeros(plot_x_number)
OursUpper = np.zeros(plot_x_number)

for i in range(plot_x_number):
    APTLower[i] = MultiAPT[i] - APTDeviation[i]
    HDoCLower[i] = MultiHDoC[i] - HDoCDeviation[i]
    LUCBLower[i] = MultiLUCB[i] - LUCBDeviation[i]
    OursLower[i] = MultiOurs[i] - OursDeviation[i]
    APTUpper[i] = MultiAPT[i] + APTDeviation[i]
    HDoCUpper[i] = MultiHDoC[i] + HDoCDeviation[i]
    LUCBUpper[i] = MultiLUCB[i] + LUCBDeviation[i]
    OursUpper[i] = MultiOurs[i] + OursDeviation[i]

# plt.plot(timearray, MultiAPT, "k-.d", label="MultiAPT")
# plt.fill_between(timearray, APTLower, APTUpper, color ="k", alpha=0.1)
# ax.plot(timearray, MultiAPT)

ax.plot(timearray, MultiHDoC, "g-.^", label="MultiLUCB")
# ax.fill_between(timearray, HDoCLower, HDoCUpper, color ="g", alpha=0.1)

ax.plot(timearray, MultiLUCB, color="b", linestyle='-.', marker='*', label="MultiHDoC")
# ax.fill_between(timearray, LUCBLower, LUCBUpper, color="b", alpha=0.1)

ax.plot(timearray, MultiOurs, "r-.h", label="MultiTUCB")
# ax.fill_between(timearray, OursLower, OursUpper, color="r", alpha=0.1)

# plt.yticks(np.arange(1, 6, step = 4))
ax.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
ax.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
ax.yaxis.get_offset_text().set_fontsize(16)
ax.xaxis.get_offset_text().set_fontsize(16)

# plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter()) 如何做百分数

plt.tick_params(labelsize=14)
plt.xticks(fontweight='bold')
ax.set_xlim(epsilon_block, epsilon_block * (plot_x_number))
ax.set_xticks(np.arange(epsilon_block, epsilon_block * (plot_x_number + 1), step= epsilon_block))

plt.yticks(fontweight='bold')

y_epsilon_block = 20000
plot_y_number = 7
ax.set_ylim(y_epsilon_block, y_epsilon_block * (plot_y_number))
ax.set_yticks(np.arange(y_epsilon_block, y_epsilon_block * (plot_y_number + 1), step=y_epsilon_block))

plt.ylim(ymin = 20000)
plt.xlim(xmin = epsilon_block)

plt.grid(b=None, which='major', axis='both')
plt.xlabel("Accuracy Rate", fontsize=14, fontweight='bold')
plt.ylabel("Stopping Time", fontsize=16, fontweight='bold')
plt.rcParams.update({'font.size': 14})
font = {'style': 'normal', 'weight': 'bold'}

# plt.tight_layout()
plt.legend(frameon=False, loc=9, ncol=2, bbox_to_anchor=(0.5, 1.18), prop=font)
plt.savefig('Epsilon2019.eps', dpi=600, format='eps', bbox_inches='tight')

plt.show()