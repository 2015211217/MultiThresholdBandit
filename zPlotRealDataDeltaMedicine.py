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

MultiAPT = []
MultiHDoC = []
MultiLUCB = []
MultiOurs = []

APTDeviation = []
HDoCDeviation = []
LUCBDeviation = []
OursDeviation = []

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

# plt.plot(timearray, MultiHDoC, "g-.^", label="MultiLUCB")
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
ax.set_xlim(delta_block, delta_block * (plot_x_number))
ax.set_xticks(np.arange(delta_block, delta_block * (plot_x_number + 1), step=delta_block))

ax.set_ylim(1000, 3500)
ax.set_yticks(np.arange(1000, 4000, step=500))
plt.yticks(fontweight='bold')

# plt.ylim(ymin=1000)
# plt.xlim(xmin=delta_block)

plt.grid(b=None, which='major', axis='both')
plt.xlabel("Confidence Bound", fontsize=16, fontweight='bold')
plt.ylabel("Stopping Time", fontsize=16, fontweight='bold')
plt.ylabel("Stopping Time", fontsize=16, fontweight='bold')

plt.rcParams.update({'font.size': 14})
font = {'style': 'normal', 'weight': 'bold'}

# plt.tight_layout()
plt.legend(frameon=False, loc=9, ncol=2, bbox_to_anchor=(0.5, 1.18), prop=font)
plt.savefig("/Users/jiangxuanke/Desktop/ECML2025/RealdataMedicineDelta.eps", dpi=600, format='eps', bbox_inches='tight')

plt.show()