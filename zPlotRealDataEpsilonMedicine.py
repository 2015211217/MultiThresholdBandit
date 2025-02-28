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


MultiAPT = [-1, 181674.58823529, 144819.64210526, 116853.30927835, 95530.54, 81274.29, 69567.81, 59540.05, 53113.02, 47289.76]
MultiHDoC = [2081.5, 2030.25, 1973.06, 1930.39, 1898.61, 1835.34, 1788.18, 1754.77, 1731.85, 1696.29]
MultiLUCB = [3284.41, 3229.69, 3173.31, 3122.85, 3071.79, 3008.21, 2967.97, 2919.15, 2867.15, 2816.32]
MultiOurs = [1693.13, 1618.8, 1585.53, 1546.54, 1508.42, 1473.02, 1422.95, 1387.44, 1350.8, 1327.74]

APTDeviation = [-1, 77896.11808452, 34931.99305498, 30578.90747699, 26363.82198598, 22850.2680677, 20340.80240978, 15810.40939974, 14478.15645031, 12240.33426841]
HDoCDeviation = [2269.77276616, 2165.37264403, 2083.25188981, 2006.03156453, 1950.39087823, 1831.98543782, 1771.07654482, 1736.97218662, 1716.52777068, 1672.55527439]
LUCBDeviation = [1001.53818794, 975.6932786, 946.89827009, 926.59055008, 906.23394656, 889.84196681, 876.95117829, 874.40320648, 866.23351788, 868.68628261]
OursDeviation = [1986.43889236, 1762.85317029, 1700.04494326, 1633.87413481, 1535.50224474, 1445.13391061, 1362.84951756, 1253.00673039, 1190.12890058, 1166.27057427]

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
# plt.fill_between(timearray, APTLower, APTUpper, color ="k", alpha=0.2)
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

ax.set_ylim(1000, 3500)
ax.set_yticks(np.arange(1000, 4000, step=500))
plt.ylim(ymin=1000)
plt.xlim(xmin=epsilon_block)

plt.grid(b=None, which='major', axis='both')
plt.xlabel("Confidence Bound", fontsize=16, fontweight='bold')
plt.ylabel("Stopping Time", fontsize=16, fontweight='bold')
plt.rcParams.update({'font.size': 14})
font = {'style': 'normal', 'weight': 'bold'}

# plt.tight_layout()
plt.legend(frameon=False, loc=9, ncol=2, bbox_to_anchor=(0.5, 1.18), prop=font)

# plt.savefig('SyntheticDelta.pdf', format='pdf', bbox_inches = 'tight')
plt.savefig('RealdataEpsilonMedicine.pdf', dpi=600, format='pdf', bbox_inches='tight')

plt.show()