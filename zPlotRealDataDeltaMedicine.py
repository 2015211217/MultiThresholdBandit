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


MultiAPT = [159632.82943144, 150893.49019608, 146577.35459459, 142996.07708779, 140378.18490967, 137828.06765328,
     135861.16998951, 134781.87735849, 133787.23769634, 132886.51046025]
MultiHDoC = [2029.522, 1977.541, 1948.431, 1930.845, 1915.501, 1903.401, 1894.292, 1888.086, 1882.113, 1873.55]
MultiLUCB = [3204.127, 2790.962, 2662.78, 2485.282, 2377.705, 2262.388, 2239.135, 2085.042, 2064.848, 2008.759]
MultiOurs = [1654.104, 1611.449, 1588.862, 1568.517, 1556.477, 1544.531, 1531.553, 1522.434, 1516.436, 1510.738]

APTDeviation = [40486.05851915, 39227.44442852, 39267.97317036, 39000.39356306, 38710.65058721, 38258.85509071, 38070.14374243,
     38043.5065537, 38169.41400362, 38032.59847124]
HDoCDeviation = [6277.95483255, 6148.12027748, 6136.71855353, 6120.68424908, 6103.42505549, 6098.67129563, 6092.35362768,
     6090.57123188, 6078.31273844, 6074.75748927]
LUCBDeviation = [974.94906989, 856.3345506, 856.67674627, 806.8319072, 782.59691794, 729.8126153, 763.87393382, 705.09719772,
     699.26410382, 678.39591753]
OursDeviation = [6079.60310162, 5954.84430455, 5941.58978565, 5923.7232273, 5919.56934662, 5912.52421145, 5910.70541266,
     5896.30321877, 5895.68469899, 5894.54876877]

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
ax.plot(timearray, MultiLUCB, "g-.^", label="MultiLUCB")
# ax.fill_between(timearray, LUCBLower, LUCBUpper, color="b", alpha=0.1)

ax.plot(timearray, MultiHDoC, color="b", linestyle='-.', marker='*', label="MultiHDoC")
# ax.fill_between(timearray, HDoCLower, HDoCUpper, color ="g", alpha=0.1)

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

ax.set_ylim(1500, 3500)
ax.set_yticks(np.arange(1000, 4000, step=500))
plt.yticks(fontweight='bold')

plt.ylim(ymin=1500)
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