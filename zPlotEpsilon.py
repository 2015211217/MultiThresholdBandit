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

MultiAPT = [77073.04, 77235.86, 76401.88, 76417.06, 79521.82, 83200.27, 86392.76, 90218.45, 92935.68, 101926.55]
MultiHDoC = [137095.63, 129949.23, 123153.38, 115880.04, 107357.78, 104795.58, 101888.33, 94329.35, 90826.88, 86954.7]
MultiLUCB = [123365.56944444, 99942.1025641, 76164.15384615, 76574.2195122, 90373.29577465, 96981.11842105, 86289.91025641, 60956.98795181, 86190.05063291, 87814.54545455]
MultiOurs = [45490.58, 43501.53, 39273.98, 36932.72, 34455.85, 33521.2, 30628.44, 29066.3, 26515.7, 25956.31]

APTDeviation = [54193., 55249., 52649., 38241., 70537.,  50711.,  54547.,  71999.,  66546.,  79601.]
HDoCDeviation = [171661.,  163772.,  113808.,  142355.,  114255.,  170566.,  165775.,  124643.,  182286., 176209.]
LUCBDeviation = [91337., 78973.,  74449.,  75289.,  68099.,  72019.,  74649.,  93820.,  77650.,  83329.]
OursDeviation = [35422.,  41370.,  37758.,  28628.,  29393.,  32725.,  26843.,  24099.,  29419.,  19715.]

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

plt.plot(timearray, MultiAPT, "k-.d", label="MultiAPT")
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

plt.savefig('SyntheticEpsilon.eps', dpi=600, format='eps', bbox_inches='tight')
plt.show()