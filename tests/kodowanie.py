
from datetime import datetime


start = datetime.now()
for _ in range(1000000):
    l2 = [[13, 3, 19, 8, 18, 17], [15, 6, 9, 14, 11], [20, 7, 16, 1, 5, 4, 12, 10, 2]]
    to_add = l2[0][4:]
    l2[0] = l2[0][:4]
    l2[1] = to_add + l2[1] + l2[2][:3]
    l2[2] = l2[2][3:]
stop = datetime.now()
print(stop-start)


start = datetime.now()
for _ in range(1000000):
    l1 = [[13, 3, 19, 8, 18, 17, 15, 6, 9, 14, 11, 20, 7, 16, 1, 5, 4, 12, 10, 2], [6, 5, 9]]
    l1[1] = [4,10,6]
stop = datetime.now()
print(stop-start)