import csv
import numpy as np
import sys
import matplotlib.pyplot as plt
import math


data_path = sys.argv[1]
stats_file = 'stats.txt'

with open(data_path, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    headers = next(reader)
    data = np.array(list(reader)).astype(int)

broken_packets = data[:, 0]

with open(stats_file, 'w') as resultFile:
    resultFile.write('Measurments: ' + headers[0] + '\nPercentage of ones: ' + headers[1] + '\nPackets sent: ' + headers[2])
    resultFile.write('\nAverage packets broken: ' + str(np.mean(broken_packets)))
    resultFile.write('\nStandard deviation: ' + str(np.std(broken_packets)))
    quartiles = np.percentile(broken_packets, [25, 50, 75])
    max_value = np.max(broken_packets)
    min_value = np.min(broken_packets)
    resultFile.write('\n\n\n\n\tFIVE-NUMBER SUMMARY\n')
    resultFile.write('\tQ0 (minimum) = ' + str(min_value))
    resultFile.write('\n\tQ1 = ' + str(quartiles[0]))
    resultFile.write('\n\tQ2 = ' + str(quartiles[1]))
    resultFile.write('\n\tQ3 = ' + str(quartiles[2]))
    resultFile.write('\n\tQ4 (maximum) = ' + str(max_value))
    
fig, axs = plt.subplots(1, 2, tight_layout=True)
axs[0].set_title('Boxplot of broken packets')
axs[0].boxplot(broken_packets)

##GENERATE HIStOGRAM

n_points = int(headers[0])
n_bins = 1 + math.floor(3.3*math.log(n_points))

axs[1].set_title('Hisogram of broken packets')
axs[1].hist(broken_packets, bins=n_bins)
plt.show()