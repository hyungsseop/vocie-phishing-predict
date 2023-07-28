start = [7.0, 8.0, 9.0, 10.0, 12.0, 12.0, 22.0, 27.0, 32.0, 34.0, 36.0, 74.0, 86.0, 87.0, 90.0, 96.0, 98.0, 100.0, 105.0]
end = [8.0, 10.0, 10.0, 12.0, 13.0, 28.0, 23.0, 32.0, 34.0, 36.0, 74.0, 86.0, 88.0, 90.0, 96.0, 97.0, 100.0, 105.0, 107.0]

import numpy as np

time_stamp = []
flag = True
time_stamp.append(0)
for i in range(len(end)-1):
    if end[i+1] - end[i] > 20:
        tmp = int(np.ceil(end[i+1] - end[i])/19)
        for j in range(tmp):
            time_stamp.append(time_stamp[-1]+19)
    elif int(end[i]) - time_stamp[-1] >20:
        time_stamp.append(int(end[i-1])) 
time_stamp.append(int(end[-1]))

print(time_stamp)
