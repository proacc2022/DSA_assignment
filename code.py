import numpy as np

input_file = open("1.in")
rows = input_file.read().strip().split('\n')
no_lifeguards = int(rows[0])
rows.pop(0)
arr = np.zeros((no_lifeguards*2, 2))
total_time = 0
uniqtime = [0] * no_lifeguards
last_time = 0
unique_time_set = []
max_common_time = 0
i, j = 0 ,0

while i < no_lifeguards*2:
    shift_time = rows[j].split(' ')
    arr[i, 0] = int(shift_time[0])
    arr[i+1, 0] = int(shift_time[1])
    arr[i, 1] = int(j)
    arr[i+1, 1] = int(j)
    i = i +2
    j = j +1
arr = arr.astype(int)
arr = arr[arr[:, 0].argsort()]

for ar in range(no_lifeguards*2):
    if len(unique_time_set) == 1:
        for loneitem in unique_time_set:
            uniqtime[loneitem] += (arr[ar, 0]) - last_time
    if len(unique_time_set) > 0:
        total_time += (arr[ar, 0]) - last_time
    if arr[ar, 1] in unique_time_set:
        unique_time_set.remove(arr[ar, 1])
    else:
        unique_time_set.append(arr[ar, 1])
    last_time = (arr[ar, 0])

for t in uniqtime:
    maximum_common_time = max(max_common_time, total_time - t)
print(max_common_time, file=open("1.out", 'w')
