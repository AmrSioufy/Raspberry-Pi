#!/usr/bin/python3

import random

Random_no = random.uniform(1, 120)
Lst1 = []
for i in range(10):
    Number = Random_no + i
    Lst1.append(round(Number, 2))
    Lst2 = Lst1[::-1]
print("Acceleration")
for i in Lst1:
    print(i)

print("Deceleration")
for i in Lst2:
    print(i)

