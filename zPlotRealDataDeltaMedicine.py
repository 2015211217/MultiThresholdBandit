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

MultiAPT = [168464.60227273, 164010.56818182, 160077.52808989, 156394.01111111, 155142.52222222, 150629.40659341, 149706.83516484, 149331.6043956, 148355.07692308, 147793.96703297]
MultiHDoC = [1996.62, 1952.94, 1936.25, 1911., 1892., 1876.81, 1871.06, 1860.7,  1855.09, 1849.62]
MultiLUCB = [3199.52, 2772.84, 2787.39, 2586.97, 2423.6,  2237.14, 2342.78, 2157.87, 2092.71, 2023.79]
MultiOurs = [1597.06, 1560.37, 1540.89, 1508.52, 1495.97, 1480.3,  1472.21, 1464.87, 1460.68, 1453.33]

APTDeviation = [39652.82242691, 39941.22511534, 40398.93081942, 39735.35328158, 39414.17157739, 38367.26180979, 38273.09955206, 38296.01670096, 38073.22663265, 38105.18972016]
HDoCDeviation = [2116.67911493, 2083.46007795, 2073.69486847, 2047.51759455, 2021.82244028, 2008.28601895, 2006.38509673, 1985.10533474, 1984.87183513, 1983.96353686]
LUCBDeviation = [948.11974434, 894.13253738, 915.54513701, 835.16907815, 808.14570468, 778.97821561, 880.62160523, 759.41318997, 720.49098946, 784.67388506]
OursDeviation = [1724.47688775, 1705.46838525, 1687.12323732, 1658.73858989, 1643.70148418, 1635.1673951,  1630.69404423, 1622.83684734, 1616.0078829,  1616.64914595]

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

# y_delta_block = 20000
# plot_y_number = 7
# ax.set_ylim(y_delta_block, y_delta_block * (plot_y_number))
# ax.set_yticks(np.arange(y_delta_block, y_delta_block * (plot_y_number + 1), step=y_delta_block))

plt.grid(b=None, which='major', axis='both')
plt.xlabel("Confidence Bound", fontsize=16, fontweight='bold')
plt.ylabel("Stopping Time", fontsize=16, fontweight='bold')

plt.rcParams.update({'font.size': 14})
font = {'style': 'normal', 'weight': 'bold'}

# plt.tight_layout()
plt.legend(frameon=False, loc=9, ncol=2, bbox_to_anchor=(0.5, 1.18), prop=font)
plt.savefig('MedicineDelta.eps', dpi=600, format='eps', bbox_inches='tight')

plt.show()