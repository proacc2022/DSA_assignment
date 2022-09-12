class Slot:
    def __init__(self, x, y):
        self.time = x
        self.index = y


input_file = open("2.in")
row = input_file.read().strip().split('\n')
no_lifeguards = int(row[0])
row.pop(0)
list = [0] * 2 * no_lifeguards
total_time = 0
uniqtime = [0] * no_lifeguards
last_time = 0
unique_time_set = set()
max_common_time = 0

for l in range(no_lifeguards):
    stamp = row[l].split(' ')
    list[2 * l] = Slot(int(stamp[0]), l)
    list[2 * l + 1] = Slot(int(stamp[1]), l)

list.sort(key=lambda state: state.time)

for s in list:
    if len(unique_time_set) == 1:
        for loneitem in unique_time_set:
            uniqtime[loneitem] += s.time - last_time
    if len(unique_time_set) > 0:
        total_time += s.time - last_time
    if s.index in unique_time_set:
        unique_time_set.remove(s.index)
    else:
        unique_time_set.add(s.index)
    last_time = s.time

for t in uniqtime:
    max_common_time = max(max_common_time, total_time - t)
print(max_common_time, file=open("2.out", 'w'))
