import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import fileinput
import itertools


depths = []
with fileinput.input(files=('input.txt')) as f:
    for line in f:
        depths.append(int(line))

# PART I
copy = []


def increasing(inc_list, depths_list):
    for i in range(0, len(depths_list)):
        if i == 0:
            inc_list.append(None)
        elif depths_list[i] > depths_list[i - 1]:
            inc_list.append(True)
        else:
            inc_list.append(False)
    return inc_list


increase = increasing(copy, depths).count(True)
print("How many measurements are larger than the previous measurement? ", increase)

# PART II
sums = []

for i in range(0,len(depths)-2):
    sums.append(sum(depths[i:i+3]))

copy2 = []

increase2 = increasing(copy2, sums).count(True)
print("How many sums are larger than the previous sum? ", increase2)

