inpu = list(map(int, input().split()))
products = 0
machines1 = list(map(int, input().split()))

machines2 = machines1.copy()
i = 0
while products != inpu[1]:
    current_machine = i % len(machines1)
    machines2[current_machine] -= 1
    if machines2[current_machine] == 0:
        products += 1
        machines2[current_machine] = machines1[current_machine]
    i += 1

import math
time = i /len(machines1)
print(math.ceil(time))