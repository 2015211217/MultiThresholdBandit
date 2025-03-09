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


MultiAPT = [0, 139660.78461538, 134110.11940299, 129392.08695652, 125092.54929577, 122661.875, 120122.35616438, 119713.83561644, 119285.73972603, 118846.61643836]
MultiHDoC = [59348.25, 57818.00, 57176.35869565, 56566.86956522, 56201.05434783, 55951.93478261, 55634.29347826, 55567.54347826, 55433.69565217, 55360.5326087 ]
MultiLUCB = [111903.26, 91904.04, 89800.85, 80105.83, 73413.65, 74297.02, 68761.95, 64713.34, 65438.83, 61324.43]
MultiOurs = [41921.5959596, 40775.3030303, 40166.83838384, 39837.21212121, 39631.5959596, 39439.39393939, 39083.58585859, 38903.78787879, 38756.50505051, 38504.11111111]

APTDeviation = [0, 100080.08512278, 91295.93218113, 83421.39166023, 76129.45454487, 72537.37834712, 68975.36025101, 68781.48849052, 68663.01893242, 68441.44528344]
HDoCDeviation = [45352.96800913,44321.95393775, 44203.18904906, 44296.45333723, 44397.87016324, 44402.80413543, 44486.87855443, 44509.74914741, 44556.53913476, 44560.69088722]
LUCBDeviation = [26462.53572605, 21347.44232498, 21400.85983524, 19518.11142814, 18706.89687862, 18408.84262249, 17490.58056977, 19915.69761631, 17704.36695341, 15748.51881369]
OursDeviation = [24127.98584002, 24200.54696781, 24137.54189912, 24197.8959193, 24229.07513467, 24301.3892718,  24432.94438777, 24375.02807298, 24374.8444915,  24367.8607728 ]

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

plt.yticks(fontweight='bold')
y_delta_block = 20000
plot_y_number = 6
ax.set_ylim(y_delta_block, y_delta_block * (plot_y_number))
ax.set_yticks(np.arange(y_delta_block, y_delta_block * (plot_y_number + 1), step=y_delta_block))

plt.ylim(ymin=20000)
plt.xlim(xmin=delta_block)

plt.grid(b=None, which='major', axis='both')
plt.xlabel("Confidence Bound", fontsize=16, fontweight='bold')
plt.ylabel("Stopping Time", fontsize=16, fontweight='bold')
plt.rcParams.update({'font.size': 14})
font = {'style': 'normal', 'weight': 'bold'}

# plt.tight_layout()
plt.legend(frameon=False, loc=9, ncol=2, bbox_to_anchor=(0.5, 1.18), prop=font)

# plt.savefig('SyntheticDelta.pdf', format='pdf', bbox_inches = 'tight')
plt.savefig('Delta2019.eps', dpi=600, format='eps', bbox_inches='tight')

plt.show()