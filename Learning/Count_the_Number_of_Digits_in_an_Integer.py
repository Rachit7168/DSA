# TODO : method : 1
n = 7168
num = n
count = 0

while num > 0 :
    count += 1  # 1 # 2 # 3 # 4
    num = num // 10 # 716 # 71 # 7 # 0
print(count)

#TODO : Method 2 

from math import *

def count_digits(n):
    return int(log10(n) + 1)

print(count_digits(n=7168))