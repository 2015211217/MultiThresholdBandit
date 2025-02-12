import matplotlib.pyplot as plt
import numpy as np
devices_block = 1
plot_x_number = 10
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

fig, ax = plt.subplots()

timearray = np.zeros(plot_x_number)
for i in range(plot_x_number):
    timearray[i] = (i+1) * devices_block

plt.plot(timearray,[12.621,30.809,45.402, 60.939, 74.219, 89.928, 105.938, 123.536, 141.933, 159.463],"k-.d",label="Trivial Solver")
plt.plot(timearray,[19.57, 43.75, 81.17, 121.22, 161.35, 199.45, 239.11, 276.87, 314.57, 353.18],"g-.^",label="MultiAPT-G")
plt.plot(timearray,[55.437, 94.035, 133.201, 172.487, 211.143, 249.755, 288.074, 326.65, 363.16, 398.392],color = "", linestyle = '-.', marker = '*', label="MultiHDoC")
plt.plot(timearray,[115.577, 180.983, 228.775, 268.296, 302.765, 333.714, 362.136, 388.448, 413.145, 436.473],"r-.h",label="MultiTUCB")

# plt.yticks(np.arange(1, 6, step = 4))
plt.tick_params(labelsize = 14)
plt.xticks(np.arange(1, 11, step = 1), fontweight = 'bold')
plt.tick_params(labelsize = 14)
plt.yticks(fontweight = 'bold')

plt.ylim(ymin = 0)
plt.xlim(xmin = 1)

plt.grid(b=None, which='major', axis='both')
# plt.title("")
plt.xlabel("", fontsize = 14, fontweight = 'bold')

plt.ylabel("", fontsize = 16, fontweight = 'bold')
# plt.ylabel("Average Connected Rate (%)", fontsize = 16, fontweight = 'bold')
#, bbox_to_anchor = (num1, ), loc = , borderaxespad =

plt.rcParams.update({'font.size': 14})
font = {'style': 'normal', 'weight': 'bold'}
plt.legend(frameon=False, loc=9, ncol=2, bbox_to_anchor=(0.5, 1.18), prop=font)

plt.savefig('DifferentDelta.pdf', format='pdf')
# plt.savefig('TimeSlotConnectedRate.png', format='png')

plt.show()