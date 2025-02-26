import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

delta_block = 0.005
plot_x_number = 10

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
fig, ax = plt.subplots()
timearray = np.zeros(plot_x_number)
for i in range(plot_x_number):
    timearray[i] = (i+1) * delta_block

MultiAPT = [160327.25, 149014.45652174, 149530.15555556, 142086.46808511,147100.34782609, 167917.51219512, 132421.83673469, 146453.64444444,152517.37777778, 122454.51020408]
MultiHDoC = [1535.3,  1812.72, 1465.92, 4063.76, 1710.16, 1781.12, 1607.48, 1620.62, 1497.16,
 1240.04]
MultiLUCB = [3098.68, 2876.78, 2501.02, 2465.04, 2542.28, 2185.06, 2125.74, 2140.16, 2115.58,
 2101.16]
MultiOurs = [1308.3,  1283.32, 1113.9,  1479.92, 1365.34, 1182.18, 1368.08, 1516.72, 1219.76, 1426.12]

APTDeviation = [38386.29641724, 40849.41320589, 37417.99464596, 35287.5673314, 40396.03507837, 53007.60101729, 36010.5473857,  39589.88414623, 45739.74331533, 32524.95234664]

HDoCDeviation = [1287.62439011,  2045.0580827,   1473.14240778, 1641.87179821, 2088.92693372,  2134.20964893,  1675.18984285,  1475.34485311,1935.6789647, 1264.32274297]
LUCBDeviation = [1095.7099149, 794.37274097, 688.73668379, 756.88712395, 779.05807332, 744.30510975, 757.81833733, 661.85670232, 912.88328038, 716.11346475]
OursDeviation = [823.29426695, 565.27524057,  410.01332905, 2053.6300625, 1198.00189666, 1067.77320982, 1322.8584783, 1647.52989703,  957.95564741, 1656.54098217]

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
ax.fill_between(timearray, HDoCLower, HDoCUpper, color ="g", alpha=0.1)

ax.plot(timearray, MultiLUCB, color="b", linestyle='-.', marker='*', label="MultiHDoC")
ax.fill_between(timearray, LUCBLower, LUCBUpper, color="b", alpha=0.1)

ax.plot(timearray, MultiOurs, "r-.h", label="MultiTUCB")
ax.fill_between(timearray, OursLower, OursUpper, color="r", alpha=0.1)

# plt.yticks(np.arange(1, 6, step = 4))
ax.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))
ax.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
ax.yaxis.get_offset_text().set_fontsize(16)
ax.xaxis.get_offset_text().set_fontsize(16)

# plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter()) 如何做百分数

plt.tick_params(labelsize=14)
plt.xticks(fontweight='bold')
ax.set_xticks(np.arange(delta_block, delta_block * (plot_x_number + 1), step=delta_block))

plt.yticks(fontweight='bold')

plt.ylim(ymin = 0)
plt.xlim(xmin = delta_block)

plt.grid(b=None, which='major', axis='both')
plt.xlabel("Confidence Bound", fontsize=16, fontweight='bold')
plt.ylabel("Stopping Time", fontsize=16, fontweight='bold')
plt.rcParams.update({'font.size': 14})
font = {'style': 'normal', 'weight': 'bold'}

# plt.tight_layout()
plt.legend(frameon=False, loc=9, ncol=2, bbox_to_anchor=(0.5, 1.18), prop=font)

# plt.savefig('SyntheticDelta.pdf', format='pdf', bbox_inches = 'tight')

plt.show()