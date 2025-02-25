import matplotlib.pyplot as plt
import numpy as np

delta_block = 1
plot_x_number = 10

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

fig, ax = plt.subplots()

timearray = np.zeros(plot_x_number)
for i in range(plot_x_number):
    timearray[i] = (i+1) * delta_block

APTDeltaResult = [12.621,30.809,45.402, 60.939, 74.219, 89.928, 105.938, 123.536, 141.933, 159.463]
HDoCDeltaResult = [19.57, 43.75, 81.17, 121.22, 161.35, 199.45, 239.11, 276.87, 314.57, 353.18]
LUCBDeltaResult = [55.437, 94.035, 133.201, 172.487, 211.143, 249.755, 288.074, 326.65, 363.16, 398.392]
OursDeltaResult = [115.577, 180.983, 228.775, 268.296, 302.765, 333.714, 362.136, 388.448, 413.145, 436.473]
lowerAPT = [10 * i for i in range(plot_x_number)]
upperAPT = [20 * i for i in range(plot_x_number)]

plt.plot(timearray, APTDeltaResult ,"k-.d",label="MultiAPT")
plt.fill_between(timearray, lowerAPT, upperAPT, color ="k", alpha = 0.2)

plt.plot(timearray,HDoCDeltaResult, "g-.^",label="MultiLUCB")
# plt.fill_between(HDoCDeltaResult, lowerAPT, upperAPT, color ="g", alpha = 0.2)

plt.plot(timearray, LUCBDeltaResult, color = "b", linestyle = '-.', marker = '*', label="MultiHDoC")
# plt.fill_between(LUCBDeltaResult, lowerAPT, upperAPT, color ="b", alpha = 0.2)

plt.plot(timearray,OursDeltaResult, "r-.h",label="MultiTUCB")
# plt.fill_between(LUCBDeltaResult, lowerAPT, upperAPT, color ="r", alpha = 0.2)

# plt.yticks(np.arange(1, 6, step = 4))
plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))

plt.tick_params(labelsize = 14)
plt.xticks(np.arange(delta_block, delta_block * plot_x_number, step = 1), fontweight = 'bold')
plt.tick_params(labelsize = 14)
plt.yticks(fontweight = 'bold')

plt.ylim(ymin = 0)
plt.xlim(xmin = 1)

plt.grid(b=None, which='major', axis='both')
plt.xlabel("Confidence Bound $\delta$", fontsize = 16, fontweight = 'bold')
plt.ylabel("Stopping time", fontsize = 16, fontweight = 'bold')
plt.rcParams.update({'font.size': 14})
font = {'style': 'normal', 'weight': 'bold'}

plt.legend(frameon=False, loc=9, ncol=2, bbox_to_anchor=(0.5, 1.18), prop=font)


# plt.savefig('SyntheticDelta.pdf', format='pdf')

plt.show()