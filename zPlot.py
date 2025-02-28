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

MultiAPT = [75328.34, 73560.74, 72622.76, 72057.81, 71467.46, 71058.83, 70595.21, 70224.09, 69923.4, 69626.79]
MultiHDoC = [105621.92, 104300.77333333, 103886.48, 103616.78666667, 103407.16, 103204.61333333, 102694.12, 102593.69333333, 102347.28, 101928.06666667]
MultiLUCB = [128794.28, 99858.82, 87023.33, 78205.42, 73460.9, 68324.32, 66644.87, 64416.08, 60297.87, 58390.3]
MultiOurs = [38388.93, 37575.47, 36985.4, 36697.66, 36441.8, 36156.92, 36022.13, 35858.99, 35688.19, 35612.44]

APTDeviation = [10524.8554814, 10303.40504651, 10398.9975143, 10466.26298131, 10411.3360578, 10419.8311416, 10408.67057822, 10277.29404473, 10343.8626209, 10419.43031005]
HDoCDeviation = [69187.32772955, 68797.98075695, 68817.46060503, 68860.23546756, 68852.12910649, 68894.51894627, 68621.22604561, 68647.82947933, 68605.31534831, 68261.52147841]
LUCBDeviation = [18285.95346985, 14020.23004189, 12103.6977086, 11759.98953501, 10313.08249603, 11141.2728796, 10423.346871, 10055.89515327, 8601.73790191, 9663.53656122]
OursDeviation = [7628.03459124, 7662.22721727, 7635.25301218, 7612.82884376, 7539.96554501, 7667.72471034, 7693.57635389, 7632.13881228, 7758.78525504, 7662.83259287]


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
ax.set_xlim(delta_block, delta_block * (plot_x_number))
ax.set_xticks(np.arange(delta_block, delta_block * (plot_x_number + 1), step=delta_block))

plt.yticks(fontweight='bold')


plt.ylim(ymin = 0)
plt.xlim(xmin = delta_block)

plt.grid(b=None, which='major', axis='both')
plt.xlabel("Confidence Bound", fontsize=16, fontweight='bold')
plt.ylabel("Stopping Time", fontsize=16, fontweight='bold')
plt.ylabel("Stopping Time", fontsize=16, fontweight='bold')

plt.rcParams.update({'font.size': 14})
font = {'style': 'normal', 'weight': 'bold'}

# plt.tight_layout()
plt.legend(frameon=False, loc=9, ncol=2, bbox_to_anchor=(0.5, 1.18), prop=font)
plt.savefig("/Users/jiangxuanke/Desktop/ECML2025/SyntheticDelta.pdf", dpi=600, format='pdf', bbox_inches='tight')

plt.show()